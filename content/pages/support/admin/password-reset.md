# Passwords
 
Even in admin, no one can see a user's current password, including staff and system administrators. Janeway stores passwords in a hashed form that can't be turned back into the original. The **Password** field on the account record shows how the password is stored, not the password itself. Passwords can be reset and managed through admin, but this should be a last resort. If a user has forgotten their password, help them set a new one. Use these options in order.
 
## Ask the user to reset their password
 
Ask the user to select **Forgotten your password?** on the login page and enter their email address. Janeway emails them a link to set a new password. See [Account troubleshooting](../guides/account-troubleshooting.md).
 
The link works for 24 hours, and only once. Each new request cancels any earlier link. Setting a new password also activates the account, if it was inactive.

You can see when a password reset link was last send at the bottom of the account page.
 
## Send a password reset link yourself
 
Sometimes the user doesn't receive the email, for example because it went to their spam folder. You can then copy their reset link from the admin area and send it to them.
 
1. Find the user's account record.
2. Scroll down to **Password reset tokens**.
3. Find the most recent token where **Expired** isn't ticked and the **Expires on** date hasn't passed.
4. Copy the token value. It is a long code in the form `3f2a9c1e-5b7d-4e8a-9c21-7d4e5f6a8b90`.
5. Add `/reset/step/2/`, the token and a final `/` to the end of the journal's web address. For example:
   - Path mode: `https://www.pressdomain.com/orbit/reset/step/2/3f2a9c1e-5b7d-4e8a-9c21-7d4e5f6a8b90/`
   - Domain mode: `https://www.orbitjournal.com/reset/step/2/3f2a9c1e-5b7d-4e8a-9c21-7d4e5f6a8b90/`
6. Send the link to the user, at the email address on their account.

If no token is listed, or every token has expired, create a new one. On the journal's login page, select **Forgotten your password?** and enter the user's email address. Janeway emails the user and adds a new token to their account, which you can then copy.
 
> [!WARNING]
> Anyone with the link can set a new password for the account. Send it only to the user, and only to the email address on their account. Don't open the link and set a password yourself.
 
## Change a password directly
 
Only change a user's password yourself if the other options haven't worked. You would then need to tell the user their new password, which is less secure than a reset link.
 
1. On the account page, under **Password**, select **this form**.
    ![The password field on the account redord.]()
2. Enter the new password in both password fields.
3. Click **Change password** to save the change.
4. Tell the user the new password by a secure route, and ask them to change it as soon as they sign in. See [Update your password](../guides/account-troubleshooting.md#update-your-password).

> [!NOTE]
> Passwords set here don't have to follow the press's password rules, such as minimum length. It is recommended to choose a password that meets them anyway.