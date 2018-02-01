import re
import os
import subprocess
import logging
import tarfile

def match_size_string(sizestr):
    if re.match(r'^\d+[bBkKmMgG]?$', sizestr):
        return True
    else:
        return False

def parse_disk_desc(client, disk_desc):
    return disk_desc
    #segs = disk_desc.split(':')
    #if match_size_string(segs[0]):
    #    return disk_desc
    #else:
    #    img = client.images.get(segs[0])
    #    return img.id

def save_image_in_tmpdir(img_id):
    tar_path='/tmp/' + img_id + '.tar'
    image = docker_client.get_image(img_id)
    image_tar = open(tar_path, 'w')
    image_tar.write(image.data)
    image_tar.close()
    return tar_path

class process_tar(object):

    def __init__(self, path, instruct='extract'):
        self._path = path
        self._instruct = instruct

    def __enter__(self):
        target = ''
        if self._instruct == 'extract':
            # target is the directory for extracted things
            target = self._path[:-4]   # strip '.tar'
            tar = tarfile.open(self._path)
            tar.extractall(path=target)
            tar.close()
        else: # create a tar
            # target is tar file of output
            target = self._path + '.tar'
            tar = tarfile.open(self._path+'.tar', 'w')
            tar.add(self._path, arcname=os.path.basename(self._path))
            tar.close()
        return target

    def __exit__(self, type, value, traceback):
        try:
            subprocess.check_call(['sudo', 'rm', '-rf', self._path])
        except Exception as e:
            logging.error(e)

def extract_tar(path):
    with process_tar(path, 'extract') as tmpdir:
        return tmpdir

'''
    layer_list format [{id, pid, filepath}, ... ]
'''
def get_image_layers(name):
    layer_list = []
    history = get_image_history(name)
    for idx in range(0, len(history)-1):
        layer_list.append({'id': history[idx]['Id'],
                           'pid': history[idx+1]['Id']})
    layer_list.append({'id': history[-1]['Id'], 'pid': 'None'})

    tar_path = save_image_in_tmpdir(history[0]['Id'])
    tmp_path = extract_tar(tar_path)

    def get_subdir(a_dir):
        return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

    dirs = get_subdir(tmp_path)
    for dir in dirs:
        path = os.path.join(tmp_path, dir)
        basename = os.path.basename(path)
        with process_tar(path, 'create') as layer_tar:
            for l in layer_list:
                if l['id'] == basename:
                    l['file'] = layer_tar
                    l['name'] = ''
    layer_list[0]['name'] = name
    return (layer_list, tmp_path)

def get_image_history(name):
    output = None
    try:
        output = docker_client.history(name)
    except Exception as e:
        logging.error(e)

    return output

def search_image_in_local(name):
    ret = False
    try:
        docker_client.inspect_image(name)
    except:
        pass
    else:
        ret = True
    return ret

def load_image(image_path):
    try:
        with open(image_path, 'r') as image:
            docker_client.load_image(image)
    except Exception as e:
        logging.error(e)
