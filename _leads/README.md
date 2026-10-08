# Lead catcher for whathappenstothehouse.com

The guide form on the home page can send leads straight to a Google Sheet and email, instead of opening the visitor's email app.
It is written in `Code.gs` (Google Apps Script). It stays off until `LEADS_ENDPOINT` in `_qa-src/site_schema.py` holds the web app's URL.
With the setting empty, the form opens the visitor's email app, as before.

What happens when someone sends the form:
1. A row is added to the Google Sheet "whathappenstothehouse.com Leads" (created automatically in the Drive of the account that deploys the script).
   Columns include a "Follow-up status" dropdown. New leads are highlighted.
2. Sam gets an email (sam@samyusufi.com). Reply goes straight to the visitor.
3. The visitor gets a short thank-you email from Sam with the guide link (at most one every few hours per address).
4. The page shows its thank-you screen with the Download button right away. No email app opens.
If the connection fails, the page shows Text, Call, and Email buttons and keeps what the visitor typed. Nothing is lost silently.

Protection: a hidden field bots fill, a minimum fill time, a per-request id (repeats are ignored), input checks, formula-neutralizing in the sheet,
and a cap of 40 submissions per hour.

## One-time setup (sign in as sam@samyusufi.com)
1. Go to https://script.google.com, click New project, and name it "whathappenstothehouse.com leads".
2. Replace the editor's contents with `Code.gs` from this folder. Save.
3. Choose the function `setup` and click Run. Approve Google's permission screen (spreadsheets and sending email as you). The log shows the new Sheet's link.
4. Choose `sendTest` and click Run. Check that a row appeared and that two emails arrived (one notice, one thank-you), both in your inbox.
5. Click Deploy > New deployment > the gear icon > Web app. Execute as: Me. Who has access: Anyone. Click Deploy and copy the Web app URL (it ends in /exec).
6. In `_qa-src/site_schema.py`, set `LEADS_ENDPOINT = "<that URL>"`. In the repo root run `python3 _guide-src/build.py`, then `python3 _qa-src/check.py`, commit, and push.
7. Send one real test from the live page and confirm the row, both emails, and the thank-you screen.

## Changing the script later
Edit `Code.gs` in the Apps Script editor, then Deploy > Manage deployments > pencil > Version: New version > Deploy. The URL stays the same.
Keep this file in sync with the editor. To turn the new form off, set `LEADS_ENDPOINT = ""` and rebuild.

## Limits
Google allows about 1,500 emails a day for a Workspace account (100 for a free Gmail account). Each lead uses two.
