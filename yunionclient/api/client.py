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
import hashlib
import hmac
from datetime import datetime, timezone
from requests import Request, Session
from urllib.parse import quote
from urllib3.util import parse_url
try:
    # python 2
    from urllib import quote
    from urlparse import urlparse
except ImportError:
    # python 3
    from urllib.parse import quote, urlparse

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
from yunionclient.api import secgroupcaches

from yunionclient.api import dnsrecords

from yunionclient.api import baremetalagents
from yunionclient.api import baremetals
from yunionclient.api import baremetalnetworks
from yunionclient.api import baremetalstorages

from yunionclient.api import reservedips

from yunionclient.api import scheduler

from yunionclient.api.stats import RegionStatsManager

from yunionclient.api import price_infos
from yunionclient.api import prices

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
from yunionclient.api import dbinstancenetworks
from yunionclient.api import elasticcaches

from yunionclient.api import dnszones
from yunionclient.api import dnsrecordsets

from yunionclient.api import actionlogs

from yunionclient.api import filesystems
from yunionclient.api import buckets
from yunionclient.api import natgateways
from yunionclient.api import cloudaccounts
from yunionclient.api import cloudproviders
from yunionclient.api import dnszonecaches
from yunionclient.api import eips
from yunionclient.api import serverskus
from yunionclient.api import dbinstancesku
from yunionclient.api import mongodbs
from yunionclient.api import cdndomains
from yunionclient.api import accessgroupcaches
from yunionclient.api import accessgrouprules
from yunionclient.api import accessgroups
from yunionclient.api import apps
from yunionclient.api import capabilities
from yunionclient.api import cloudregions
from yunionclient.api import nasskus

from yunionclient.api import kafkas
from yunionclient.api import elasticsearchs
from yunionclient.api import mounttargets

