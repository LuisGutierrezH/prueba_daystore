/* @odoo-module */

import { Thread } from "@mail/core/common/thread_model";

import { patch } from "@web/core/utils/patch";

patch(Thread.prototype, {

    get typesAllowingCalls() {
        return super.typesAllowingCalls.concat(["social_chat"]);
    },

    get isChatChannel() {
        return this.type === "social_chat" || super.isChatChannel;
    },
});
