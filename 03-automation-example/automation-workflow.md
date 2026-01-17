# Automation Example: New Hire → Accounts + Notifications

## Goal
Reduce manual steps for onboarding by using a no-code automation tool (Make/Zapier/n8n) with a simple approval flow.

## Trigger
- New row added to a Google Sheet: "New Hires"
  - Fields: full_name, personal_email, work_email, role, department, manager_email, start_date

## Workflow steps
1. Validate required fields
   - If missing: notify IT channel + tag HR/manager, then stop.

2. Notify Slack
   - Post to #it-ops (or #onboarding):
     - New hire name, role, start date, manager

3. Create Trello card
   - Board: "IT Onboarding"
   - List: "To Do"
   - Card title: "Onboard <full_name> (<start_date>)"
   - Checklist: Google account, MFA, Groups, Shared Drives, Slack, Trello
   - Assign: IT owner + manager

4. Email manager (confirmation)
   - Ask manager to confirm access requirements
   - Include link to the Trello card

5. Log outcome
   - Update the Google Sheet row:
     - status = "Created"
     - trello_card_url = ...
     - timestamp = ...

## Error handling
- Duplicate work_email detected -> set status "Duplicate" and notify IT.
- API/tool failure -> set status "Failed" and notify IT with error details.
- Manual override -> allow IT to set status "Skip automation" for special cases.

## Auditability
- Keep all actions logged in:
  - Google Sheet status columns
  - Slack message thread link
  - Trello card history
