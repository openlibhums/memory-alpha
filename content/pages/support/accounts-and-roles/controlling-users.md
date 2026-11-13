# Controlling users

Controlling a user lets you sign in to Janeway as another user, without their password. While you control an account, you see Janeway exactly as that user does, with their roles, tasks and permissions. This is useful for investigating problems reported by users, or for helping users when they can't complete part of the workflow. In the Janeway logs, controlling a user is called "hijacking".

Only users with staff permission can control other users. This is usually press managers or those with similar roles within the press/journal. See [Staff permission](./roles-and-permissions-on-janeway.md#staff-permission).

The control functionality can be disabled entirely by a system administrator, if required.

> [!WARNING]
> Everything you do when controlling an account is recorded as that user's action. For example, an email you send or a review you submit appears to come from them. Only act on a user's behalf when they have agreed and your press policy allows it.

## When to control a user

It can be helpful to control a user when you need to see or do something exactly as they would. For example:

- To investigate an issue reported by a user.
- To check what pages, tasks and articles a user can access - especially when they report being unable to access parts of the system.
- To complete a step for a user who can't do it themselves, when they have agreed for you to do it for them.

## When not to control a user

Janeway doesn't have a policy on controlling users. We recommend you follow your press policy. As best practice, don't control a user under the following circumstances:

- Without their knowledge or consent, except if your role explictly allows you to do so (e.g. technical support for a press).
- To submit, review or make other editorial decisions on their behalf, unless they have agreed and your press's policy allows you to do so.
- To view or change their personal details beyond what is required for the task.

If you only need to change a user's details or roles, edit their account instead or ask them to edit their profile. See [Managing user accounts](./managing-user-accounts.md).

## How to control a user

1. Go to **Journal users** on the Manager dashboard or **All users** on the Press manager.
2. Find the user.
3. Click **Control**.
   ![The Journal users list, with the Control button highlighted ](../images/control-user-button.png)

Janeway will then open the user's dashboard. A banner at the top of each back-office page shows **You are currently working on behalf of** followed by the user's name. Click the **Release** button to stop controlling the user. If you click the **Release** button on a page the controlling account does not have access to (e.g. an author's revision request) you will be presented with a server error. Going to any other page you would normally have access to will resolve this. If you leave the website without releasing the user you are controlling, you may be faced with an error when returning accompanied with an **Abort** button. Click this button and return to a page you would normally have access to to resolve this.

![The banner reading 'You are currently working on behalf of' a user.](../images/control-user-banner.png)

> [!NOTE]
> You can only control active users. If you try to control an inactive user, you will see a server error.

> [!NOTE]
> The banner appears only in the back office, not on the public journal website.

## What Janeway records

Janeway logs when you start and stop controlling a user, with your name and the user's name. These log entries appear as **Hijack start** and **Hijack release** in the admin area, under **Log entries**. They don't appear on the user's **History** page, which lists emails only.

Actions you take while controlling the account aren't marked as yours. They are recorded as the user's own.