from yunionclient.api import alertnotifications
from yunionclient.api import alertdashboards
from yunionclient.api import alertpanels
from yunionclient.api import alertrecords
from yunionclient.api import alertrecordshields
from yunionclient.api import alertresources
from yunionclient.api import alerts
from yunionclient.api import appfromfiles
from yunionclient.api import baremetalevents
from yunionclient.api import cachedloadbalanceracls
from yunionclient.api import cachedloadbalancercertificates
from yunionclient.api import charts
from yunionclient.api import cloudkubeclusters
from yunionclient.api import cloudkubenodepools
from yunionclient.api import cloudkubenodes
from yunionclient.api import cloudevents
from yunionclient.api import cloudgroupcaches
from yunionclient.api import cloudgroups
from yunionclient.api import cloudpermissions
from yunionclient.api import cloudpolicies
from yunionclient.api import cloudpolicycaches
from yunionclient.api import cloudproviderquotas
from yunionclient.api import cloudroles
from yunionclient.api import cloudusers
from yunionclient.api import commonalerts
from yunionclient.api import configmaps
from yunionclient.api import contacts
from yunionclient.api import cronjobs
from yunionclient.api import daemonsets
from yunionclient.api import datasources
from yunionclient.api import dbinstanceskus
from yunionclient.api import dbinstanceaccounts
from yunionclient.api import dbinstancebackups
from yunionclient.api import dbinstancedatabases
from yunionclient.api import dbinstanceparameters
from yunionclient.api import dbinstanceprivileges
from yunionclient.api import deployments
from yunionclient.api import devtoolcronjobs
from yunionclient.api import devtooltemplates
from yunionclient.api import dnstrafficpolicies
from yunionclient.api import domainquotas
from yunionclient.api import elasticcacheaccounts
from yunionclient.api import elasticcacheacls
from yunionclient.api import elasticcachebackups
from yunionclient.api import elasticcacheparameters
from yunionclient.api import elasticcacheskus
from yunionclient.api import emailconfigs
from yunionclient.api import events
from yunionclient.api import federatedclusterrolebindings
from yunionclient.api import federatedclusterroles
from yunionclient.api import federatednamespaces
from yunionclient.api import federatedrolebindings
from yunionclient.api import federatedroles
from yunionclient.api import globalvpcs
from yunionclient.api import guestimages
from yunionclient.api import identityproviders
from yunionclient.api import infrasquotas
from yunionclient.api import ingresses
from yunionclient.api import instancesnapshots
from yunionclient.api import instancegroups
from yunionclient.api import intervpcnetworkroutesets
from yunionclient.api import intervpcnetworks
from yunionclient.api import isolateddevices
from yunionclient.api import jobs
from yunionclient.api import k8sevents
from yunionclient.api import k8snodes
from yunionclient.api import k8sservices
from yunionclient.api import kubeclusters
from yunionclient.api import kubemachines
from yunionclient.api import loadbalanceracls
from yunionclient.api import loadbalanceragents
from yunionclient.api import loadbalancerbackendgroups
from yunionclient.api import loadbalancerbackends
from yunionclient.api import loadbalancercertificates
from yunionclient.api import loadbalancerclusters
from yunionclient.api import loadbalancerlistenerrules
from yunionclient.api import loadbalancerlisteners
from yunionclient.api import meteralerts
from yunionclient.api import metricfields
from yunionclient.api import metricmeasurements
from yunionclient.api import monitorresources
from yunionclient.api import namespaces
from yunionclient.api import natskus
from yunionclient.api import natdentries
from yunionclient.api import natsentries
from yunionclient.api import networkaddresses
from yunionclient.api import networkinterfaces
from yunionclient.api import nodealerts
from yunionclient.api import notifications
from yunionclient.api import notifyconfigs
from yunionclient.api import notifytemplates
from yunionclient.api import parameters
from yunionclient.api import persistentvolumeclaims
from yunionclient.api import persistentvolumes
from yunionclient.api import pods
from yunionclient.api import policies
from yunionclient.api import policyassignments
from yunionclient.api import policydefinitions
from yunionclient.api import projectmappings
from yunionclient.api import projectquotas
from yunionclient.api import proxysettings
from yunionclient.api import rbacclusterrolebindings
from yunionclient.api import rbacclusterroles
from yunionclient.api import rbacrolebindings
from yunionclient.api import rbacroles
from yunionclient.api import receivers
from yunionclient.api import regionquotas
from yunionclient.api import regions
from yunionclient.api import releases
from yunionclient.api import repos
from yunionclient.api import robots
from yunionclient.api import roleassignments
from yunionclient.api import rolepolicies
from yunionclient.api import routetableassociations
from yunionclient.api import routetableroutesets
from yunionclient.api import routetables
from yunionclient.api import samlproviders
from yunionclient.api import samlusers
from yunionclient.api import scalingactivities
from yunionclient.api import scalinggroups
from yunionclient.api import scalingpolicies
from yunionclient.api import scheduledtaskactivities
from yunionclient.api import scheduledtasks
from yunionclient.api import schedulers
from yunionclient.api import scopedpolicies
from yunionclient.api import scopedpolicybindings
from yunionclient.api import scriptapplyrecords
from yunionclient.api import scripts
from yunionclient.api import secgrouprules
from yunionclient.api import secrets
from yunionclient.api import servertemplates
from yunionclient.api import serviceaccounts
from yunionclient.api import servicecatalogs
from yunionclient.api import servicecertificates
from yunionclient.api import serviceurls
from yunionclient.api import smsconfigs
from yunionclient.api import snapshotpolicies
from yunionclient.api import snapshotpolicycaches
from yunionclient.api import snapshots
from yunionclient.api import specs
from yunionclient.api import sshinfos
from yunionclient.api import statefulsets
from yunionclient.api import storagecaches
from yunionclient.api import storageclasses
from yunionclient.api import subscribers
from yunionclient.api import tasks
from yunionclient.api import tiller
from yunionclient.api import topics
from yunionclient.api import unifiedmonitors
from yunionclient.api import vcenters
from yunionclient.api import verifications
from yunionclient.api import vpcpeeringconnections
from yunionclient.api import wafinstances
from yunionclient.api import wafipsetcaches
from yunionclient.api import wafipsets
from yunionclient.api import wafregexsetcaches
from yunionclient.api import wafregexsets
from yunionclient.api import wafrulegroups
from yunionclient.api import wafrules
from yunionclient.api import webappenvironments
from yunionclient.api import webapps
from yunionclient.api import webconsole
from yunionclient.api import workerstats
from yunionclient.api import x509keypairs
from yunionclient.api import zonequotas


