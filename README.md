# ShiftSure

**ShiftSure is a cross-platform mobile app that protects food delivery riders from short-term income loss caused by external disruptions like heavy rain, flooding, extreme heat, severe pollution, and access restrictions.**

We are building this for urban delivery riders who work shift-to-shift and lose real income when the city becomes temporarily undeliverable. Instead of making them file manual claims, ShiftSure uses a parametric model: when disruption conditions cross a defined threshold in the rider’s operating zone, the system automatically evaluates eligibility, runs fraud checks, and simulates payout.

The product is intentionally narrow. We are not trying to solve “insurance for everyone.” We are focused on one real use case: **weekly income protection for food delivery riders in high-disruption urban zones**. That focus makes the product easier to trust, easier to price, and much more realistic to build.

## The problem

Food delivery riders work in a fragile earning model. A missed lunch shift or evening shift is not a small inconvenience — it directly hits that week’s income.

In cities like Chennai, this problem gets worse during heavy rain, waterlogging, extreme heat, poor air quality, or sudden access restrictions. Riders are expected to stay available, but the city itself often becomes partially undeliverable. The result is simple: fewer completed deliveries, fewer working hours, and less money taken home.

Traditional insurance products are not built for this kind of loss. They are too broad, too slow, and too paperwork-heavy for a worker who needs short-cycle protection. What is missing is a lightweight income protection layer that works the same way these workers already live and earn: **weekly, mobile-first, and based on real external conditions**. :contentReference[oaicite:0]{index=0}

## Who this is for

We chose to focus on **food delivery riders in Chennai**, especially riders working on platforms like Swiggy and Zomato.

This was a deliberate choice. Food delivery is one of the clearest examples of disruption-linked income loss:
- riders work outdoors
- earnings depend on short working windows
- weather and mobility conditions directly affect order completion
- the impact is immediate and easy to understand

### Example persona

**Rahul**, 24, is a delivery rider in Chennai. He usually works two strong earning windows: lunch and evening. On days with heavy rain, flooding, or extreme heat, he may still be “working,” but practically he completes far fewer deliveries. A few bad disruption days in a week can materially cut his income.

ShiftSure is designed for someone like Rahul — not as a general insurance product, but as a focused income continuity tool.

## Our approach

ShiftSure is a **parametric income protection app**.

That means we do not wait for the rider to manually prove loss in the traditional sense. Instead, the app monitors predefined disruption signals in the rider’s insured operating zone. If the disruption crosses an agreed threshold, the system automatically checks whether:
- the rider has an active policy
- the rider’s zone matches the affected area
- the event is valid
- the claim passes fraud checks

If those conditions are satisfied, the app creates a claim and simulates payout.

This is a much better fit for gig workers than traditional claims-heavy insurance. It is faster, simpler, and easier to explain.

## How the app works

1. The rider signs up in the mobile app and selects their operating zone.
2. ShiftSure calculates a weekly risk score using zone-level and disruption-related signals.
3. Based on that score, the rider gets a weekly premium and protection plan.
4. Once the plan is active, the backend keeps monitoring disruption events.
5. If a valid disruption affects the rider’s zone, the system automatically checks eligibility.
6. A fraud layer verifies location and claim consistency.
7. If approved, the claim is created and payout is simulated.
8. The rider sees the reason, status, and protected amount in the app.

On the admin side, the system also shows exposure by zone, claims triggered, suspicious cases, and risk trends.

## Weekly premium model

We did not want pricing to feel like fake “insurance math.” The brief is clear that pricing should be weekly, and that actually makes sense for this audience. Food delivery riders think in weekly earnings, not annual policy cycles. So the product should too. :contentReference[oaicite:1]{index=1}

ShiftSure uses a **weekly micro-premium model** with a simple base plan and a risk adjustment layer on top.

### Base plans

| Plan | Weekly Premium | Daily Protection |
|------|----------------|------------------|
| Basic | ₹19/week | up to ₹250/day |
| Standard | ₹29/week | up to ₹400/day |
| Plus | ₹45/week | up to ₹600/day |

These are not final actuarial numbers. They are product-facing plan bands that make the pricing easy to understand in the app.

### How pricing is adjusted

The final premium is not flat across the city. A rider operating in a low-disruption zone should not pay the same as a rider working in a flood-prone or heat-heavy area.

