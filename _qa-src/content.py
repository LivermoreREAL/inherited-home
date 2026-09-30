# Page content for the "What Happens to the House?" question site.
# Each page: slug, topic, h1, meta (search description), short (the quotable short answer),
# body (HTML), related (list of slugs). Written from the approved guide v2 (Sept 2026).

PAGES = [
dict(
slug="inherited-house-first-30-days",
topic="Getting started",
h1="What should you do with an inherited house in the first 30 days?",
meta="The first steps to take with an inherited house in California: secure it, photograph it, call the insurer, keep bills current, gather paperwork, and wait on belongings.",
short="Focus on protecting the house, not selling it. Secure it, photograph every room, tell the insurance company it may be vacant, and keep the utilities and bills current. Gather the paperwork, hold off on belongings until someone has legal authority, and talk to an attorney before signing anything.",
body="""
<p>Before anyone talks about selling, the house just needs to be looked after. Here's what helps most in the first few weeks.</p>
<ol class="steps">
<li><b>Keep it secure.</b> Lock the doors and windows, and have someone stop by at least once a week.</li>
<li><b>Take photos before anything changes.</b> Photograph every room, inside and out, before any cleaning or repairs. It gives the estate and the whole family a clear record of the home's condition.</li>
<li><b>Call the homeowner's insurance company.</b> Let them know the owner has passed and the home may be empty. Many policies limit coverage when a home sits vacant, so ask what you need to do to stay covered.</li>
<li><b>Keep the utilities on.</b> Power, water, and heat protect the house from damage and make it easier to show later.</li>
<li><b>Keep up with the bills.</b> The mortgage, property taxes, insurance, and HOA dues don't pause. Keep every receipt, and ask the attorney how those payments will be handled.</li>
<li><b>Hold off on the belongings.</b> It's natural to want to start sorting. Wait on selling or giving away anything of value until someone has the legal authority to do it.</li>
<li><b>Gather the paperwork.</b> Look for the will or trust, the deed, recent mortgage, HELOC, and property tax statements, the insurance policy, and any HOA information. Order several certified copies of the death certificate.</li>
<li><b>Talk to an attorney before signing anything.</b> That includes offers from investors who reach out by mail or phone. There's no rush to respond.</li>
</ol>
<p class="why">And here's why it matters: a well-cared-for house protects the value of the estate for everyone in the family.</p>
""",
related=["does-inherited-house-go-through-probate","common-mistakes-inherited-house","sell-inherited-house-as-is-or-fix-up"]),

dict(
slug="does-inherited-house-go-through-probate",
topic="Getting started",
h1="Does an inherited house have to go through probate in California?",
meta="Whether an inherited California home goes through probate depends on how it was owned: living trust, joint tenancy, transfer-on-death deed, or the person's name alone.",
short="Not always. It depends on how the home was owned. A home in a living trust, in joint tenancy with a surviving owner, or with a transfer-on-death deed usually passes without probate. A home in the person's name alone, with no trust, usually goes through probate, though some smaller estates and surviving spouses can use simpler procedures.",
body="""
<p>Say your mother passed away in March. She owned her home in Pleasanton outright. You're one of three siblings, and none of you have been through this before. The first question is always the same: <b>was there a trust?</b></p>
<table class="t">
<tr><th>How the home was owned</th><th>What usually happens</th></tr>
<tr><td>In the name of a living trust</td><td>The trust path. A successor trustee manages the home, usually without any court involvement.</td></tr>
<tr><td>Joint tenancy with someone still living</td><td>The surviving owner usually takes over without probate, once some paperwork is recorded.</td></tr>
<tr><td>With a transfer-on-death deed</td><td>The named beneficiary usually receives the home without probate, once some paperwork is recorded.</td></tr>
<tr><td>In the person's name alone, with no trust</td><td>Usually probate, a court process. Simpler procedures exist for some smaller estates and surviving spouses, so ask an attorney what applies.</td></tr>
</table>
<h2>How to find out how the home was owned</h2>
<p>The current deed will tell you. You can request a copy from the county recorder's office. A title company or a real estate agent can usually pull one for you, too.</p>
<h2>Two assumptions to double-check</h2>
<ul class="dots">
<li><b>"There's a will, so there's no probate."</b> A will says who inherits. If the house was in the person's name alone, it may still go through probate.</li>
<li><b>"There's a trust, so the house is in it."</b> Not always. Homes are sometimes never transferred into the trust, or are taken out during a refinance. The deed will tell you.</li>
</ul>
<p class="src">Official source: <a href="https://selfhelp.courts.ca.gov/probate/simple-transfer">California Courts, when formal probate may not be needed</a></p>
""",
related=["selling-house-in-a-trust","who-can-sell-house-in-probate","how-long-does-probate-take"]),

dict(
slug="who-can-sell-house-in-probate",
topic="Probate",
h1="Who has the authority to sell a house in probate?",
meta="In a California probate, only the court-appointed Personal Representative (executor or administrator) can sell the house, and only after the court issues Letters.",
short="Only the Personal Representative the court appoints: the executor if there's a will, or the administrator if there isn't. They can't sell until the court issues Letters, and the Letters say whether they have full or limited authority. Being the closest relative doesn't give someone authority on its own.",
body="""
<h2>Executor or administrator</h2>
<p>The court appoints a <b>Personal Representative</b> to handle the estate. If there's a will, it's usually the executor named in it. If there isn't one, it's usually a close family member, called the administrator.</p>
<h2>Nothing happens until Letters are issued</h2>
<p>Once appointed, the Personal Representative receives a court document called <b>Letters</b>: Letters Testamentary if there's a will, Letters of Administration if there isn't. Nobody has the authority to sell the house until Letters are issued.</p>
<p>The Letters also say how much authority the Personal Representative has: full or limited. That one detail shapes the whole sale.</p>
<div class="box"><p><b>Being next of kin isn't the same as having authority.</b> A spouse, child, or sibling may feel responsible for the house, but only the Personal Representative can sign a listing, approve work, or accept an offer.</p></div>
""",
related=["full-vs-limited-authority","notice-of-proposed-action","probate-overbids"]),

dict(
slug="full-vs-limited-authority",
topic="Probate",
h1="What's the difference between full and limited authority in probate?",
meta="Full authority under California's IAEA lets a Personal Representative sell a house without a court hearing after 15 days' notice. Limited authority requires court confirmation.",
short="It's the level of power the court gives the Personal Representative. With full authority under California's Independent Administration of Estates Act (IAEA), they can sell the house without a court hearing, after giving heirs 15 days' written notice. With limited authority, the sale needs a court confirmation hearing, where other buyers can overbid.",
body="""
<div class="two">
<div class="card"><div class="s">Full authority</div><div class="ct">Sale without a court hearing</div><p>Under the IAEA, the Personal Representative can sell the home without a court hearing, as long as every heir gets written notice first.</p><p><b>Usually faster and more private.</b></p></div>
<div class="card"><div class="s">Limited authority</div><div class="ct">Sale confirmed by the court</div><p>The sale needs a court hearing to be confirmed, and other buyers can outbid the accepted offer at that hearing.</p><p><b>Adds a court date and a bidding step.</b></p></div>
</div>
<h2>Where to find out which one applies</h2>
<p>It's written in the Personal Representative's Letters. It's worth confirming before anyone talks about price or a listing date, because it changes the timeline.</p>
<h2>What full authority still requires</h2>
<p>Even with full authority, the Personal Representative sends a Notice of Proposed Action to every heir before the sale. If someone objects within 15 days, the sale goes to the court after all.</p>
""",
related=["notice-of-proposed-action","probate-overbids","how-long-does-probate-take"]),

dict(
slug="notice-of-proposed-action",
topic="Probate",
h1="What is a Notice of Proposed Action in a probate sale?",
meta="A Notice of Proposed Action (NOPA) tells every heir about a planned probate sale. If no one objects within 15 days, the sale proceeds without a court hearing.",
short="A Notice of Proposed Action (NOPA) is a formal written notice the Personal Representative sends to every heir and interested party before selling under full authority. If no one objects within 15 days, the sale moves forward without a court hearing. If someone does object, the sale goes to the court for approval.",
body="""
<p>In plain English: it's a formal heads-up that says, "Here's the sale we plan to make." It gives everyone with an interest in the estate a chance to speak up before the house is sold.</p>
<h2>The 15-day window</h2>
<p>If nobody objects within 15 days, the sale proceeds to closing, with no court hearing needed. If someone objects, the sale moves to court confirmation, where other buyers can overbid.</p>
<h2>Where families get tripped up</h2>
<ul class="dots">
<li><b>Missing someone.</b> If an heir doesn't receive the notice correctly, the 15-day clock can start over.</li>
<li><b>Not planning for it.</b> Families are often least prepared for this step, so build the 15 days into the timeline from the start.</li>
</ul>
""",
related=["full-vs-limited-authority","probate-overbids","who-can-sell-house-in-probate"]),

dict(
slug="probate-overbids",
topic="Probate",
h1="How do overbids work in a California probate sale?",
meta="In a court-confirmed California probate sale, the first overbid must be at least the accepted price plus 10% of the first $10,000 and 5% of the rest. Example included.",
short="When a probate sale needs court confirmation, the accepted offer isn't final until a court hearing. At that hearing, other buyers can bid more. The first overbid must be at least the accepted price, plus 10% of the first $10,000, plus 5% of the rest. On an $800,000 offer, that's $840,500.",
body="""
<h2>When does a sale need court confirmation?</h2>
<p>It depends on the authority in the Personal Representative's Letters. With limited authority, the sale goes to court. With full authority, a sale only goes to court if an heir objects to the Notice of Proposed Action.</p>
<p>For a court-confirmed sale, the price usually has to be at least 90% of the value set by the <b>probate referee</b>, a court-appointed appraiser.</p>
<h2>How the minimum overbid is figured</h2>
<table class="math">
<tr><td>Accepted offer</td><td>$800,000</td></tr>
<tr><td>Plus 10% of the first $10,000</td><td>$1,000</td></tr>
<tr><td>Plus 5% of the remaining $790,000</td><td>$39,500</td></tr>
<tr class="tot"><td>Minimum first overbid</td><td>$840,500</td></tr>
</table>
<h2>What happens at the hearing</h2>
<p>Any qualified buyer can make a higher offer at the hearing. The highest bid wins, and the court confirms the sale.</p>
<h2>What this means for your family</h2>
<p>A court-confirmed sale adds a hearing date and a bidding step to the timeline. Hearing dates depend on the county court's calendar, so it helps to plan for it from the start.</p>
""",
related=["full-vs-limited-authority","notice-of-proposed-action","how-long-does-probate-take"]),

dict(
slug="how-long-does-probate-take",
topic="Probate",
h1="How long does probate take in California?",
meta="Many California probates take 9 to 18 months, and some take longer. The house can usually be sold before the estate closes, once the Personal Representative has authority.",
short="Many California probates take 9 to 18 months, and some take longer. The good news: the house can usually be sold before the estate closes, once the Personal Representative has Letters and the authority to sell.",
body="""
<h2>What affects the timeline</h2>
<ul class="dots">
<li>How long it takes the court to appoint the Personal Representative and issue Letters.</li>
<li>Whether the sale needs court confirmation, which adds a hearing date.</li>
<li>Whether any heir objects to the Notice of Proposed Action.</li>
<li>Whether family members agree on the plan for the house.</li>
</ul>
<h2>The typical steps for selling (full authority)</h2>
<ol class="steps sm">
<li>The court appoints the Personal Representative and issues Letters.</li>
<li>A probate referee appraises the home. This can happen while the house is being prepared.</li>
<li>The Personal Representative signs a listing agreement.</li>
<li>The home is marketed and shown.</li>
<li>An offer is accepted.</li>
<li>The Notice of Proposed Action goes to every heir. The 15-day clock starts.</li>
<li>If no one objects, the sale moves to closing.</li>
<li>If someone objects, the sale goes to court confirmation, with the overbid process.</li>
</ol>
<p>If the home is in a trust instead, the sale is usually faster, because most trust sales don't involve the court at all.</p>
<p class="src">Official source: <a href="https://selfhelp.courts.ca.gov/probate/formal-probate">California Courts, how formal probate works</a></p>
""",
related=["full-vs-limited-authority","selling-house-in-a-trust","inherited-house-first-30-days"]),

dict(
slug="selling-house-in-a-trust",
topic="Trusts",
h1="How do you sell a house held in a trust in California?",
meta="A successor trustee can usually sell a California trust home without court involvement, once proof of authority is in place and beneficiaries have been notified.",
short="The successor trustee named in the trust usually sells it without going to court. Before listing, the trustee needs proof of authority in place, often a Certification of Trust, and must follow the trust's terms. California also requires the trustee to notify beneficiaries and heirs within 60 days after the trust becomes irrevocable.",
body="""
<h2>Who's in charge</h2>
<p>When the person who created the trust passes, the <b>successor trustee</b> named in the trust takes over. The trustee follows the trust document, not the probate court.</p>
<h2>Paperwork comes first</h2>
<p>Before the home is listed, the trustee needs proof of their authority. That proof is often a short document called a <b>Certification of Trust</b>, which confirms the trustee's power without sharing the whole trust.</p>
<h2>Notice to the family</h2>
<p>When a trust becomes irrevocable at death, California requires the trustee to send a formal notice to beneficiaries and heirs within 60 days. The attorney usually handles this, but it's part of the timeline.</p>
<h2>A real responsibility</h2>
<p>A trustee has a <b>fiduciary duty</b> to every beneficiary. In plain English: decisions about the house have to be fair to everyone the trust names, not just the trustee.</p>
<div class="two">
<div class="card"><div class="s">What's usually easier</div><ul class="dots"><li>No court hearing</li><li>No 15-day notice before a sale</li><li>No overbid process</li><li>A faster timeline overall</li></ul></div>
<div class="card"><div class="s">What still needs care</div><ul class="dots"><li>Trustee paperwork in place first</li><li>Following the trust's terms</li><li>Keeping beneficiaries informed</li><li>Agreement among beneficiaries</li></ul></div>
</div>
""",
related=["does-inherited-house-go-through-probate","siblings-disagree-inherited-house","inherited-house-capital-gains"]),

dict(
slug="sell-inherited-house-as-is-or-fix-up",
topic="Selling",
h1="Should you sell an inherited house as-is or fix it up first?",
meta="Selling an inherited California house as-is, with light preparation, or fully updated: how to decide, and what to ask before spending estate money.",
short="It depends on the house and the family's goals. Selling as-is is the simplest option and common in probate. Light preparation, like a clean-out, paint, yard cleanup, and small repairs, is often the best balance of cost and return. Bigger updates can raise the price but take time and estate money, so find out what buyers would pay first.",
body="""
<table class="t">
<tr><th>Path</th><th>What it looks like</th></tr>
<tr><td>Sell as-is</td><td>Little or no work before listing. The simplest option, and common for probate sales. Buyers factor repairs into their offers.</td></tr>
<tr><td>Light preparation</td><td>A clean-out, deep cleaning, fresh paint, yard cleanup, and small repairs. Often the best balance of cost and return.</td></tr>
<tr><td>Full preparation</td><td>Larger repairs or updates before listing. Can raise the price, but takes more time and upfront money.</td></tr>
</table>
<p>Any work should be approved by the Personal Representative or trustee, and paid by the estate or trust.</p>
<h2>Before you spend estate money, ask</h2>
<ul class="dots">
<li>What would buyers likely pay for the house as it is today?</li>
<li>Which repairs actually matter to buyers, and which are just cosmetic?</li>
<li>What does waiting cost each month in mortgage, taxes, insurance, and upkeep?</li>
<li>Will the work likely add more to the sale price than it costs?</li>
</ul>
<h2>Clean-out and estate sales</h2>
<p>Sorting a lifetime of belongings takes longer than most families expect. Set aside photos, keepsakes, and important papers first. If you're holding an estate sale, book early and schedule it around showings.</p>
<h2>Disclosures</h2>
<p>Sales by a Personal Representative or trustee are often exempt from California's standard Transfer Disclosure Statement. You'll still need to share what you know about the home's condition.</p>
""",
related=["inherited-house-first-30-days","inherited-house-capital-gains","whos-on-your-team"]),

dict(
slug="inherited-house-capital-gains",
topic="Taxes",
h1="Do you pay capital gains tax when you sell an inherited house?",
meta="Inherited property usually gets a stepped-up basis, so selling soon after inheriting often means little or no capital gains tax. Example with real numbers.",
short="Often little or none, if you sell soon after inheriting. Inherited property usually gets a stepped-up basis, meaning its value for tax purposes resets to what it was worth on the date of death. Capital gains are then figured from that value, not from what the original owner paid. Confirm the details with a CPA.",
body="""
<h2>How stepped-up basis works</h2>
<div class="box"><p>Say your parents bought their home in 1985 for $150,000, and it was worth $1,100,000 when your mother passed. If the family sells a few months later for $1,120,000, capital gains are usually figured from about $1,100,000, not $150,000.</p></div>
<p>That's why selling soon after inheriting often means little or no capital gains tax. Holding the house for years while it gains value is a different story, so it's worth a conversation with the estate's CPA before deciding.</p>
<h2>Good questions to ask your CPA</h2>
<ul class="dots">
<li>Should we get a date-of-death value for the home in writing?</li>
<li>How will the sale be reported, and by whom?</li>
<li>Which costs of preparing and selling the home can reduce any gain?</li>
</ul>
<p>If anyone in the family is thinking about keeping the house instead, ask about Proposition 19 too. It can change the property tax bill. You can estimate it with the free <a href="/prop19-calculator/">Prop 19 Calculator</a>.</p>
""",
related=["prop-19-inherited-home","sell-inherited-house-as-is-or-fix-up","whos-on-your-team"]),

dict(
slug="prop-19-inherited-home",
topic="Taxes",
h1="Does Prop 19 apply to an inherited home in California?",
meta="Under Prop 19, a child keeps a parent's low property tax base only by making the inherited home their primary residence within a year, up to a value limit.",
short="Yes, for inheritances since February 2021. A child who inherits a parent's home keeps the parent's property tax base only if they make it their own primary residence within one year, and only up to the parent's taxable value plus $1,044,586 (for transfers from February 16, 2025 to February 15, 2027). Otherwise, the home is reassessed at today's market value, which can mean a much higher tax bill.",
body="""
<h2>The common assumption</h2>
<p>"I inherited my parents' house, so I keep their low property tax bill." Since February 2021, that's often not true.</p>
<h2>How it works</h2>
<ul class="dots">
<li>If you move in and make it your primary residence within one year, you can keep your parent's tax base, up to your parent's taxable value plus $1,044,586. Any value above that is added.</li>
<li>If you don't move in, for example if you rent it out or keep it empty, the home is reassessed at current market value.</li>
</ul>
<div class="box"><p>Say your parents' home is assessed at $150,000 for tax purposes, and it's worth $1,100,000 today. If it's reassessed, property taxes are based on about $1,100,000 instead, roughly seven times the old amount.</p></div>
<p class="why">And here's why it matters: if anyone in the family is thinking about keeping the house, talk to a CPA about Prop 19 before you decide.</p>
<div class="box"><p><b>Run your own numbers:</b> the free <a href="/prop19-calculator/">Prop 19 Calculator</a> shows the property tax bill with and without a child moving in, using 2025-26 rates for Alameda, Contra Costa, and San Joaquin counties.</p></div>
""",
related=["inherited-house-capital-gains","siblings-disagree-inherited-house","common-mistakes-inherited-house"]),

dict(
slug="siblings-disagree-inherited-house",
topic="Family",
h1="What if siblings disagree about selling an inherited house?",
meta="How California families can work through disagreements about an inherited house: agree on the process, share the same numbers, and let the attorney guide real disputes.",
short="It's common, and it doesn't mean your family is doing it wrong. Agree on the process before debating price, work from the same written opinion of value, share information with everyone at the same time, and let the estate attorney guide real disputes. If someone lives in the house or wants to buy out the others, talk to the attorney early.",
body="""
<h2>Questions to talk through early</h2>
<ul class="dots">
<li>Does anyone want to keep the house, or buy out the others?</li>
<li>Is anyone living there now?</li>
<li>Who has keys and access right now?</li>
<li>What should happen to the belongings, and who decides?</li>
<li>Is there a timeline the family is hoping for?</li>
<li>What matters most: the highest price, simplicity, or speed?</li>
</ul>
<p class="why">That last answer shapes almost every decision that follows.</p>
<h2>When you don't agree</h2>
<ol class="steps sm">
<li><b>Agree on the process before you debate the price.</b> Decide who makes which decisions and how everyone will be kept informed.</li>
<li><b>Work from the same numbers.</b> A neutral, written opinion of the home's value gives everyone a shared starting point.</li>
<li><b>Share information with everyone at the same time.</b> It's the simplest way to build trust when emotions are high.</li>
<li><b>Let the attorney guide real disputes.</b> The Personal Representative or trustee has legal duties, and the attorney can explain the options.</li>
</ol>
""",
related=["who-can-sell-house-in-probate","selling-house-in-a-trust","common-mistakes-inherited-house"]),

dict(
slug="common-mistakes-inherited-house",
topic="Getting started",
h1="What are the most common mistakes when selling an inherited house?",
meta="Nine common mistakes California families make with an inherited house, from assuming a will avoids probate to learning about Prop 19 too late, and how to avoid each.",
short="Most come from honest assumptions: thinking a will avoids probate, assuming the house is in the trust, acting before anyone has authority, debating price before agreeing on a process, clearing out belongings too quickly, renovating without a plan, and learning about Prop 19 too late.",
body="""
<dl class="pit">
<div><dt>Assuming a will means no probate</dt><dd>A will names who inherits. The house may still need to go through probate.</dd></div>
<div><dt>Assuming the house is in the trust</dt><dd>Check the deed. Homes are sometimes never transferred in, or are taken out during a refinance.</dd></div>
<div><dt>Acting before anyone has authority</dt><dd>Being the closest relative isn't the same as having legal authority. In probate, wait until Letters are issued.</dd></div>
<div><dt>Listing before the trustee paperwork is ready</dt><dd>A successor trustee needs proof of authority in place before the home goes on the market.</dd></div>
<div><dt>Debating price before agreeing on the process</dt><dd>Settle who decides, and how, before anyone talks numbers.</dd></div>
<div><dt>Missing someone on the notice</dt><dd>If an heir doesn't receive the Notice of Proposed Action correctly, the 15-day clock can start over.</dd></div>
<div><dt>Clearing out belongings too quickly</dt><dd>Make sure the right people agree on what happens to belongings before anything is sold, donated, or thrown away.</dd></div>
<div><dt>Renovating before there's a plan</dt><dd>Know what the house is worth as it is, and what buyers care about, before spending estate money.</dd></div>
<div><dt>Learning about Prop 19 too late</dt><dd>If anyone might keep the house, talk to a CPA about property taxes before the family decides.</dd></div>
</dl>
""",
related=["inherited-house-first-30-days","does-inherited-house-go-through-probate","siblings-disagree-inherited-house"]),

dict(
slug="whos-on-your-team",
topic="Selling",
h1="Who do you need on your team to settle an inherited house?",
meta="The professionals who help settle an inherited California house: estate attorney, CPA, title and escrow, insurance agent, real estate agent, and more, and what each handles.",
short="Usually a small team: an estate attorney for legal authority and court steps, a CPA for taxes, title and escrow to confirm ownership and close the sale, an insurance agent to keep the home covered, and a real estate agent for value, preparation, and the sale. In probate, the court also appoints a probate referee to appraise the property.",
body="""
<table class="t">
<tr><th>Who</th><th>What they handle</th></tr>
<tr><td>Estate attorney</td><td>Legal authority, probate or trust procedure, court filings, and disagreements between heirs.</td></tr>
<tr><td>CPA or tax professional</td><td>Stepped-up basis, Prop 19, and any tax returns for the estate or trust.</td></tr>
<tr><td>Title and escrow</td><td>Confirming ownership, paying off the mortgage and any liens, and closing the sale.</td></tr>
<tr><td>Insurance agent</td><td>Keeping the home covered while it's vacant or changing hands.</td></tr>
<tr><td>Real estate agent</td><td>Value, preparation, pricing, marketing, and timing the sale around notice periods and court dates.</td></tr>
<tr><td>Estate sale or clean-out company</td><td>Sorting, selling, donating, or removing belongings.</td></tr>
<tr><td>Contractors and handymen</td><td>Repairs and preparation approved by the Personal Representative or trustee.</td></tr>
<tr><td>Probate referee</td><td>Appraises the property for the court. Probate only, and appointed by the court, not hired by the family.</td></tr>
</table>
<p class="why">When everyone knows their role, the house doesn't get stuck waiting on the wrong person.</p>
""",
related=["sell-inherited-house-as-is-or-fix-up","who-can-sell-house-in-probate","inherited-house-capital-gains"]),

dict(
slug="probate-trust-glossary",
topic="Reference",
h1="Probate and trust terms, explained",
meta="Definitions of common California probate and trust terms: executor, administrator, Letters, IAEA, NOPA, overbid, probate referee, successor trustee, stepped-up basis, Prop 19.",
short="The words you'll hear most when a home is in probate or a trust, and what they mean. You're not expected to know them. Here they are, one at a time.",
glossary=[
("Administrator","The person the court appoints to handle an estate when there's no will, or no executor able to serve."),
("Beneficiary","A person named to receive something from a will or trust."),
("Certification of Trust","A short document that proves a trustee's authority without sharing the whole trust."),
("Court confirmation","A probate court hearing that approves a home sale, where other buyers can overbid."),
("Executor","The person named in a will to handle the estate."),
("Heir","A family member who has a right to inherit under California law."),
("IAEA","The Independent Administration of Estates Act. It lets a Personal Representative handle many tasks, including selling a home, with less court involvement."),
("Letters","The court document that gives a Personal Representative authority to act for the estate."),
("NOPA","Notice of Proposed Action. The written notice sent to heirs before a sale under full authority. Heirs have 15 days to object."),
("Overbid","A higher offer made at a court confirmation hearing."),
("Personal Representative","The general term for an executor or administrator."),
("Probate","The court process for settling an estate when property isn't held in a trust or passed on another way."),
("Probate referee","A court-appointed appraiser who values the estate's property."),
("Proposition 19","The 2021 California law that changed how inherited homes are taxed."),
("Stepped-up basis","The reset of an inherited home's tax value to what it was worth on the date of death."),
("Successor trustee","The person named in a trust to take over when the original trustee passes or can't serve."),
],
body="",
related=["who-can-sell-house-in-probate","full-vs-limited-authority","selling-house-in-a-trust"]),
]

GROUPS = [
("Getting started", ["inherited-house-first-30-days","does-inherited-house-go-through-probate","common-mistakes-inherited-house"]),
("If the home is in probate", ["who-can-sell-house-in-probate","full-vs-limited-authority","notice-of-proposed-action","probate-overbids","how-long-does-probate-take"]),
("If the home is in a trust", ["selling-house-in-a-trust"]),
("Preparing and selling", ["sell-inherited-house-as-is-or-fix-up","whos-on-your-team"]),
("Taxes", ["inherited-house-capital-gains","prop-19-inherited-home"]),
("Family", ["siblings-disagree-inherited-house"]),
("Reference", ["probate-trust-glossary"]),
]
