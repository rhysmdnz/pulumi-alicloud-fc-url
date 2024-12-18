# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'GetTriggerUrlResult',
    'AwaitableGetTriggerUrlResult',
    'get_trigger_url',
    'get_trigger_url_output',
]

@pulumi.output_type
class GetTriggerUrlResult:
    """
    A collection of values returned by getTriggerUrl.
    """
    def __init__(__self__, config=None, creation_time=None, function_name=None, id=None, invocation_role=None, last_modification_time=None, service_name=None, source_arn=None, trigger_name=None, type=None, url_internet=None, url_intranet=None):
        if config and not isinstance(config, str):
            raise TypeError("Expected argument 'config' to be a str")
        pulumi.set(__self__, "config", config)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if function_name and not isinstance(function_name, str):
            raise TypeError("Expected argument 'function_name' to be a str")
        pulumi.set(__self__, "function_name", function_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invocation_role and not isinstance(invocation_role, str):
            raise TypeError("Expected argument 'invocation_role' to be a str")
        pulumi.set(__self__, "invocation_role", invocation_role)
        if last_modification_time and not isinstance(last_modification_time, str):
            raise TypeError("Expected argument 'last_modification_time' to be a str")
        pulumi.set(__self__, "last_modification_time", last_modification_time)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if source_arn and not isinstance(source_arn, str):
            raise TypeError("Expected argument 'source_arn' to be a str")
        pulumi.set(__self__, "source_arn", source_arn)
        if trigger_name and not isinstance(trigger_name, str):
            raise TypeError("Expected argument 'trigger_name' to be a str")
        pulumi.set(__self__, "trigger_name", trigger_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if url_internet and not isinstance(url_internet, str):
            raise TypeError("Expected argument 'url_internet' to be a str")
        pulumi.set(__self__, "url_internet", url_internet)
        if url_intranet and not isinstance(url_intranet, str):
            raise TypeError("Expected argument 'url_intranet' to be a str")
        pulumi.set(__self__, "url_intranet", url_intranet)

    @property
    @pulumi.getter
    def config(self) -> str:
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> str:
        """
        Example identifier
        """
        return pulumi.get(self, "function_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="invocationRole")
    def invocation_role(self) -> str:
        return pulumi.get(self, "invocation_role")

    @property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> str:
        return pulumi.get(self, "last_modification_time")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Example configurable attribute
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> str:
        return pulumi.get(self, "source_arn")

    @property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> str:
        """
        Example identifier
        """
        return pulumi.get(self, "trigger_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="urlInternet")
    def url_internet(self) -> str:
        return pulumi.get(self, "url_internet")

    @property
    @pulumi.getter(name="urlIntranet")
    def url_intranet(self) -> str:
        return pulumi.get(self, "url_intranet")


class AwaitableGetTriggerUrlResult(GetTriggerUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTriggerUrlResult(
            config=self.config,
            creation_time=self.creation_time,
            function_name=self.function_name,
            id=self.id,
            invocation_role=self.invocation_role,
            last_modification_time=self.last_modification_time,
            service_name=self.service_name,
            source_arn=self.source_arn,
            trigger_name=self.trigger_name,
            type=self.type,
            url_internet=self.url_internet,
            url_intranet=self.url_intranet)


def get_trigger_url(function_name: Optional[str] = None,
                    service_name: Optional[str] = None,
                    trigger_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTriggerUrlResult:
    """
    Example data source


    :param str function_name: Example identifier
    :param str service_name: Example configurable attribute
    :param str trigger_name: Example identifier
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['serviceName'] = service_name
    __args__['triggerName'] = trigger_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud-fc-url:index/getTriggerUrl:getTriggerUrl', __args__, opts=opts, typ=GetTriggerUrlResult).value

    return AwaitableGetTriggerUrlResult(
        config=pulumi.get(__ret__, 'config'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        function_name=pulumi.get(__ret__, 'function_name'),
        id=pulumi.get(__ret__, 'id'),
        invocation_role=pulumi.get(__ret__, 'invocation_role'),
        last_modification_time=pulumi.get(__ret__, 'last_modification_time'),
        service_name=pulumi.get(__ret__, 'service_name'),
        source_arn=pulumi.get(__ret__, 'source_arn'),
        trigger_name=pulumi.get(__ret__, 'trigger_name'),
        type=pulumi.get(__ret__, 'type'),
        url_internet=pulumi.get(__ret__, 'url_internet'),
        url_intranet=pulumi.get(__ret__, 'url_intranet'))
def get_trigger_url_output(function_name: Optional[pulumi.Input[str]] = None,
                           service_name: Optional[pulumi.Input[str]] = None,
                           trigger_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTriggerUrlResult]:
    """
    Example data source


    :param str function_name: Example identifier
    :param str service_name: Example configurable attribute
    :param str trigger_name: Example identifier
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['serviceName'] = service_name
    __args__['triggerName'] = trigger_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('alicloud-fc-url:index/getTriggerUrl:getTriggerUrl', __args__, opts=opts, typ=GetTriggerUrlResult)
    return __ret__.apply(lambda __response__: GetTriggerUrlResult(
        config=pulumi.get(__response__, 'config'),
        creation_time=pulumi.get(__response__, 'creation_time'),
        function_name=pulumi.get(__response__, 'function_name'),
        id=pulumi.get(__response__, 'id'),
        invocation_role=pulumi.get(__response__, 'invocation_role'),
        last_modification_time=pulumi.get(__response__, 'last_modification_time'),
        service_name=pulumi.get(__response__, 'service_name'),
        source_arn=pulumi.get(__response__, 'source_arn'),
        trigger_name=pulumi.get(__response__, 'trigger_name'),
        type=pulumi.get(__response__, 'type'),
        url_internet=pulumi.get(__response__, 'url_internet'),
        url_intranet=pulumi.get(__response__, 'url_intranet')))
