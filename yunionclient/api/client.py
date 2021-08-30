# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import json

from yunionclient.common import http

from yunionclient.api import zones
from yunionclient.api import keypairs
from yunionclient.api import hosts
from yunionclient.api import vpcs
from yunionclient.api import wires
from yunionclient.api import hostwires
from yunionclient.api import storages
from yunionclient.api import hoststorages
from yunionclient.api import cachedimages

from yunionclient.api import networks
from yunionclient.api import disks
from yunionclient.api import guests
from yunionclient.api import guestdisks
from yunionclient.api import guestnetworks
from yunionclient.api import groupnetworks

from yunionclient.api import groupguests

from yunionclient.api import flavors

from yunionclient.api import usages

from yunionclient.api import logs

from yunionclient.api import images

from yunionclient.api import vncproxy

from yunionclient.api import sshrelay

from yunionclient.api import quotas

from yunionclient.api import secgroups

from yunionclient.api import dnsrecords

from yunionclient.api import baremetalagents
from yunionclient.api import baremetals
from yunionclient.api import baremetalnetworks
from yunionclient.api import baremetalstorages

from yunionclient.api import reservedips

from yunionclient.api import scheduler

from yunionclient.api.stats import RegionStatsManager

from yunionclient.api import price_infos

from yunionclient.api.tenantinfo import TenantInfo, TenantInfoManager

from yunionclient.api import users
from yunionclient.api import tenants
from yunionclient.api import projects
from yunionclient.api import domains
from yunionclient.api import groups
from yunionclient.api import roles
from yunionclient.api import groupusers

from yunionclient.api import ec2credentials
from yunionclient.api import services
from yunionclient.api import endpoints
from yunionclient.api import schedtags
from yunionclient.api import metadatas
from yunionclient.api import loadbalancers
from yunionclient.api import dbinstances
from yunionclient.api import elasticcaches

from yunionclient.api import dnszones
from yunionclient.api import dnsrecordsets

from yunionclient.api import actionlogs

from yunionclient.api import filesystems
from yunionclient.api import buckets
from yunionclient.api import natgateways
from yunionclient.api import cloudaccounts
from yunionclient.api import cloudproviders


logger = logging.getLogger(__name__)