So ShiftSure adjusts pricing using a risk score built from:
- operating zone
- rainfall severity history
- flood / waterlogging exposure
- heat exposure
- AQI severity
- disruption frequency
- shift timing

That gives us **hyperlocal weekly pricing**, which feels much more honest than a city-wide flat premium.

### Why this model works

The goal is not to maximize pricing complexity. The goal is to keep the model:
- affordable
- explainable
- adaptable
- realistic for gig workers

A weekly model also makes the demo stronger. It is easier to show why a rider paid ₹29 this week and got protected during a disruption than to explain some larger long-term policy construct.

## Parametric triggers

The app only works if the triggers are believable.

We are not building a vague “claim when something bad happens” system. We are defining a small set of external, measurable events that directly affect a rider’s ability to earn.

### Trigger set

#### 1. Heavy rain
Used when rainfall crosses a defined threshold in the rider’s operating zone.

#### 2. Flood / waterlogging
Used when road conditions or flood severity make delivery movement impractical.

#### 3. Extreme heat
Used when temperature or heat index makes sustained outdoor work unsafe.

#### 4. Severe air pollution
Used when AQI crosses a severe threshold and prolonged outdoor work becomes risky.

#### 5. Access restriction / mobility disruption
Used when the rider’s area is affected by road closure, zone restriction, curfew, or severe traffic blockage.

### Trigger logic

A claim becomes eligible only when:
- the disruption threshold is crossed
- the rider has an active policy
- the affected zone matches the rider’s insured zone
- the fraud score is within an acceptable range

This matters because we want the product to feel automated, but not careless.

### Why parametric works here

This use case is a strong fit for parametric insurance because the source of loss is external and measurable. We are not trying to judge damage after the fact. We are responding to disruption conditions that can be tracked in near real time. That keeps the workflow much cleaner than traditional claims handling. :contentReference[oaicite:2]{index=2}

## Where AI/ML fits

A lot of hackathon projects say they use AI, but only use it as decoration. We wanted it to sit in parts of the workflow where it actually changes product behavior.

ShiftSure uses AI/ML in three places.

### 1. Premium calculation

The first use is risk-based pricing. We use disruption-related signals to estimate how exposed a rider is to short-term income loss in a given zone.

Inputs include:
- historical rainfall patterns
- flood exposure
- AQI severity
- heat intensity
- zone-level disruption frequency
- rider shift pattern

Output:
- a risk score
- recommended weekly premium band
- suggested protection band

This is the most direct AI use in the product because it affects what the rider sees at onboarding.

### 2. Fraud detection

We also use ML-driven logic to score suspicious claims.

This includes checks like:
- GPS mismatch with insured zone
- duplicate claims for the same disruption window
- abnormal claim frequency
- event mismatch
- inconsistent rider activity patterns

The point is not to reject claims aggressively. The point is to stop the system from being trivially exploitable.

### 3. Predictive admin insights

The third use is on the admin side. We want the insurer view to show more than just counts and charts.

So the system will also estimate:
- which zones are likely to become high-risk next week
- where claim pressure may rise
- where payout burden is clustering

That makes the platform feel like an operational risk system, not just a worker app.

### Why we kept the AI practical

We are intentionally keeping the ML explainable. For this use case, a clear and interpretable risk/fraud model is more useful than a complicated model that looks impressive but is hard to trust.

## Why mobile, not web

We chose to build ShiftSure as a **cross-platform mobile app** because that is where this product actually belongs.

Food delivery riders already work through their phones. Their navigation, shift flow, earnings tracking, order handling, and communication all happen on mobile. Asking them to manage income protection from a desktop-first product would be unnatural.

### Why mobile is the right product decision

- riders need access during live work shifts
- location-aware checks are easier on mobile
- policy alerts and payout updates make more sense as mobile interactions
- onboarding is faster in an app flow
- it matches how gig workers already use digital tools

### Why cross-platform

We want one codebase and fast iteration during the hackathon, so we are building with **Flutter**. That gives us Android and iOS support without splitting effort.

The worker experience is mobile-first.  
The admin experience can still be supported through a lightweight dashboard later, but the main product is the rider app.

This was a deliberate product choice, not a technical convenience.

## Tech stack

