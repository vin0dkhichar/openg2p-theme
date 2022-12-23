/** @odoo-module **/

import {WebClient} from "@web/webclient/webclient";
import {patch} from "@web/core/utils/patch";

patch(WebClient.prototype, "OpenG2P Window Title", {
    setup() {
        this._super();
        this.title.setParts({zopenerp: "OpenG2P"});
    },
});
