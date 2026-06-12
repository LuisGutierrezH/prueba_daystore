/* @odoo-module */

import { Thread } from "@mail/core/common/thread_model";
import { assignIn, assignDefined } from "@mail/utils/common/misc";
import { url } from "@web/core/utils/urls";
import { patch } from "@web/core/utils/patch";

patch(Thread, {
    _insert(data) {
        const thread = super._insert(...arguments);
        if (thread.type === "social_chat") {
            assignIn(thread, data, ["anonymous_name", "anonymous_country"]);
            this.store.discuss.social_chat.threads.add(thread);
        }
        return thread;
    },
});

patch(Thread.prototype, {
    get hasMemberList() {
        return this.type === "social_chat" || super.hasMemberList;
    },

    get imgUrl() {
        let imgUrl = super.imgUrl
        if (this.type == "social_chat") {
            return url(
                `/discuss/channel/${this.id}/avatar_128`,
                assignDefined({}, { unique: this.avatarCacheKey })
            );
        }
        return imgUrl
    },
});