logger = logging.getLogger(__name__)


class Client(http.HTTPClient):
    """Client for Yunion Cloud API
    """

    def __init__(self, auth_url, username=None, password=None, domain_name=None,
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
        self.secgroupcaches = secgroupcaches.SecgroupCacheManager(self)

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
        self.dbinstancenetworks = dbinstancenetworks.DBInstancenetworkManager(self)
        self.elasticcaches = elasticcaches.ElasticcacheManager(self)

        self.price_infos = price_infos.PriceInfoManager(self)
        self.prices = prices.PriceManager(self)
        self.price_metadatas = prices.PriceMetadataManager(self)

        self.dnszones = dnszones.DnsZoneManager(self)
        self.dnsrecordsets = dnsrecordsets.DnsRecordsetManager(self)

        self.actionlogs = actionlogs.ActionManager(self)

        self.file_systems = filesystems.FilesystemManager(self)
        self.buckets = buckets.BucketManager(self)
        self.natgateways = natgateways.NatgatewayManager(self)
        self.cloudaccounts = cloudaccounts.CloudaccountManager(self)
        self.cloudproviders = cloudproviders.CloudproviderManager(self)
        self.dnszonecaches = dnszonecaches.DnsZoneCacheManager(self)
        self.eips = eips.EIPManager(self)
        self.serverskus = serverskus.ServerSkuManager(self)
        self.dbinstance_skus = dbinstancesku.DbinstanceSkuManager(self)
        self.mongodbs = mongodbs.MongoDBManager(self)
        self.cdndomains = cdndomains.CdnDomainManager(self)
        self.accessgroupcaches = accessgroupcaches.AccessGroupCacheManager(self)
        self.accessgrouprules = accessgrouprules.AccessGroupRuleManager(self)
        self.accessgroups = accessgroups.AccessGroupManager(self)
        self.apps = apps.AppManager(self)
        self.capabilities = capabilities.CapabilityManager(self)
        self.cloudregions = cloudregions.CloudregionManager(self)

        self.nasskus = nasskus.NasSkuManager(self)
        self.kafkas = kafkas.KafkaManager(self)
        self.elasticsearchs = elasticsearchs.ElasticSearchManager(self)
        self.mounttargets = mounttargets.MountTargetManager(self)

        self.alertnotifications = alertnotifications.AlertNotificationManager(self)
        self.alertdashboards = alertdashboards.AlertdashboardManager(self)
        self.alertpanels = alertpanels.AlertpanelManager(self)
        self.alertrecords = alertrecords.AlertrecordManager(self)
        self.alertrecordshields = alertrecordshields.AlertrecordshieldManager(self)
        self.alertresources = alertresources.AlertresourceManager(self)
        self.alerts = alerts.AlertManager(self)
        self.appfromfiles = appfromfiles.AppfromfileManager(self)
        self.baremetalevents = baremetalevents.BaremetaleventManager(self)
        self.cachedloadbalanceracls = cachedloadbalanceracls.CachedloadbalanceraclManager(self)
        self.cachedloadbalancercertificates = cachedloadbalancercertificates.CachedloadbalancercertificateManager(self)
        self.charts = charts.ChartManager(self)
        self.cloudkubeclusters = cloudkubeclusters.CloudKubeClusterManager(self)
        self.cloudkubenodepools = cloudkubenodepools.CloudKubeNodePoolManager(self)
        self.cloudkubenodes = cloudkubenodes.CloudKubeNodeManager(self)
        self.cloudevents = cloudevents.CloudeventManager(self)
        self.cloudgroupcaches = cloudgroupcaches.CloudgroupcacheManager(self)
        self.cloudgroups = cloudgroups.CloudgroupManager(self)
        self.cloudpermissions = cloudpermissions.CloudpermissionManager(self)
        self.cloudpolicies = cloudpolicies.CloudpolicyManager(self)
        self.cloudpolicycaches = cloudpolicycaches.CloudpolicycacheManager(self)
        self.cloudproviderquotas = cloudproviderquotas.CloudproviderquotaManager(self)
        self.cloudroles = cloudroles.CloudroleManager(self)
        self.cloudusers = cloudusers.ClouduserManager(self)
        self.commonalerts = commonalerts.CommonalertManager(self)
        self.configmaps = configmaps.ConfigmapManager(self)
        self.contacts = contacts.ContactManager(self)
        self.cronjobs = cronjobs.CronjobManager(self)
        self.daemonsets = daemonsets.DaemonsetManager(self)
        self.datasources = datasources.DatasourceManager(self)
        self.dbinstanceskus = dbinstanceskus.DbinstanceSkuManager(self)
        self.dbinstanceaccounts = dbinstanceaccounts.DbinstanceaccountManager(self)
        self.dbinstancebackups = dbinstancebackups.DbinstancebackupManager(self)
        self.dbinstancedatabases = dbinstancedatabases.DbinstancedatabaseManager(self)
        self.dbinstanceparameters = dbinstanceparameters.DbinstanceparameterManager(self)
        self.dbinstanceprivileges = dbinstanceprivileges.DbinstanceprivilegeManager(self)
        self.deployments = deployments.DeploymentManager(self)
        self.devtoolcronjobs = devtoolcronjobs.DevtoolCronjobManager(self)
        self.devtooltemplates = devtooltemplates.DevtoolTemplateManager(self)
        self.dnstrafficpolicies = dnstrafficpolicies.DnsTrafficpolicyManager(self)
        self.domainquotas = domainquotas.DomainQuotaManager(self)
        self.elasticcacheaccounts = elasticcacheaccounts.ElasticcacheaccountManager(self)
        self.elasticcacheacls = elasticcacheacls.ElasticcacheaclManager(self)
        self.elasticcachebackups = elasticcachebackups.ElasticcachebackupManager(self)
        self.elasticcacheparameters = elasticcacheparameters.ElasticcacheparameterManager(self)
        self.elasticcacheskus = elasticcacheskus.ElasticcacheskuManager(self)
        self.emailconfigs = emailconfigs.EmailConfigManager(self)
        self.events = events.EventManager(self)
        self.federatedclusterrolebindings = federatedclusterrolebindings.FederatedclusterrolebindingManager(self)
        self.federatedclusterroles = federatedclusterroles.FederatedclusterroleManager(self)
        self.federatednamespaces = federatednamespaces.FederatednamespaceManager(self)
        self.federatedrolebindings = federatedrolebindings.FederatedrolebindingManager(self)
        self.federatedroles = federatedroles.FederatedroleManager(self)
        self.globalvpcs = globalvpcs.GlobalvpcManager(self)
        self.guestimages = guestimages.GuestimageManager(self)
        self.identityproviders = identityproviders.IdentityProviderManager(self)
        self.infrasquotas = infrasquotas.InfrasQuotaManager(self)
        self.ingresses = ingresses.IngressManager(self)
        self.instancesnapshots = instancesnapshots.InstanceSnapshotManager(self)
        self.instancegroups = instancegroups.InstancegroupManager(self)
        self.intervpcnetworkroutesets = intervpcnetworkroutesets.InterVpcNetworkRouteSetManager(self)
        self.intervpcnetworks = intervpcnetworks.InterVpcNetworkManager(self)
        self.isolateddevices = isolateddevices.IsolatedDeviceManager(self)
        self.jobs = jobs.JobManager(self)
        self.k8sevents = k8sevents.K8sEventManager(self)
        self.k8snodes = k8snodes.K8sNodeManager(self)
        self.k8sservices = k8sservices.K8sServiceManager(self)
        self.kubeclusters = kubeclusters.KubeclusterManager(self)
        self.kubemachines = kubemachines.KubemachineManager(self)
        self.loadbalanceracls = loadbalanceracls.LoadbalanceraclManager(self)
        self.loadbalanceragents = loadbalanceragents.LoadbalanceragentManager(self)
        self.loadbalancerbackendgroups = loadbalancerbackendgroups.LoadbalancerbackendgroupManager(self)
        self.loadbalancerbackends = loadbalancerbackends.LoadbalancerbackendManager(self)
        self.loadbalancercertificates = loadbalancercertificates.LoadbalancercertificateManager(self)
        self.loadbalancerclusters = loadbalancerclusters.LoadbalancerclusterManager(self)
        self.loadbalancerlistenerrules = loadbalancerlistenerrules.LoadbalancerlistenerruleManager(self)
        self.loadbalancerlisteners = loadbalancerlisteners.LoadbalancerlistenerManager(self)
        self.meteralerts = meteralerts.MeteralertManager(self)
        self.metricfields = metricfields.MetricfieldManager(self)
        self.metricmeasurements = metricmeasurements.MetricmeasurementManager(self)
        self.monitorresources = monitorresources.MonitorresourceManager(self)
        self.namespaces = namespaces.NamespaceManager(self)
        self.natskus = natskus.NatSkuManager(self)
        self.natdentries = natdentries.NatdentryManager(self)
        self.natsentries = natsentries.NatsentryManager(self)
        self.networkaddresses = networkaddresses.NetworkaddressManager(self)
        self.networkinterfaces = networkinterfaces.NetworkinterfaceManager(self)
        self.nodealerts = nodealerts.NodealertManager(self)
        self.notifications = notifications.NotificationManager(self)
        self.notifyconfigs = notifyconfigs.NotifyconfigManager(self)
        self.notifytemplates = notifytemplates.NotifytemplateManager(self)
        self.parameters = parameters.ParameterManager(self)
        self.persistentvolumeclaims = persistentvolumeclaims.PersistentvolumeclaimManager(self)
        self.persistentvolumes = persistentvolumes.PersistentvolumeManager(self)
        self.pods = pods.PodManager(self)
        self.policies = policies.PolicyManager(self)
        self.policyassignments = policyassignments.PolicyAssignmentManager(self)
        self.policydefinitions = policydefinitions.PolicyDefinitionManager(self)
        self.projectmappings = projectmappings.ProjectMappingManager(self)
        self.projectquotas = projectquotas.ProjectQuotaManager(self)
        self.proxysettings = proxysettings.ProxysettingManager(self)
        self.rbacclusterrolebindings = rbacclusterrolebindings.RbacclusterrolebindingManager(self)
        self.rbacclusterroles = rbacclusterroles.RbacclusterroleManager(self)
        self.rbacrolebindings = rbacrolebindings.RbacrolebindingManager(self)
        self.rbacroles = rbacroles.RbacroleManager(self)
        self.receivers = receivers.ReceiverManager(self)
        self.regionquotas = regionquotas.RegionQuotaManager(self)
        self.regions = regions.RegionManager(self)
        self.releases = releases.ReleaseManager(self)
        self.repos = repos.RepoManager(self)
        self.robots = robots.RobotManager(self)
        self.roleassignments = roleassignments.RoleAssignmentManager(self)
        self.rolepolicies = rolepolicies.RolepolicyManager(self)
        self.routetableassociations = routetableassociations.RouteTableAssociationManager(self)
        self.routetableroutesets = routetableroutesets.RouteTableRouteSetManager(self)
        self.routetables = routetables.RouteTableManager(self)
        self.samlproviders = samlproviders.SamlProviderManager(self)
        self.samlusers = samlusers.SamluserManager(self)
        self.scalingactivities = scalingactivities.ScalingactivityManager(self)
        self.scalinggroups = scalinggroups.ScalinggroupManager(self)
        self.scalingpolicies = scalingpolicies.ScalingpolicyManager(self)
        self.scheduledtaskactivities = scheduledtaskactivities.ScheudledtaskactivityManager(self)
        self.scheduledtasks = scheduledtasks.ScheduledtaskManager(self)
        self.schedulers = schedulers.SchedulerManager(self)
        self.scopedpolicies = scopedpolicies.ScopedpolicyManager(self)
        self.scopedpolicybindings = scopedpolicybindings.ScopedpolicybindingManager(self)
        self.scriptapplyrecords = scriptapplyrecords.ScriptapplyrecordManager(self)
        self.scripts = scripts.ScriptManager(self)
        self.secgrouprules = secgrouprules.SecgroupruleManager(self)
        self.secrets = secrets.SecretManager(self)
        self.servertemplates = servertemplates.ServertemplateManager(self)
        self.serviceaccounts = serviceaccounts.ServiceaccountManager(self)
        self.servicecatalogs = servicecatalogs.ServicecatalogManager(self)
        self.servicecertificates = servicecertificates.ServicecertificateManager(self)
        self.serviceurls = serviceurls.ServiceurlManager(self)
        self.smsconfigs = smsconfigs.SmsConfigManager(self)
        self.snapshotpolicies = snapshotpolicies.SnapshotpolicyManager(self)
        self.snapshotpolicycaches = snapshotpolicycaches.SnapshotpolicycacheManager(self)
        self.snapshots = snapshots.SnapshotManager(self)
        self.specs = specs.SpecManager(self)
        self.sshinfos = sshinfos.SshinfoManager(self)
        self.statefulsets = statefulsets.StatefulsetManager(self)
        self.storagecaches = storagecaches.StoragecacheManager(self)
        self.storageclasses = storageclasses.StorageclassManager(self)
        self.subscribers = subscribers.SubscriberManager(self)
        self.tasks = tasks.TaskManager(self)
        self.tiller = tiller.TillerManager(self)
        self.topics = topics.TopicManager(self)
        self.unifiedmonitors = unifiedmonitors.UnifiedmonitorManager(self)
        self.vcenters = vcenters.VcenterManager(self)
        self.verifications = verifications.VerificationManager(self)
        self.vpcpeeringconnections = vpcpeeringconnections.VpcPeeringConnectionManager(self)
        self.wafinstances = wafinstances.WafInstanceManager(self)
        self.wafipsetcaches = wafipsetcaches.WafIpsetCacheManager(self)
        self.wafipsets = wafipsets.WafIpsetManager(self)
        self.wafregexsetcaches = wafregexsetcaches.WafRegexsetCacheManager(self)
        self.wafregexsets = wafregexsets.WafRegexsetManager(self)
        self.wafrulegroups = wafrulegroups.WafRuleGroupManager(self)
        self.wafrules = wafrules.WafRuleManager(self)
        self.webappenvironments = webappenvironments.WebappenvironmentManager(self)
        self.webapps = webapps.WebappManager(self)
        self.webconsole = webconsole.WebconsoleManager(self)
        self.workerstats = workerstats.WorkersManager(self)
        self.x509keypairs = x509keypairs.X509keypairManager(self)
        self.zonequotas = zonequotas.ZoneQuotaManager(self)

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
    
    def get_signed_headers(self, req, _ignoreHeaders = []):
        ret = []
        hasHost = False
        hasContentHash = False
        ignoreHeaders = []
        headers = []
        for h in _ignoreHeaders:
            ignoreHeaders.append(h.lower())
        for k, v in req.headers.items():
            if k in ignoreHeaders:
                continue
            if k.lower() == 'host':
                hasHost = True
            elif k.lower() == 'x-amz-content-sha256':
                hasContentHash = True
            else:
                headers.append(k.lower())
        if not hasHost:
            headers.append('host')
        if not hasContentHash:
            headers.append('x-amz-content-sha256')

        headers.sort()
        return headers

    def get_canonical_headers(self, req, signed_headers=[]):
        ret = ''
        for h in signed_headers:
            ret += h
            ret += ':'
            if h == 'host':
                parsedurl = urlparse(req.url)
                host = parsedurl.netloc.split(':')[0]
                if len(host) > 0:
                    ret += host
                ret += '\n'
            else:
                if hasattr(req, 'headers') and hasattr(req.headers, h):
                    ret += req.headers[h]
                ret+= '\n'
        return ret

    def get_canonical_request(self, req, signed_headers=[]):
        url = quote(req.url).replace('+', '%20')
        parsedurl = urlparse(req.url)
        canonical_path = quote(parsedurl.path if parsedurl.path else '/', safe='/-_.~')

        canonical_querystring = ''
        querystring_sorted = '&'.join(sorted(parsedurl.query.split('&')))

        for query_param in querystring_sorted.split('&'):
            key_val_split = query_param.split('=', 1)

            key = key_val_split[0]
            if len(key_val_split) > 1:
                val = key_val_split[1]
            else:
                val = ''

            if key:
                if canonical_querystring:
                    canonical_querystring += "&"
                canonical_querystring += u'='.join([key, val])

        body = bytes()
        if hasattr(req, 'body'):
            body = req.body
        try:
            body = body.encode('utf-8')
        except (AttributeError, UnicodeDecodeError):
            body = body

        payload_hash = hashlib.sha256(body).hexdigest()

        canonical_headers = self.get_canonical_headers(req, signed_headers)
        ret = [req.method, canonical_path, canonical_querystring, canonical_headers, ';'.join(signed_headers), payload_hash]
        return '\n'.join(ret)

    def get_scope(self, location, t):
        return '/'.join([t.strftime('%Y%m%d'), location, 's3', 'aws4_request'])

    def sign(self, key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def get_signature_key(self, key, dateStamp, location):
        kDate = self.sign(('AWS4' + key).encode('utf-8'), dateStamp)
        kRegion = self.sign(kDate, location)
        kService = self.sign(kRegion, 's3')
        kSigning = self.sign(kService, 'aws4_request')
        return kSigning

    def sign_v4(self, req, access_key=None, access_secret=None, location=None):
        if access_key is None or access_secret is None:
            return req
        if hasattr(req, 'body'):
            sha = hashlib.sha256(req.body.encode('utf-8')).hexdigest()
            req.headers['X-Amz-Content-Sha256'] = sha
        # 20060102T150405Z
        now = datetime.now(timezone.utc)
        req.headers['X-Amz-Date'] = now.strftime('%Y%m%dT%H%M%SZ')
        # Mon, 02 Jan 2006 15:04:05 MST
        req.headers['Date'] = datetime.now(timezone.utc).strftime('%a, %m %b %Y %H:%M:%S MST')
        signed_headers = self.get_signed_headers(req, ['Authorization', 'Content-Type', 'Content-Length', 'User-Agent'])
        canonical_request = self.get_canonical_request(req, signed_headers)

        algorithm = 'AWS4-HMAC-SHA256'
        t = datetime.now(timezone.utc)
        scope = self.get_scope(location, t)
        string_to_sign = algorithm + '\n' + t.strftime('%Y%m%dT%H%M%SZ') + '\n' + scope + '\n' + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

        signing_key = self.get_signature_key(access_secret, t.strftime('%Y%m%d'), location)

        string_to_sign_utf8 = string_to_sign.encode('utf-8')

        credential = self.get_credential(access_key, location, t)

        signature = hmac.new(signing_key, string_to_sign_utf8, hashlib.sha256).hexdigest()
        authorization_header = [
                algorithm + ' ' + 'Credential=' + credential, 
                'SignedHeaders=' + ';'.join(signed_headers),
                'Signature=' + signature,
                ]
        
        req.headers['Authorization'] = ','.join(authorization_header)
        return req

    def get_credential(self, access_key, location, t):
        scope = self.get_scope(location, t)
        return access_key + '/' + scope

    def decode_access_key_request(self, req, virtual_host=False):
        auth_header = req.headers['Authorization']
        if auth_header is None or len(auth_header) == 0:
            raise Exception('missing authorization header')
        aksk_req = self.decode_auth_header(auth_header)

        aksk_req = self.parse_request(req, aksk_req, virtual_host)
        return aksk_req

    #def verify(aksk, secret):
    #    signing_key = self.get_signature_key

    def parse_request(self, req, aksk={}, virtual_host=False):
        date_str = req.headers['X-Amz-Date']
        if len(date_str) == 0:
            raise Exception('missing x-amz-date')
        date_sign = datetime.strptime(date_str, '%Y%m%dT%H%M%SZ')

        canonical_req = self.get_canonical_request(req, aksk['signed_headers'])
        aksk['sign_date'] = date_sign.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        aksk['request'] = self.get_string_to_sign_v4(date_sign, aksk['location'], canonical_req)
        return aksk

    def get_string_to_sign_v4(self, date, location, canonical_request):
        string_to_sign = 'AWS4-HMAC-SHA256' + '\n' + date.strftime('%Y%m%dT%H%M%SZ') + '\n'
        string_to_sign += self.get_scope(location, date) + '\n'
        string_to_sign += hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
        return string_to_sign

    def decode_auth_header(self, auth_header=''):
        pos = auth_header.index(' ')
        if pos <= 0:
            raise Exception('illegal authorization header')
        algo = auth_header[:pos]
        if algo == 'AWS4-HMAC-SHA256':
            return self.decode_auth_header_v4(auth_header[pos+1:])

        raise Exception('unsupported signing algorithm %s', algo)

    def decode_auth_header_v4(self, auth_str=''):
        parts = auth_str.split(',')
        if len(parts) != 3 or not (parts[0].startswith('Credential=') and parts[1].startswith('SignedHeaders=') and parts[2].startswith('Signature=')):
            raise Exception('illegal v4 auth header')
        cred_parts = parts[0][len('Credential='):].split('/')
        if len(cred_parts) != 5:
            raise Exception('illegal v4 auth header Credential')
       
        req = {}
        req['algorithm'] = 'AWS4-HMAC-SHA256'
        req['access_key'] = cred_parts[0]
        req['location'] = cred_parts[2]
        headers = parts[1][len('SignedHeaders='):].split(';')
        headers.sort()
        req['signed_headers'] = headers
        req['signature'] = parts[2][len('Signature='):]
        return req

    def authenticate_by_access_key(self, access_key=None, access_secret=None, source='cli'):
        logging.info('authenticate %s %s' % (access_key, access_secret))
        auth = {}
        aksk = {'access_key': access_key, 'location': 'cn-beijing', 'algorithm': 'AWS4-HMAC-SHA256'}
        actx = {'source': source}
        auth['context'] = actx
        auth['identity'] = {
                'access_key_secret': str(json.dumps(aksk)),
                'methods': ['aksk'],
                }
        body = {'auth': auth}
        req = Request('POST', self.auth_url+ '/auth/tokens', data=json.dumps(body), headers={})
        newReq = self.sign_v4(req, access_key, access_secret, aksk['location'])

        _aksk = self.decode_access_key_request(req, False)

        self.verify_key_secret(_aksk, actx)

    def verify_key_secret(self, aksk, actx):
        input = {
                'auth': {
                    'identity': {
                        'methods': ['aksk'],
                        'access_key_secret': str(json.dumps(aksk)),
                        },
                    'ctx': actx,
                    },
                }
        resp, body = self._json_request(self.auth_url, None,
                                            'POST', '/auth/tokens', body=input)
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

