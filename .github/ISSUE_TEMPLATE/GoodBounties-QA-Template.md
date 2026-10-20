# Reusable QA report

Attach the report to the QA request and affected PRs.
Record observations on the tested version; use the retest section for later builds.
A recommendation becomes acceptance only when the authorized person records their decision.

- **Request and guide revision:** [Request link and checklist revision]
- **Tester / date / environment:** [Name, time, browser/device/network]
- **Exact tested commits and build or package versions:** [Full SHAs and installed artifact versions for all repositories]
- **Manual result counts:** Pass [n] · Fail [n] · Blocked [n] · Not run [n]
- **Author self-tests and automated checks:** [Versioned run links and actual outcomes]
- **Recommendation and main reason:** [Accept / hold / retest and reason]

## Case results

| Case | Result   | Observation and evidence               | Finding or next action     |
| ---- | -------- | -------------------------------------- | -------------------------- |
| [ID] | [Result] | [Observer, actual result and evidence] | [Finding / owner / action] |
| [ID] | [Result] | [Observer, actual result and evidence] | [Finding / owner / action] |
| [ID] | [Result] | [Observer, actual result and evidence] | [Finding / owner / action] |

Pass = expected outcome observed. Fail = executed and outcome differed. Blocked = a prerequisite prevented execution. Not run = not attempted. Label each observation as human or agent execution; keep author self-tests separate. Mark a case not applicable only with a reason and Lead agreement. Install failures are not failed test assertions.

## Findings and retest

- **Finding ID / case / impact:** [ID, failed case and affected user outcome]
- **Reproduction steps and expected versus actual:** [Exact steps and observed difference]
- **Redacted evidence and frequency:** [Screenshots/video/logs with sensitive data removed]
- **Triage decision / severity / owner / linked fix:** [Confirmed decision and follow-up]
- **Retest build and cases / result / evidence / tester / date:** [New versions, rerun cases, result and evidence links]
- **Remaining gaps, known limits and any requested exception:** [Required gaps and proposed next action]

Record each distinct finding separately. The agent may suggest severity; a reviewer or Lead confirms it. Preserve blocked and unrun required cases as open gaps. A Lead may record an explicit exception with reason and follow-up owner; do not turn that exception into a Pass.

## Decision record

| Decision                                    | Person and dated record                       |
| ------------------------------------------- | --------------------------------------------- |
| Tester confirms the recorded execution      | [Name, date and report link]                  |
| Reviewer confirms technical review complete | [Reviewer, date and review link]              |
| Lead accepts QA or holds with reason        | [Lead, date, version and decision link]       |
| Maintainer records final sign-off or hold   | [Maintainer, date, version and decision link] |