class Client(http.HTTPClient):
    """Client for Yunion Cloud API
    """

    def __init__(self, auth_url, username, password, domain_name,
                    region=None, zone=None, endpoint_type='internalURL',
                    timeout=600, insecure=False):
        """ Initialize a new client for the Images v1 API. """
        super(Client, self).__init__(timeout, insecure)

        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.domain_name = domain_name

        self.endpoint_type = endpoint_type

        self.set_region(region, zone)

        self.default_tenant = None
        self.tenants_info_manager = TenantInfoManager()

        self.keypairs = keypairs.KeypairManager(self)
        self.zones = zones.ZoneManager(self)
        self.hosts = hosts.HostManager(self)
        self.vpcs = vpcs.VpcManager(self)
        self.wires = wires.WireManager(self)
        self.storages = storages.StorageManager(self)

        self.hostwires = hostwires.HostwireManager(self)
        self.hoststorages = hoststorages.HoststorageManager(self)
        self.cachedimages = cachedimages.CachedimageManager(self)

        self.networks = networks.NetworkManager(self)
        self.disks = disks.DiskManager(self)

        self.flavors = flavors.FlavorManager(self)

        self.guests = guests.GuestManager(self)

        self.guestnetworks = guestnetworks.GuestnetworkManager(self)
        self.groupnetworks = groupnetworks.GroupnetworkManager(self)
        self.guestdisks = guestdisks.GuestdiskManager(self)

        self.groupguests = groupguests.GroupguestManager(self)

        self.usages = usages.UsageManager(self)

        self.images = images.ImageManager(self)

        self.vncproxy = vncproxy.VNCProxyManager(self)

        self.sshrelay = sshrelay.SSHRelayManager(self)

        self.logs = logs.LogManager(self)

        self.quotas = quotas.QuotaManager(self)

        self.scheduler = scheduler.SchedulerManager(self)

        self.users = users.UserManager(self)
        self.tenants = tenants.TenantManager(self)
        self.projects = projects.ProjectManager(self)
        self.domains = domains.DomainManager(self)
        self.groups = groups.GroupManager(self)
        self.roles = roles.RoleManager(self)
        self.groupusers = groupusers.GroupuserManager(self)

        self.ec2credentials = ec2credentials.EC2CredentialManager(self)
        self.services = services.ServiceManager(self)
        self.endpoints = endpoints.EndpointManager(self)

        self.secgroups = secgroups.SecuritygroupManager(self)

        self.dns = dnsrecords.DNSRecordManager(self)

        self.baremetalagents = baremetalagents.BaremetalAgentManager(self)
        self.baremetals = baremetals.BaremetalManager(self)
        self.baremetalnetworks = baremetalnetworks.BaremetalnetworkManager(self)
        self.baremetalstorages = baremetalstorages.BaremetalstorageManager(self)

        self.reservedips = reservedips.ReservedIPManager(self)

        self.schedtags = schedtags.SchedtagManager(self)
        self.schedtag_hosts = schedtags.SchedtagHostManager(self)

        self.region_stats = RegionStatsManager(self)
        self.metadatas = metadatas.MetadataManager(self)
        self.loadbalancers = loadbalancers.LoadbalancerManager(self)
        self.loadbalancerlisteners = loadbalancers.LoadbalancerListenerManager(self)
        self.loadbalancerlistenerrules = loadbalancers.LoadbalancerListenerRuleManager(self)
        self.loadbalancercertificates = loadbalancers.LoadbalancerCertificateManager(self)
        self.loadbalancerbackendgroups = loadbalancers.LoadbalancerBackendGroupManager(self)
        self.loadbalancerbackends = loadbalancers.LoadbalancerBackendManager(self)
        self.loadbalanceracls = loadbalancers.LoadbalancerAclManager(self)

        self.loadbalancerclusters = loadbalancers.LoadbalancerClusterManager(self)
        self.loadbalanceragents = loadbalancers.LoadbalancerAgentManager(self)

        self.dbinstances = dbinstances.DbinstanceManager(self)
        self.elasticcaches = elasticcaches.ElasticcacheManager(self)

        self.price_infos = price_infos.PriceInfoManager(self)

        self.dnszones = dnszones.DnsZoneManager(self)
        self.dnsrecordsets = dnsrecordsets.DnsRecordsetManager(self)

        self.actionlogs = actionlogs.ActionManager(self)

        self.file_systems = filesystems.FilesystemManager(self)
        self.buckets = buckets.BucketManager(self)
        self.natgateways = natgateways.NatgatewayManager(self)
        self.cloudaccounts = cloudaccounts.CloudaccountManager(self)
        self.cloudproviders = cloudproviders.CloudproviderManager(self)

    def set_region(self, region, zone=None):
        self.region = region
        self.zone = zone

    def _authenticatev3(self, project_name=None, project_id=None):
        logging.info('authenticate %s %s' % (project_name, project_id))
        auth = {}
        user = {'name': self.username, 'password': self.password}
        if self.domain_name:
            user['domain'] = {'name': self.domain_name}
        else:
            user['domain'] = {'id': 'default'}
        auth['identity'] = {'methods': ['password'],
                            'password': {'user': user}}
        project = {}
        if project_name:
            project['name'] = project_name
            project['domain'] = {'id': 'default'}
        if project_id:
            project['id'] = project_id
        auth['scope'] = {'project': project}
        body = {'auth': auth}
        resp, body = self._json_request(self.auth_url, None,
                                            'POST', '/auth/tokens', body=body)
        if 'token' in body:
            token_id = resp['x-subject-token']
            if 'project' in body['token']:
                self.default_tenant = TenantInfo(None, None)
                token = {'id': token_id,
                        'tenant': body['token']['project'],
                        'expires': body['token']['expires_at']}
                catalog = body['token']['catalog']
                user = body['token']['user']
                self.default_tenant.set_access_info(token, catalog, user)
                self.tenants_info_manager.add_tenant(self.default_tenant)
            else:
                self._fetch_tenants(token_id)
            return True
        else:
            raise Exception('Wrong return format %s' % json.dumps(body))

    def _authenticate(self, tenant_name=None, tenant_id=None):
        logging.info('authenticate %s %s' % (tenant_name, tenant_id))
        auth = {}
        auth['passwordCredentials'] = {'username': self.username,
                                        'password': self.password}
        if tenant_id is not None and len(tenant_id) > 0:
            auth['tenantId'] = tenant_id
        elif tenant_name is not None and len(tenant_name) > 0:
            auth['tenantName'] = tenant_name
        body = {'auth': auth}
        resp, body = self._json_request(self.auth_url, None,
                                            'POST', '/tokens', body=body)
        # print json.dumps(body, indent=4)
        if 'access' in body:
            token = body['access']['token']
            catalog = body['access']['serviceCatalog']
            user = body['access']['user']
            if 'tenant' in token:
                self.default_tenant = TenantInfo(None, None)
                # print 'Token:', token
                self.default_tenant.set_access_info(token, catalog, user)
                self.tenants_info_manager.add_tenant(self.default_tenant)
            else:
                self._fetch_tenants(token['id'])
            return True
        else:
            raise Exception('Wrong return format %s' % json.dumps(body))
        return False

    def _fetch_tenants(self, token):
        try:
            resp, body = self._json_request(self.auth_url, token,
                                            'GET', '/tenants')
            if 'tenants' in body:
                for t in body['tenants']:
                    self.tenants_info_manager.add_tenant(TenantInfo(t['id'],
                                                                    t['name']))
            return True
        except Exception as e:
            raise Exception('_fetch_tenants %s' % e)
        return False

    def get_tenants(self):
        self._authenticate(None, None)
        return self.tenants_info_manager.get_tenants()

    def set_project(self, project_name=None, project_id=None):
        return self.set_tenant(tenant_name=project_name, tenant_id=project_id)

    def set_tenant(self, tenant_name=None, tenant_id=None):
        tenant = self.tenants_info_manager.get_tenant(tenant_id=tenant_id,
                                                        tenant_name=tenant_name)
        if tenant is None:
            return self._authenticatev3(project_name=tenant_name,
                                            project_id=tenant_id)
        else:
            self.default_tenant = tenant
            return True

    def get_default_tenant(self):
        if self.default_tenant is None:
            raise Exception('No tenant specified')
        # if self.default_tenant.expire_soon():
        #    self._authenticate(tenant_name=self.default_tenant.get_name(),
        #                        tenant_id=self.default_tenant.get_id())
        return self.default_tenant

    def get_regions(self):
        t = self.get_default_tenant()
        if t is not None:
            return t.get_regions()
        else:
            return None

    def get_endpoint(self, service, admin_api=False, region=None, zone=None):
        t = self.get_default_tenant()
        if t is not None:
            if admin_api:
                ep_type = 'adminURL'
            else:
                ep_type = self.endpoint_type
            if region is None:
                region = self.region
            if zone is None:
                zone = self.zone
            return t.get_endpoint(region, service, ep_type, zone=zone)
        else:
            raise Exception('No tenant specified')

    def _wrapped_request(self, func, service, admin_api, method, url, **kwargs):
        t = self.get_default_tenant()
        if t is not None:
            ep = self.get_endpoint(service, admin_api)
            if ep is not None:
                ep = self._strip_version(ep)
                return func(ep, t.get_token(), method, url, **kwargs)
            else:
                raise Exception('NO valid endpoint found for %s' % service)
        else:
            raise Exception('No tenant specified')

    def json_request(self, service, admin_api, method, url, **kwargs):
        return self._wrapped_request(self._json_request, service, admin_api,
                                                        method, url, **kwargs)

    def raw_request(self, service, admin_api, method, url, **kwargs):
        return self._wrapped_request(self._raw_request, service, admin_api,
                                                        method, url, **kwargs)

    def get_urllib2_raw_request(self, service, admin_api, url, **kwargs):
        return self._wrapped_request(self._get_urllib2_raw_request, service,
                                                admin_api, 'GET', url, **kwargs)

    def from_file(self, filename):
        with open(filename, 'r') as f:
            desc = f.read()
            self.from_json(json.loads(desc))

    def from_json(self, desc):
        self.auth_url = desc['auth_url']
        self.username = desc['username']
        self.endpoint_type = desc['endpoint_type']
        self.set_region(desc['region'], desc.get('zone', None))
        self.tenants_info_manager = TenantInfoManager()
        self.tenants_info_manager.from_json(desc['tenants'])
        if 'default_tenant_id' in desc:
            self.set_tenant(tenant_id=desc['default_tenant_id'])

    def to_file(self, filename):
        with open(filename, 'w') as f:
            desc = self.to_json()
            f.write(json.dumps(desc))

    def to_json(self):
        desc = {}
        desc['tenants'] = self.tenants_info_manager.to_json()
        desc['username'] = self.username
        desc['auth_url'] = self.auth_url
        desc['region'] = self.region
        if self.zone:
            desc['zone'] = self.zone
        desc['endpoint_type'] = self.endpoint_type
        if self.default_tenant is not None:
            desc['default_tenant_id'] = self.default_tenant.get_id()
        return desc

    def is_admin(self):
        tenant = self.get_default_tenant()
        if tenant is not None:
            return tenant.is_admin()
        return False

    def is_system_admin(self):
        tenant = self.get_default_tenant()
        if tenant is not None:
            return tenant.is_system_admin()
        return False

