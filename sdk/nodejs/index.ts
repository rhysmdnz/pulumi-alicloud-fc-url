// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { GetTriggerUrlArgs, GetTriggerUrlResult, GetTriggerUrlOutputArgs } from "./getTriggerUrl";
export const getTriggerUrl: typeof import("./getTriggerUrl").getTriggerUrl = null as any;
export const getTriggerUrlOutput: typeof import("./getTriggerUrl").getTriggerUrlOutput = null as any;
utilities.lazyLoad(exports, ["getTriggerUrl","getTriggerUrlOutput"], () => require("./getTriggerUrl"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export sub-modules:
import * as config from "./config";

export {
    config,
};
pulumi.runtime.registerResourcePackage("alicloud-fc-url", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:alicloud-fc-url") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
