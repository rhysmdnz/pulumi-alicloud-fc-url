// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AlicloudFcUrl
{
    public static class GetTriggerUrl
    {
        /// <summary>
        /// Example data source
        /// </summary>
        public static Task<GetTriggerUrlResult> InvokeAsync(GetTriggerUrlArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTriggerUrlResult>("alicloud-fc-url:index/getTriggerUrl:getTriggerUrl", args ?? new GetTriggerUrlArgs(), options.WithDefaults());

        /// <summary>
        /// Example data source
        /// </summary>
        public static Output<GetTriggerUrlResult> Invoke(GetTriggerUrlInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTriggerUrlResult>("alicloud-fc-url:index/getTriggerUrl:getTriggerUrl", args ?? new GetTriggerUrlInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTriggerUrlArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Example identifier
        /// </summary>
        [Input("functionName", required: true)]
        public string FunctionName { get; set; } = null!;

        /// <summary>
        /// Example configurable attribute
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        /// <summary>
        /// Example identifier
        /// </summary>
        [Input("triggerName", required: true)]
        public string TriggerName { get; set; } = null!;

        public GetTriggerUrlArgs()
        {
        }
        public static new GetTriggerUrlArgs Empty => new GetTriggerUrlArgs();
    }

    public sealed class GetTriggerUrlInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Example identifier
        /// </summary>
        [Input("functionName", required: true)]
        public Input<string> FunctionName { get; set; } = null!;

        /// <summary>
        /// Example configurable attribute
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// Example identifier
        /// </summary>
        [Input("triggerName", required: true)]
        public Input<string> TriggerName { get; set; } = null!;

        public GetTriggerUrlInvokeArgs()
        {
        }
        public static new GetTriggerUrlInvokeArgs Empty => new GetTriggerUrlInvokeArgs();
    }


    [OutputType]
    public sealed class GetTriggerUrlResult
    {
        public readonly string Config;
        public readonly string CreationTime;
        /// <summary>
        /// Example identifier
        /// </summary>
        public readonly string FunctionName;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        public readonly string InvocationRole;
        public readonly string LastModificationTime;
        /// <summary>
        /// Example configurable attribute
        /// </summary>
        public readonly string ServiceName;
        public readonly string SourceArn;
        /// <summary>
        /// Example identifier
        /// </summary>
        public readonly string TriggerName;
        public readonly string Type;
        public readonly string UrlInternet;
        public readonly string UrlIntranet;

        [OutputConstructor]
        private GetTriggerUrlResult(
            string config,

            string creationTime,

            string functionName,

            string id,

            string invocationRole,

            string lastModificationTime,

            string serviceName,

            string sourceArn,

            string triggerName,

            string type,

            string urlInternet,

            string urlIntranet)
        {
            Config = config;
            CreationTime = creationTime;
            FunctionName = functionName;
            Id = id;
            InvocationRole = invocationRole;
            LastModificationTime = lastModificationTime;
            ServiceName = serviceName;
            SourceArn = sourceArn;
            TriggerName = triggerName;
            Type = type;
            UrlInternet = urlInternet;
            UrlIntranet = urlIntranet;
        }
    }
}