from odoo import _, models


class ResUser(models.Model):
    _inherit = "res.users"

    def reset_password(self, login):
        """retrieve the user corresponding to login (login or email),
        and reset their password
        """
        users = self.search([("login", "=", login)])
        if not users:
            users = self.search([("email", "=", login)])
        if len(users) != 1:
            raise Exception(
                _("Incorrect email. Please enter the registered email address.")
            )
        return users.action_reset_password()
