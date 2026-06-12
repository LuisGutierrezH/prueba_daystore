/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { SocialPostCommentEmoji } from '../social_post_comment_emojis/social_post_comment_emojis';
import { Component, useState } from "@odoo/owl";

export class SocialPostComment extends Component {

    setup() {
        this.orm = useService("orm");
        this.state = useState({
            reply_comments: []
        });
        this.props.reply_comments = []
        this.notificationService = useService("notification");
    }

    async _likeComment(ev) {
        ev.preventDefault();
        var $target = $(ev.currentTarget);
        var current_comment = $target.closest('.social_comment');
        var div_like_count = current_comment.find('.comment_like_count').first();
        var social_comment_id = current_comment.attr("social_comment_id");
        this.orm.call('social.post', 'like_comment', [this.props.post_id, social_comment_id], {}).then(
            data => {
                if (data) {
                    var new_like_count = parseInt(div_like_count.text()) + parseInt(data);
                    div_like_count.text(new_like_count);
                }
            });
    }

    async _hideCommnet(ev) {
        ev.preventDefault();
        var self = this;
        var $target = $(ev.currentTarget);
        var current_comment = $target.closest('.social_comment');
        var social_comment_id = current_comment.attr("social_comment_id");

        this.orm.call('social.post', 'hide_comment', [this.props.post_id, social_comment_id], {}).then(
            data => {
                if (data.success) {
                    current_comment.css({ 'opacity': '0.5' });
                    current_comment.find('.button_like_comment').css({ 'display': 'none' });
                    current_comment.find('.button_reply_comment').css({ 'display': 'none' });
                    current_comment.find('.social_comment_action').css({ 'display': 'none' });
                    current_comment.find('.button_unhide_comment').css({ 'display': 'inline-block' });
                } else {
                    self.notificationService.add(data.msg_error, {
                        title: _t('Error'),
                        type: "danger",
                    });
                }
            });
    }

    async _unhideComment(ev) {
        ev.preventDefault();
        var self = this;
        var $target = $(ev.currentTarget);
        var current_comment = $target.closest('.social_comment');
        var social_comment_id = current_comment.attr("social_comment_id");

        this.orm.call('social.post', 'unhide_comment', [this.props.post_id, social_comment_id], {}).then(
            data => {
                if (data.success) {
                    current_comment.css({ 'opacity': '1' });
                    current_comment.find('.button_like_comment').css({ 'display': 'inline-block' });
                    current_comment.find('.button_reply_comment').css({ 'display': 'inline-block' });
                    current_comment.find('.social_comment_action').css({ 'display': 'inline-block' });
                    current_comment.find('.button_unhide_comment').css({ 'display': 'none' })
                } else {
                    self.notificationService.add(data.msg_error, {
                        title: _t('Error'),
                        type: "danger",
                    });
                }
            });
    }

    async _deleteComment(ev) {
        ev.preventDefault();
        var $target = $(ev.currentTarget);
        var current_comment = $target.closest('.social_comment');
        var social_comment_id = current_comment.attr("social_comment_id");
        var div_post_comment_count = $('.post_comment_count');
        this.orm.call('social.post', 'delete_comment', [this.props.post_id, social_comment_id], {}).then(
            data => {
                if (data) {
                    current_comment.remove();
                    var new_comment_count = parseInt(div_post_comment_count.text()) - 1;
                    if (new_comment_count > 0) {
                        div_post_comment_count.text(new_comment_count);
                    }
                }
            });
    }

    async _showReplyInput(ev) {
        ev.preventDefault();
        var $target = $(ev.currentTarget);
        var div_root_comment = $target.closest('.social_root_comment');
        var reply_content = div_root_comment.find('.social_reply_comment_input');
        var hide_div = div_root_comment.find('.d-none');
        hide_div.removeClass('d-none');
        reply_content.children("textarea").focus();
    }

    async _showReplyComment(ev) {
        ev.preventDefault();
        var $target = $(ev.currentTarget);
        $target.hide();
        this.orm.call('social.post', 'get_reply_comments', [this.props.post_id, this.props.comment.id], {}).then(
            data => {
                this.props.reply_comments = data.replys;
                this.state.reply_comments = data.replys;
            });
    }

    async _replyComment(ev) {
        if (ev.keyCode == 13 || ev.which == 13) {
            if (!ev.shiftKey) {
                ev.preventDefault();
                var $target = $(ev.currentTarget);
                var reply_message = $target.val()
                if (reply_message == '') {
                    return;
                }
                $target.val('')
                this.orm.call('social.post', 'add_comment', [this.props.post_id, reply_message, this.props.comment.id], {}).then(
                    data => {
                        if (data) {
                            var old_comments = this.state.reply_comments;
                            var new_comments = old_comments.concat(data.replys);
                            this.state.reply_comments = new_comments;
                        }
                    });
            }
        }
    }

}

SocialPostComment.components = { SocialPostCommentEmoji };
SocialPostComment.template = 'viin_social.SocialPostComment';