We picked the stack with one constraint in mind: it should be fast enough for a hackathon, but not so hacky that the product falls apart the moment we add real workflows.

### Mobile app
- **Flutter** for cross-platform development
- Dart
- Riverpod for state management
- GoRouter for navigation
- Supabase Flutter SDK for auth and data access

Flutter gives us a single codebase for Android and iOS, which matters in a short build window. More importantly, it fits the product well: ShiftSure needs location-aware flows, notification-friendly UX, and a fast mobile onboarding experience.

### Backend
- **FastAPI**
- Python
- background jobs for trigger monitoring
- REST APIs for app/backend communication

We chose FastAPI because the project already needs Python for the AI/ML side. Keeping the backend and model-serving layer in the same ecosystem reduces friction and speeds up iteration.

### Database and backend platform
- **Supabase**
- PostgreSQL
- Supabase Auth
- Row Level Security
- Realtime subscriptions

Supabase gives us a strong base without wasting time on boilerplate backend setup. It is a good fit for hackathons because it handles auth, database, and realtime updates cleanly, while still giving us PostgreSQL underneath for proper relational modeling.

### AI / ML
- Python
- Pandas
- scikit-learn
- anomaly detection techniques for fraud scoring

We are deliberately keeping the ML stack practical. We do not need exotic models to prove the product. We need models that are explainable enough to justify pricing and credible enough to flag suspicious claims.

### External integrations
- weather API
- AQI API
- mobility / access disruption feed
- payout simulation layer
- location/GPS validation from the app

These integrations are what make the product feel real. The point of ShiftSure is not just to show UI screens — it is to connect app behavior to measurable external conditions.

## Development plan

We are treating the build in the same order the product needs to work.

### Phase 1 — Foundation
- lock persona and product scope
- define pricing model
- define trigger framework
- design app flow
- define backend services
- document architecture and README

### Phase 2 — Core product
- build rider onboarding flow
- build policy creation flow
- connect Supabase auth and database
- implement weekly premium calculation
- implement trigger monitoring service
- create automated claim flow

### Phase 3 — Intelligence and polish
- add fraud scoring
- add predictive admin metrics
- simulate payout workflow
- improve rider claim visibility
- prepare demo scenario and final presentation

The goal is not to overbuild. The goal is to make sure the product works end-to-end: onboarding, pricing, trigger detection, claim generation, fraud check, payout simulation.

## What makes this product different

A lot of teams will build something that looks like insurance software. We are trying to build something that feels like it actually belongs in the daily workflow of a delivery rider.

What makes ShiftSure stronger:

### 1. Narrow scope
We are not solving for every gig worker. We are solving one sharp problem for one sharp user group.

### 2. Mobile-first by design
This is not a web dashboard pretending to be useful for riders. The product is designed around the device they already use for work.

### 3. Hyperlocal pricing
We are not using one flat premium across the city. Risk is tied to operating conditions.

### 4. Zero-touch claims
The system is designed to reduce manual effort, which is exactly where traditional insurance fails for this audience.

### 5. Practical AI
AI is used where it changes decisions: pricing, fraud checks, and admin foresight — not as decoration.

## Scope boundaries

To keep the project disciplined and aligned with the brief, ShiftSure only covers **income loss caused by external disruptions**.

We are **not** covering:
- health insurance
- accident claims
- life insurance
- vehicle repair
- general reimbursement workflows

That boundary is important. It keeps the product coherent and stops it from becoming a vague “insurance app” with too many disconnected use cases. :contentReference[oaicite:3]{index=3}

## Team

| Member | Role | Responsibility |
|--------|------|----------------|
| Member 1 | AI / ML Engineer | Risk modeling, premium calculation, fraud detection |
| Member 2 | Backend Engineer / Team Lead | Insurance workflow, APIs, claim automation, architecture |
| Member 3 | Frontend Engineer | Rider app, UX, policy and claim flows |
| Member 4 | Integration & DevOps | External APIs, payout simulation, deployment, demo, presentation |

## Closing note

ShiftSure is our attempt to build something narrow, honest, and actually usable.

The core idea is simple: if external disruption is measurable, then short-term income protection for riders should not depend on slow, manual, traditional claims logic. It should be mobile, lightweight, and responsive to real operating conditions.

That is what we are building.
