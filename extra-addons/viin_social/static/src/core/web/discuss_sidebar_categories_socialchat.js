/* @odoo-module */

import { discussSidebarCategoriesRegistry } from "@mail/discuss/core/web/discuss_sidebar_categories";

discussSidebarCategoriesRegistry.add(
    "socialchats",
    { value: (store) => store.discuss.social_chat },
    { sequence: 10 }
);
