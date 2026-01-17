# Google Workspace Access Model (Groups + Shared Drives)

## Goal
Use Google Groups to manage Shared Drive permissions so access is consistent, auditable, and easy to change.

## Principles
- Assign permissions to **Google Groups**, not individual users.
- Use **least privilege**: give the minimum access needed for the role.
- Keep naming consistent so people can understand access quickly.
- Make onboarding/offboarding fast by changing group membership only.

## Group naming convention
Format:
- gws-sd-<drive>-owners
- gws-sd-<drive>-managers
- gws-sd-<drive>-contributors
- gws-sd-<drive>-viewers

Example (Media):
- gws-sd-media-owners
- gws-sd-media-managers
- gws-sd-media-contributors
- gws-sd-media-viewers
- gws-sd-media-archive-viewers

## Shared Drive permission mapping (example)
- Media - Active
  - gws-sd-media-owners -> Manager
  - gws-sd-media-managers -> Content manager
  - gws-sd-media-contributors -> Contributor
  - gws-sd-media-viewers -> Viewer
- Media - Archive
  - gws-sd-media-archive-viewers -> Viewer
  - (Optional) gws-sd-media-archive-managers -> Content manager

## Onboarding flow (simple)
1. Create user (correct OU).
2. Enforce MFA / security baseline.
3. Add user to role group(s) (example: "media-editors").
4. Role group membership determines Shared Drive access via the permission groups above.
5. Verify access (drive + key folders).

## Offboarding flow (simple)
1. Suspend user immediately.
2. Remove from all groups (or disable account first, then clean up).
3. Transfer ownership of key files if needed.
4. Verify access is removed.
5. Document actions in the ticket.

## Audit and maintenance
- Quarterly: review group membership for privileged groups (owners/managers).
- When someone changes role: update group membership only (no direct permissions).
