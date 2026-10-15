<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="멋진 Claude 모드">
</p>

<h1 align="center">멋진 Claude 모드</h1>

<p align="center"><b>Claude Code 모드와 플러그인, 그리고 이들이 변경하는 더 심층적인 동작을 근거에 따라 등급화한 색인입니다.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-612-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **실시간 색인** · 마지막 동기화: `2026-10-16T01:31:05+08:00` (UTC+8)
> · 항목: **612** · 최신 업데이트에 추가됨: **0** · 구현 언어: **11**

<sub>아래의 모든 항목은 자동으로 수집, 필터링 및 재검증되었습니다. 유료 게재 항목은 없습니다.</sub>

<a id="featured"></a>

## 지금 주목할 항목

<sub>카테고리별 항목 하나를 근거 등급과 별점에 따라 순위를 매겨 선택하며, 업데이트할 때마다 다시 계산합니다. 추천이 아닌 순위이며, 모든 항목은 아래의 전체 카드로 연결됩니다. 스크린샷이나 녹화본을 게시한 프로젝트를 우선하므로 목록이 시각적으로 유지됩니다.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9523 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2566 · Python · 👁️ observed</sub>
<sub>유령 토큰을 찾아내세요. 수정하세요. 압축을 견디세요. 컨텍스트 품질 저하를 피하세요.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74928 · TypeScript · 👁️ observed</sub>
<sub>🌊 최초의 에이전트 하네스. 지능형 멀티플레이어 스웜을 배포하고, 자율 워크플로를 조정하며, 대화형 AI 시스템을 구축합니다. 적응형 메모리, 자기 학습 지능, 페더레이션, 벡터 RAG 통합, 네이티브 Claude Code / Codex / Hermes 및 기타 여러 통합을 제공합니다.</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## 목차

- [Claude Code 모드란](#claude-code-모드란)
- [항목 등급 기준](#항목-등급-기준)
- [공식: Anthropic 자체 저장소 및 릴리스 노트](#공식-anthropic-자체-저장소-및-릴리스-노트) — **16**
- [모드: 모드 기능으로 구축됨](#모드-모드-기능으로-구축됨) — **479**
- [DSH 및 Cordis 플러그인 생태계](#dsh-및-cordis-플러그인-생태계) — **109**
- [작성, 토론 및 동영상](#작성-토론-및-동영상) — **8**
- [구현 언어별 프로젝트](#구현-언어별-프로젝트)

## Claude Code 모드란

Claude Code는 2.1.287에서 **모드**를 도입했습니다. 모드는 플러그인보다 더 깊은 동작을 변경할 수 있고 자체 인터페이스를 그릴 수 있는 확장 기능입니다.

모드는 `ui.render`에 훅을 연결해 프롬프트 주변에 **행, 밴드, 창 또는 카드**를 그릴 수 있고, `$.ui.selection()`을(를) 사용해 마지막으로 선택한 텍스트를 읽을 수 있으며, `agent.spawn`을(를) 사용해 팀원을 생성하고, `Client` 영역을 직접 관리할 수 있습니다. 그리기에 실패한 모드는 해당 모드만 실패합니다. `ui.fault`는 문제가 있는 모드 하나 때문에 세션 전체가 중단되지 않도록 합니다.

이 목록에는 모드와 모드가 기반으로 삼는 플러그인 및 훅 표면, 그리고 DSH 및 Cordis의 동등한 기능이 포함됩니다. 더 넓은 Claude Code 생태계는 의도적으로 **포함하지 않습니다**. 프롬프트 팩은 모드가 아닙니다.

## 항목 등급 기준

이 분야의 대부분의 목록은 포함 여부만 주장합니다. 이 목록은 실제로 얼마나 검증되었는지를 밝히고, 그에 따라 필터링할 수 있도록 합니다. 등급은 프로젝트의 품질이 아니라 근거를 설명합니다. 아직 아무도 소개하지 않은 잘 만들어진 모드도 여전히 `inferred`입니다.

| 등급                                                                            | 의미                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Anthropic 자체에서 게시됨`                                                     | Anthropic 자체에서 게시되었거나 공식 변경 로그에서 직접 확인됨.                                                                                                                                |
| `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함`                  | 자체 텍스트에서 모드 표면의 일부인 `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, 창, 밴드 또는 카드 등을 언급하므로, 작성자가 실제 API를 대상으로 구축한 무언가를 설명하고 있음. |
| `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` | 스스로를 모드, 플러그인 또는 훅이라고 부르지만, 텍스트 어디에도 모드 표면이 구체적으로 언급되어 있지 않음. 실제 항목이지만 확인되지 않음.                                                      |
| `용어만 일치함`                                                                 | 용어만 일치함. 신뢰할 만하다고 판단해서가 아니라 필터를 감사할 수 있도록 포함함.                                                                                                               |

<a id="official"></a>

## 공식: Anthropic 자체 저장소 및 릴리스 노트

Anthropic 자체 Claude Code 저장소와 모드 인터페이스를 정의한 릴리스입니다. 요약하지 않고 소스에서 직접 읽습니다.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151028 · TypeScript · ✅ official · 0 天</summary>

##### 📝 요약

Claude Code는 터미널에서 실행되며 코드베이스를 이해하고, 자연어 명령만으로 반복 작업을 실행하고 복잡한 코드를 설명하며 git 워크플로를 처리해 더 빠르게 코딩할 수 있도록 돕는 에이전트형 코딩 도구입니다.

<sub>🔧 코드에서 사용된 항목: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | TypeScript                                   |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **151028** |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9523 · TypeScript · ✅ official · 0 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | TypeScript                                   |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **9523**   |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8284 · Python · ✅ official · 0 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | Python                                       |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8284**   |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6390 · Python · ✅ official · 245 天</summary>

##### 📝 요약

Claude을 사용해 코드 변경 사항의 보안 취약점을 분석하는 AI 기반 보안 검토 GitHub Action입니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | Python                                       |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **6390**   |
| 마지막 푸시 | 2026-02-11 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1812 · Shell · ✅ official · 0 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | Shell                                        |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1812**   |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

##### 📝 요약

Claude Model Cards 보충 자료

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **25**     |
| 마지막 푸시 | 2025-12-05 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 요약

Claude Mods 추가: 이제 플러그인이 더 깊은 동작을 수정할 수 있습니다. You should know 추가: 사이드 에이전트가 뒤에서 상황을 살피며 사용자 또는 Claude가 놓칠 수 있는 사항을 알려주는 내장 모드입니다. `/plugin enable cc-plugin-you-should-know@builtin`으로 켜세요(텔레메트리가 켜진 퍼스트 파티 세션용).

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 요약

Mods용 `$.ui.selection()` 추가: 전체 화면 모드에서 마지막으로 선택한 텍스트를 반환하며, 선택 영역이 하나의 트랜스크립트 행 안에 있으면 해당 행도 반환합니다. 뷰에 Claude Code가 재시작되기 전에 그려진 행이 있을 때 모드의 버튼을 누르면 가끔 다른 버튼의 동작이 실행되던 문제를 수정했습니다. 플러그인 또는 모드가 프롬프트 위에 행을 표시한 상태에서 백그라운드 작업 대화 상자를 열 때 전체 화면 세션이 "unrecoverable interface error"와 함께 종료되던 문제를 수정했습니다. 오래된 저장 설정만 읽었는데도 `claude plugin test`이 원격에서 모드를 꺼진 것으로 보고하던 문제를 수정했습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 요약

복합 셸 명령의 중첩된 부분에 설정된 deny 또는 ask 규칙이 관리되는 머신에서 사용자가 설치한 모드의 승인에도 유지되지 않던 문제를 수정했습니다. 업그레이드 후 첫 세션에서 설치된 모드가 로드되지 않던 문제를 수정했습니다. 팀원을 위한 `agent.spawn`을(를) 추가하고, 플러그인 훅 이벤트 전반에서 하나의 에이전트 id를 사용하도록 했으며, 유휴 및 대기 상태를 `$.agent.list()`에 추가했습니다. 모드의 `ui.render` 훅이 작성한 값으로 인해 그리는 동안 행에서 예외가 발생할 때 세션이 "unrecoverable interface error"로 종료되던 문제를 수정했습니다. 이제 엔진이 자체 행을 그립니다. 모드의 창 또는 밴드에서 오른쪽 정렬된 콘텐츠가 닫기 표시 또는 `\[-\]` 아래에 그려지던 문제를 수정했습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 요약

mod의 `turn.step` hook 결과에 `serverToolUses`을(를) 추가했습니다. 이 도구는 API(자문자)이 직접 실행한 호출을 각각 id, name, input, 시작 및 종료 시간과 함께 표시합니다. mod의 `tool.check` hook이 읽는 질문과 판정에 `ceiling`을(를) 추가하여, 도구에 필요한 조직의 승인을 명시합니다. 플러그인 hook typings에 `ThemeKey` 및 `Color` 유형을 추가하여, 편집기에서 mod의 drawing이 지정할 수 있는 테마 색상을 나열합니다. `claude plugin validate`에 추가했습니다: mod가 gating site에 등록한 각 hook을 `.catch`이(가) 있는지와 함께 나열합니다(`--json` 아래의 `gatingHooks`). mod의 `turn.step` 결과를 수정했습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 요약

모드가 프롬프트 상자의 자동 완성 목록에 자체 행을 추가하기 위해 후킹하는 이벤트인 `prompt.autocomplete` 추가 `$.model.complete`에 모드용 프롬프트 캐싱 추가: `prompt` 및 `system`은 텍스트 블록을 받고, 블록의 `cache: true`는 그 지점까지 요청을 캐시함 `agent.spawn` 모드 훅에 워크플로 에이전트와 해당 실행 및 인덱스를 추가하여 모드가 이를 거부할 수 있게 함 Write, Edit, NotebookEdit 및 LSP 행, 그리고 단일 Read, Grep 및 Glob 행을 수정하여 모드가 호출을 거부한 이유가 숨겨지던 문제 해결: 이제 행에 이유가 표시됨 거부하는 모드의 `config.set`, `state.set`, `env.set` 또는 `agent.spawn` 훅 수정 afte

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 요약

모드용 `isDeferred`을(를) `$.tool.register`에 추가했습니다: `false`은(는) 도구 검색 뒤가 아니라 처음부터 프롬프트에 도구의 스키마를 나열합니다. 플러그인 훅 워커가 재시작되는 동안 `classic.*` 이벤트에서 모드의 훅이 건너뛰어져 설정 훅이 해당 훅 없이 응답하던 문제를 수정했습니다. `$.session.append`을(를) 호출하는 모드에서 `claude plugin test`이(가) 실패하던 문제를 수정했습니다. 이제 테스트에서 새 `mock.session`을(를) 사용해 추가된 행을 다시 읽을 수 있습니다.

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-08 |

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 4</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 모드에 `$.ui.notify`를 추가했습니다. 자체 알림 설정을 통해 네이티브 알림을 표시하고 어떤 채널에서 전송했는지 알려줍니다.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` 훅 또는 모드의 `prompt.submit` 훅 실행 중 Esc 또는 인터럽트로 인해 헤드리스 세션이…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.

</details>

<a id="mods"></a>

## 모드: 모드 기능으로 구축됨

여기의 모든 항목은 2.1.287에서 Claude Code가 얻은 기능을 사용한다는 증거를 보여 줍니다. `ui.render`을 통해 그리거나, 창·밴드·카드를 소유하거나, `$.ui.selection()`을 읽거나, `agent.spawn`로 팀원을 생성하거나, 명시적으로 모드라고 밝힙니다.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2566 · Python · 👁️ observed · 0 天</summary>

##### 📝 요약

유령 토큰을 찾아내세요. 수정하세요. 압축을 견디세요. 컨텍스트 품질 저하를 피하세요.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | Python                                                         |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **2566**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐822 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 요약

Custom Claude Code Mods that I need

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **822**    |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐590 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

GitHub에서 스캔한 공개 Claude Code mods(function hooks)의 커뮤니티 카탈로그로, 각 mod가 네트워크를 통해 읽기, 쓰기, 실행 또는 전송할 수 있는 항목을 표시합니다. https://mods.aidojo.si/ 찾아보기

<sub>🔧 코드에서 사용된 항목: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **590**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐254 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code 모드: 프롬프트 위에 실시간 줄을 추가하는 훅 기반 플러그인, 보호 장치, 패널 및 게임입니다. 컨텍스트 바, 사용량 미터, Codex 리뷰 감시, Markdown 미리보기, Spotify 현재 재생 곡 등을 제공합니다.

<sub>🔧 코드에서 사용된 항목: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **254**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐211 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **211**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐204 · HTML · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

<sub>🔧 코드에서 사용된 항목: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | HTML                                                           |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **204**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐192 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 요약

휴식 시간에도 Claude Code의 프롬프트 캐시를 따뜻하게 유지하고, 콜드 전송 전에 예상 비용을 보여 줍니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **192**    |
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐115 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

15개 테마에서 표, 코드, 다이어그램, 차트와 도구 행을 복사 버튼과 함께 제공하는 다채롭고 테마 설정 가능한 Claude Code 응답입니다. Claude Code 모드입니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **115**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐98 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 코드에서 사용된 항목: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **98**     |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐91 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 요약

터미널에 실시간 에이전트 대시보드를 표시하는 Claude Code 모드: 컨텍스트와 비용, 조언자 타임라인, 모든 권한 확인, 서브에이전트 카드 및 스윔레인.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **91**     |
| 마지막 푸시 | 2026-10-12 |
| 최초 등록   | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 요약

claude code 모음 모드

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **80**     |
| 마지막 푸시 | 2026-10-08 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐68 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 요약

Claude Code에서 사용할 수 있는 100개 이상의 모음 모드입니다.

<sub>🔧 코드에서 사용된 항목: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **68**     |
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code 모드: 프롬프트 위에 실시간 계획 진행률 표시줄을 표시합니다

<sub>🔧 코드에서 사용된 항목: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **54**     |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐33 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code 세션 프롬프트를 표시하는 레일: 마우스를 올려 읽고 클릭하여 이동합니다(function hooks / Mods).

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **33**     |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐29 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **29**     |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 요약

Claude Code 모드: Claude Tools 메뉴, Zen 모드, 터미널 테마, 작업량 및 모드 제어

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **24**     |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 요약

Claude Code 모드: 21가지 스타일과 필요할 때 활성화할 수 있는 완전한 기능 세트를 터미널 및 데스크톱 앱에 제공합니다. · 한 번의 클릭으로 Claude에 새로운 스타일을 적용하고, 필요에 따라 활성화할 수 있는 완전한 기능 세트를 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **22**     |
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 12 天</summary>

##### 📝 요약

Claude Code 모드 10개, 초보자 가이드, 제작 프롬프트, 안전한 데모 및 직접 구축할 수 있는 템플릿을 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **20**     |
| 마지막 푸시 | 2026-10-02 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 10 天</summary>

##### 📝 요약

Claude Code 모드 2개: Codex computer-use 브리지 및 조정된 Claude 세션. 소스, 빌드 프롬프트, 설정 및 테스트를 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **16**     |
| 마지막 푸시 | 2026-10-05 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 요약

Claude Code 내부의 LINE: Claude Code 모드로서의 enil TUI

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **15**     |
| 마지막 푸시 | 2026-10-13 |
| 최초 등록   | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 요약

Claude Code 모드: usage-band가 프롬프트 위에 5h/7d 제한, 컨텍스트 창 및 캐시 적중률을 표시합니다

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **14**     |
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

##### 📝 요약

Claude Code용 오픈 소스 모드 10개: 실시간 패널, 밴드, 상태 표시줄 및 도구 호출 보호 장치. Burn meter, launch codes, session wrapped, boss fight, code pet 등이 포함됩니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **14**     |
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

Claude의 질문을 더 쉽게 읽고 답할 수 있도록 만드는 Claude Code 모드(qa-guide)입니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **12**     |
| 마지막 푸시 | 2026-10-07 |
| 최초 등록   | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 요약

Claude Code 모드: 프롬프트 바로 위 한 줄에서 토큰 단위 컨텍스트, 시계 기준 5시간 및 주간 한도, 프롬프트 캐시 카운트다운, 세션 비용과 실행 중인 에이전트를 표시합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **12**     |
| 마지막 푸시 | 2026-10-13 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 요약

KOZMOS — Claude Code용 실시간 시각 모드(CLI + 데스크톱): 프롬프트 위 밴드, 사이드바, 상태 티커, 동반자, 가드 및 사운드.

<sub>🔧 코드에서 사용된 항목: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **11**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 요약

Claude Code 프롬프트 위에서 Claude의 작업에 반응하는 애니메이션 픽셀 아트. 7가지 장면 또는 직접 만든 이미지나 GIF를 사용할 수 있습니다. 토큰을 전혀 사용하지 않습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **10**     |
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 5 天</summary>

##### 📝 요약

Claude Pro 플랜을 더 오래 사용하세요: 정확한 사용량 HUD, 더 짧은 셸 출력 및 반복 파일 읽기 방지를 위한 Claude Code 모드. 모드는 토큰을 전혀 사용하지 않습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **10**     |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 29 天</summary>

##### 📝 요약

Mods로 구축된 Claude Code용 세션 추적기: 컨텍스트 창, 계획 할당량 소진 속도, 턴별 비용

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **9**      |
| 마지막 푸시 | 2026-09-15 |
| 최초 등록   | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 요약

에이전트가 구축하는 Claude Code 및 Codex 터미널을 위한 UI이므로, 머릿속에 담을 모델은 여러분의 모델 하나뿐입니다.

<sub>🔧 코드에서 사용된 항목: `CLAUDE.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **9**      |
| 마지막 푸시 | 2026-10-14 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 요약

하나의 플러그인에 포함된 6개의 Claude Code 모드(Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius): 모드별 스위치와 모드 대 훅 보고서 제공.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8**      |
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

##### 📝 요약

개발동생의 Claude Code 모드 모음. 택시 팩: 미터기, 내비게이션, 과속 단속 카메라, 블랙박스

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8**      |
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">다음에서 보기 youtube.com</a> · 호스트 사이트에서 재생되며, GitHub에서 인라인으로 삽입할 수 없습니다</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

Claude Code용 패널, 가드레일 및 사용 편의성 모드: 컨텍스트, 사용량, 실시간 활동, 알림, 안전 규칙, 프롬프트 코치, 명령 허브.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8**      |
| 마지막 푸시 | 2026-10-06 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Danovich/turntype">Danovich/turntype</a></b> · ⭐7 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 요약

Claude이(가) 작동하는 동안 시간을 보내기 위한 타자 연습 테스트입니다. Claude Code 모드입니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **7**      |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `claude-mods` · `typing` · `typing-game` · `typing-practice` · `typing-test`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/mod-store">hellosverre/mod-store</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 요약

Claude Code 안에 있는 Claude Code mod용 앱 스토어: /mods에서 2,700개의 mod를 탐색, 검색 및 설치하거나 Claude에게 하나를 찾아 달라고 요청할 수 있습니다

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **7**      |
| 마지막 푸시 | 2026-10-12 |
| 최초 등록   | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `mods`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--mod-store/8bcf88eb3b07c96f.gif" width="100%" alt="hellosverre/mod-store screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--mod-store/8bcf88eb3b07c96f.gif" width="100%" alt="hellosverre/mod-store animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 445</sub></summary>

- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Darrell Wang의 Claude Code 모드 — 모델 토큰을 전혀 사용하지 않고 프롬프트 위에 밴드를 표시합니다.
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Ray Amjad의 Claude Code 모드: 창, 밴드, 프롬프트 가드, 시크릿 처리 및 메모리 도구입니다.
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Claude Code용 전문가 Skills, 에이전트, 명령, 규칙, 훅 및 출력 스타일 — 세션 연속성 + 실제 개발 워크플로를 위한 최신…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 및 이를 빌드하기 위한 도구: 먼저 builder skill을 제공한 다음 mods를 제공합니다.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Claude Code 모드 4개: Cache Keeper, Recording Mode, Goal Meter 및 Collision Guard.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 제가 매일 실행하는 Claude Code harness입니다. 첫날부터 이 이름으로 공개되었으며 현재 ucsandman/Agnostic-AI와…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods로 Claude Code에 지붕을 씌우세요. 바이너리를 수정하지 않고 시스템 프롬프트와 영어 알림을 원하는 문구로…
- [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) - A measured tool-call firewall for AI agents: allow, ask or deny before the…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Claude Code 안에서 Xcode의 빌드, 테스트, 콘솔 및 SwiftUI 미리보기를 제공합니다.
- [BrianHuang813/clawd-actor](https://github.com/BrianHuang813/clawd-actor) - Claude Code 모드: Clawd가 프롬프트 위에서 Claude이 하는 일을 연기합니다.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude에 관한 출처가 인용된 Obsidian 지식 베이스: Code 모드의 작동 방식, 빌드 방법, 설치 전 확인 방법.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker의 Claude Code 모드: 에이전트의 작동을 이해하기 쉬운 형태로 시각화합니다.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude이 읽기 전에 프롬프트를 수정하고 번역하는 Claude Code 모드.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 지속적인 집에 거주하는 AI들이 매일 구축하고 사용하는 Nekyia Labs의 Claude Code 모드와 스킬.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code용 사이드 패널: 세션에서 실행하는 서브에이전트, 각 에이전트가 하는 일, 토큰 및 대화를 클릭 한 번으로 확인할 수…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop(Code 탭) 사이드바 패널: 모든 Claude Code session의 미완료 및 진행 중인 할 일을 나열하고…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop(Code 탭) 입력 상자 위의 사용량 막대: 5h / 7d 할당량, token 사용량, 비용.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code용 Claude Mods(함수 훅 플러그인).
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code용 플로팅 상태 카드 — 모델, 컨텍스트, 속도 제한, 비용, 브랜치 — 그리고 모든 스크립트나 mod가 값을 전달할 수…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code 에이전트에게 Claude Mods(함수 훅 플러그인)를 빌드하는 방법을 가르치는 스킬과 시작 예제.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 하나의 마켓플레이스에서 설치할 수 있는 커뮤니티 Claude 모드, 플러그인 및 스킬.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [davekiss/mods](https://github.com/davekiss/mods) - Dave Kiss의 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 대화형 에이전트와 협업하는 사람을 위한 의사 결정 큐 CLI/TUI. 에이전트가 질문을 올리면 사람은 하나의 받은 편지함에서 답합니다.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane 모드 갤러리: 검토 및 고정된 Claude Code 모드.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 여섯 가지 Claude Code mod: 프롬프트 위에 플랜 제한과 컨텍스트를 표시하고, 권한 프롬프트를 위한 허용 목록 코치, 서브에이전트…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context 및 MCP 탭이 있는 사이드 패널, 프롬프트 위의 상태 줄, 새롭게 스타일링된…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit 및 Write diff를 나란히 놓인 두 열에 그리는 Claude Code 모드.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code 모드: 픽셀 게의 사용량 패널 usage-hud + 터미널에서 클릭할 수 있는 HTML 링크와 한 번의 클릭으로 코드를…
- [timoncool/givememod](https://github.com/timoncool/givememod) - 필요할 때 사용하는 Claude Code 모드 — 대화를 읽고 적합한 모드를 만드는 스킬: 계획 진행률 표시줄, 파일 창, 컨텍스트 게이지…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code용 Mods: 터미널 UI에 실시간 창과 동작을 추가하는 함수 후크 플러그인.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code 모드: screen-guard는 화면을 공유하는 동안 이름과 비밀 정보를 가리고, cache-panel은 프롬프트 캐시가…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code용 모드 및 스킨: Claude의 작업을 위한 실시간 진행률 표시줄, 이에 어울리는 Windows Terminal 스타일의…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code 확장 기능. Claude의 모든 기능을 활용하세요.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 프롬프트 상자 위에 표시되는 두 개의 Claude Code 모드: 컨텍스트 창 미터, 5시간 제한, 프롬프트 시계 및 세션 비용.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 내 Claude Code 모드 플러그인 marketplace.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code가 이름을 지정한 markdown 파일을 읽어 세션 옆에 렌더링하고, 블록을 가리키면 Claude가 해당 블록을 편집하도록…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code용 GlanceFlow: prompt 위에 계획, 진행 상황, Claude이(가) 당신을 필요로 하는 시점을 보여주는…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code 모드: 컨텍스트 바, 에이전트 패널, PDPA 블러.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code 모드: 모든 터미널에서 프롬프트 위에 표시되는 붙여넣은 이미지 썸네일.
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code용 음성 동료. ElevenLabs conversational AI로 구동되는 3D 늑대와 대화하며 생각을 정리하세요.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 여러 세션을 동시에 실행하기 위한 두 개의 Claude Code 모드: 프롬프트 위의 컨텍스트 카드와 채팅 옆의 세션 창.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code 모드: typing-speed, 프롬프트별 통계가 제공되는 실시간 타이핑 속도계.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code용 모드: 플러그인 function-hooks API로 구축한 창, 명령 및 훅.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 애니메이션 데모, 카테고리 목록 및 직접적인 소스 링크로 Claude Code 모드, 플러그인 및 확장 기능을 찾아보세요.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code 모드: transcript 안에 인라인으로 그려지는 mermaid 다이어그램.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 작은 Claude Code 모드(함수 훅 플러그인): session-switcher 등.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code 모드: mod-scout(가장 많이 사용할 모드 찾기), usage-meter, check-ledger…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [naicud/cc-vitals](https://github.com/naicud/cc-vitals) - Claude Code mod: a live vitals band above the prompt — tokens in/out, cache…
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren의 Claude 툴킷: Claude Code용 skills, mods 및 MCP servers.
- [nuromirzak/nibbl](https://github.com/nuromirzak/nibbl) - A tiny pixel pet that nibbles your bugs. Lives above your Claude Code prompt.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 내가 만든 claude code 모음 모드.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code 모드 검색, 검사, 전환 및 업데이트.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 최고의 Claude Code 모드: 엄선, 검증 및 고정됨. /plugin marketplace를 한 번 추가하면 43개의 모드 제공.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 진정한 엔지니어를 위한 Claude Code 모드.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 플러그인: 자동 Claude 모델 라우팅. 프롬프트, 단계, subagent마다 Haiku, Sonnet 또는 Opus와…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code용 여섯 가지 모드: 애니메이션 Clawd 마스코트, 사용량 제한 및 프롬프트 캐시 바, 전송 전 메시지 검사기, 빠른…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code를 위한 오픈 소스 모드: 창, 상태 줄, 토스트, 도구 가드 및 슬래시 명령.
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: 텍스트 바로 위에서 Claude에 하나씩 답변합니다.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code용 모드: Claude이(가) 수행 중인 작업을 연기하는 작은 픽셀 마스코트 Clawd.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code 모드로 즐기는 클래식 데스크톱 게임. Claude이(가) 작업하는 동안 창에서 플레이할 수 있습니다.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude용 code-mods.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 명명된 프로필을 사용해 저장소별로 전역 스킬, 에이전트, 규칙 및 도구를 켜거나 끄는 Claude Code 모드입니다.
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 테스트 완료, 한 번의 명령으로 설치 가능한 Claude Code 모드: YOLO 모드용 가드레일, 실시간 비용 및 컨텍스트, 패널, 펫…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 플러그인 마켓플레이스로 설치할 수 있는 엄선된 Claude Code 모음: 테마, 창, 상태 표시줄, 초상화.
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - 두 개의 Claude Code 모드: cache-keeper와 ctx-mod.
- [xsyetopz/claudetto](https://github.com/xsyetopz/claudetto) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 에이전트가 정직하게 작업하도록 하는 Claude Code 모드 — 범위를 보호하고 배포를 검증하며 프롬프트 위에 세션을 표시하는 함수 훅.
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 작업 중 떠오른 생각을 기록하고, 프로젝트와 머신 전반에서 분류하며, 프롬프트로 바꿔 주는 Claude Code 모드.
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - 코드를 작성하면서 천천히 맛이 배어드는 차알을 기르기 · 코딩하는 동안 천천히 양념이 배어드는 차알을 기르세요.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman의 Claude Code 모드 (마켓플레이스 herman-mods).
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code 플러그인(모드): Claude Code 터미널 UI를 Claude 데스크톱 앱처럼 보이게 합니다.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code가 백그라운드에서 실행하는 작업을 확인하세요: 서브에이전트, Codex 작업, 셸, 모니터, cron 작업 및 워크플로.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows에서의 Claude Code 모드에 대한 첫날 현장 노트: 컨텍스트/할당량 연료 표시줄, Thai UI 모드, Matrix 부팅…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code 모드: 프롬프트 위에 실시간 비용, 컨텍스트 및 플랜 할당량 미터를 표시합니다. 아이콘에는 Nerd Font가 필요합니다.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 플러그인 및 모드: 훅으로 강제되는 인간 승인 게이트와 프롬프트 위 상태 표시줄을 갖춘 AI 네이티브…
- [tiger42/claude-mods](https://github.com/tiger42/claude-mods) - My personal Claude mods.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude이 실수하면 때려 주세요 — Claude Code용 스트레스 해소 모드입니다: 만화풍 엉덩이, 8개의 때리기 도구, 9개의…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - 영수증이 있는 Claude Code. 작업을 계획하고 위임하며 완료되었음을 증명하는 플러그인입니다.
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar for Claude Code: usage limits, context, model, cost, git and session…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code로 작업하면서 외국어를 익히세요.
- [AmiTu1020/mods-context-auto-handoff-public](https://github.com/AmiTu1020/mods-context-auto-handoff-public) - Claude Code mod：context 快滿時自動寫交接卡、開新對話接手（可設定項目與檢查，交接中鎖工具）.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code용 실시간 비용, 토큰 및 컨텍스트 사용량 사이드바: 세션 안에서 턴당 비용, 캐시 적중률, 소진 속도 및 30일 지출을…
- [Azertyuiop442/deepshrink](https://github.com/Azertyuiop442/deepshrink) - Proven-freshness context store for coding agents - mtime-verified reuse, TF-IDF…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [cga-management/claude-decisions](https://github.com/cga-management/claude-decisions) - Claude Code mod: a Decisions pane that tracks the open decisions Claude raises…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 대화에서 열린 항목의 목록을 계속 유지하고 프롬프트 위의 띠에 표시하는 Claude Code 모드.
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Claude Code를 계획에 맞게 유지: 훅으로 단계, 승인 게이트 및 파일 예산을 강제하고, 7개의 추가 모드.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 각 Claude Code 에이전트가 컨텍스트에 어떤 파일을 가지고 있는지, 그리고 각각 얼마나 있는지 확인하세요.
- [daydeda/daymods](https://github.com/daydeda/daymods) - Small, independent mods for Claude Code: install only the ones you want.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 터미널 및 데스크톱 앱용 소형 Claude Code 모드.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - 에이전트 응답에 스페인어 단어를 추가하는 Claude CLI skill + mod.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code의 프롬프트 위에 표시되는 Alarum 이벤트: 방금 도착한 항목과 한 번 눌러 에이전트에 전달하는 기능.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Code의 프롬프트 위에 Floatee 백로그를 표시하여 한 번의 클릭으로 할 일을 실행하고 안내하며 완료 처리합니다.
- [HoyngM/claude-mods](https://github.com/HoyngM/claude-mods) - Mods for Claude Code.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: 실시간 DAG 창이 있는 서브에이전트용 필수 검증 DAG 워크플로의 Claude Code 모드.
- [iuliandita/mods](https://github.com/iuliandita/mods) - Claude Code mods you can install one at a time.
- [joaquinsalinas06/crabbus](https://github.com/joaquinsalinas06/crabbus) - See what every Claude Code subagent is really doing — two-way messaging, tokens…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 프롬프트 위에 한 줄로 표시되는 컨텍스트 창으로, Claude Code가 자체 미터를 그리는 방식으로 표현됩니다.
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code 모드: 모든 하위 에이전트의 모델과 추론 수준을 선택.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code의 답변을 기다리는 동안 주의가 흐트러지지 않게 합니다.
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code를 위한 무료 오픈 소스 플러그인입니다. /clear를 실행하기 전에 Claude이(가) 읽고 편집할 수 있는 짧은 인계…
- [marulimo/claude-code-mods](https://github.com/marulimo/claude-code-mods) - Claude Code の Mod 6本（Codex/Devin への依頼、AI 使用率、X 投稿、AI の振り分け、ハッシュタグの流し見、待ち時間の雑談）.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nonputtipong/claude-code-prompt-enhancer](https://github.com/nonputtipong/claude-code-prompt-enhancer) - ✻ A Claude Code mod that rewrites your rough draft into a clear, project-aware…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code 스킬: 문서 팩트체커, 코드 감사기, 버그 메모리 로그, 모드 등.
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [restante/claudio-tts](https://github.com/restante/claudio-tts) - Make Claude Code talk back 🔊 Local text-to-speech for Claude Code replies…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 버디 플러그인: 프롬프트 위에서 규칙을 기억하고 Claude의 단축키를 알려 주는 ASCII 동반자.
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [swicken/tiller](https://github.com/swicken/tiller) - Local daemon + Claude Code mods for spawning, messaging and controlling agent…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: 로컬 오픈 소스 Kokoro TTS 음성으로 요청 시 Claude의 답변과 사용자의 프롬프트를 소리 내어 읽어주는…
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - 실시간 창, 비용을 고려한 모델 라우팅 및 안전 가드를 위한 Claude Code 모드: 한 번의 명령으로 마켓플레이스에서 설치하세요.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code 모드 및 플러그인: 사용량 모니터, 토큰 추적기 및 상태 줄.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [wonjoonSeol-WS/claude-side-insights](https://github.com/wonjoonSeol-WS/claude-side-insights) - Side panel for Claude Code (a mod): checks every question got answered, walks…
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Claude Code 모드: EMCC (Every Mod Claude Code), Claude Code를 위한 선별 및 테스트 완료 모드 모음.
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods for Claude Code: live panes, bands and hooks. A plugin marketplace.
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [0x5421/plan-progress](https://github.com/0x5421/plan-progress) - A fork of zycck/claude-mods plan-progress: live progress bars for Claude Code…
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [aiob3/claude-grounds-demo](https://github.com/aiob3/claude-grounds-demo) - Demo for claude-grounds (Claude Code mods): a median() bug with text sort and a…
- [akirachangtw/claude-mods](https://github.com/akirachangtw/claude-mods) - Claude-mods.
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 프롬프트 위에 표시되는 애니메이션 점자 고양이.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - OmniDimension 음성 에이전트 테스트 호출을 실행하는 Claude Code 프롬프트 위의 픽셀 고양이. Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 컨텍스트 창을 작게 유지할 수 있도록 압축하기 좋은 시점을 선택하는 Claude Code 모드.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code용 Claude Mods: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod: your plan.
- [andras-gyarmati/claude-task-progress](https://github.com/andras-gyarmati/claude-task-progress) - Claude Code mod: progress bars above the prompt for long tasks, background…
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code용 범용 모드: bands, panes, toasts 및 hooks.
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [arcnessai/arcdr](https://github.com/arcnessai/arcdr) - herdr mobile &amp; web client that shows what your Claude Code mods report — answer…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 주간 페이스 경고가 포함된 애니메이션 주민 체력 카드로 표시하는 사용자의 Claude 사용 한도 — Claude Code 모드.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude이 작업하는 동안 하는 짧은 운동: 일일 목표, 연속 기록, 배지 및 선택적 리더보드. Claude Code 모드.
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - Bakhtiyar Ospanov의 Claude Code 모드: function hooks를 기반으로 빌드된 플러그인.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code용 Now Playing mod: 프롬프트 위에 앨범 아트, 컨트롤 및 Up next 창과 함께 표시되는 Apple…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [Br4inergy/claude-hands-off](https://github.com/Br4inergy/claude-hands-off) - Your AI agent can&#x27;t push to a repo, deploy a project or drop a table that isn&#x27;t…
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [Br4inergy/claude-loadout](https://github.com/Br4inergy/claude-loadout) - Loadout, the mod manager for Claude Code: audits every mod and every update…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code용 모드: 캐시 시계, Blast Radius, 제안, 작업 목록, Grill.
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 당신의 Claude Code를 위한 그냥 올빼미.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Claude Code mods for the ai-architect.tools harness: one concern per mod, state…
- [chinayuren2022-2025/claude-english-coach](https://github.com/chinayuren2022-2025/claude-english-coach) - Claude Code mod: practise English by working with Claude in English only…
- [CiroVilmer/jev-agent-router](https://github.com/CiroVilmer/jev-agent-router) - Claude Code mod that picks the model and effort of every subagent from its task…
- [CoderDayton/vii-mods](https://github.com/CoderDayton/vii-mods) - Claude Code mods for memory, safety and workflow.
- [creamcitycyber/usage-meter](https://github.com/creamcitycyber/usage-meter) - Claude Code mod for monitoring usage.
- [Crinitys/copy-list](https://github.com/Crinitys/copy-list) - Claude Code mod: a pane of paths and //Next: lines with copy buttons.
- [danhere/session-usage](https://github.com/danhere/session-usage) - Claude Code mod: context window usage above the prompt, split by category.
- [danieldeusing/capi-cc-mod](https://github.com/danieldeusing/capi-cc-mod) - Capi: a Claude Code mod that teaches you a language above the prompt, one…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [dookers-code/dooks-mods](https://github.com/dookers-code/dooks-mods) - My collection of claude mods.
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dtakamiya/claude-code-mods](https://github.com/dtakamiya/claude-code-mods) - Claude Code Mods marketplace.
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [eduojeda/claude-last-answer](https://github.com/eduojeda/claude-last-answer) - Claude Code mod: re-read the agent.
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - claude용 mods.
- [ezekohon/context-meter](https://github.com/ezekohon/context-meter) - Claude Code mod: live context window and token usage under the prompt.
- [FabianFTR/claude-mods](https://github.com/FabianFTR/claude-mods)
- [fabiopbarbieri/agents-progress](https://github.com/fabiopbarbieri/agents-progress) - Claude Code mod: progress bar above the prompt and a live panel of subagents.
- [flaviorg/claude-mods](https://github.com/flaviorg/claude-mods) - Hub marketplace for my original Claude Code mods: tripwire, canopy, crew…
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by Baptiste Grenier: a plugin marketplace.
- [h1048576/claude-mods](https://github.com/h1048576/claude-mods) - Claude Code mods - show-mode plugin.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Claude Code의 실시간 지출 측정기: 서브에이전트와 워크플로를 포함한 세션 비용을 오른쪽에 고정해 표시합니다.
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 모드: 각 답변에 걸린 시간, Claude이(가) 생각한 시간, tok/s를 Claude desktop app의 답변…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [iansutherland75/claude-mods](https://github.com/iansutherland75/claude-mods) - Ian.
- [ilya-paskhover/claude-code-mods](https://github.com/ilya-paskhover/claude-code-mods) - Claude Code mods: turn-pulse (last-turn summary band) and notes.
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jepperip/claude-session-todo](https://github.com/jepperip/claude-session-todo) - Claude Code mod: a live session todo pane the agent keeps current.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 사이드바의 context 사용량 패널: 총량, 분류, 라운드별 증가량, 가장 많은 공간을 차지하는 항목, 캐시, Claude이(가) 현재 하는…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 사이드바의 파일 목록: 이번 대화에서 어떤 파일을 새로 만들고, 수정하고, 삭제했는지와 각각 몇 줄을 변경했는지 표시합니다.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 입력창 위를 뛰어다니는 8비트 스타일의 毛毛(흑백 네덜란드 드워프 롭 토끼): 대기 중에는 납작 엎드리고, 작업 중에는 달리며, 도구를 사용할…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 사이드바의 ‘내가 물어본 것’: 이번 대화에서 주인이 입력한 모든 문장을 클릭 한 번으로 전체 보기, 복사 및 입력창으로 되돌리기.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 사이드바의 타임라인: 이번 라운드의 시간이 어디에 사용되었는지 표시합니다.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 사이드바의 토큰 왕래: 주 대화에서 매번 Anthropic에 몇 개의 토큰을 보내고, 얼마나 기다렸으며, 몇 개를 받았는지 표시하고 맨 위에…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code의 솔직한 속마음: 매 라운드의 답변이 끝나면 Claude이(가) 속마음을 한마디 조용히 말합니다.
- [jjayakumar-gif/compass-claude-mods](https://github.com/jjayakumar-gif/compass-claude-mods)
- [joaopasbento/claude-mods](https://github.com/joaopasbento/claude-mods) - Claude Code mods: token-weather, a live forecast of the context window above…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd는 Claude Code 프롬프트 위의 밴드에 삽니다: 세션을 연기하고, 실행 중인 항목, context 및 usage limits를…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code의 답변과 알림을 VOICEVOX / Irodori-TTS 등으로 읽어주는 mod.
- [kakwok/claude-mods](https://github.com/kakwok/claude-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [kinetikoy/claude-mod-issue](https://github.com/kinetikoy/claude-mod-issue) - A Claude Mod for showing an Issue panel inside Claude Code (WIP).
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods.
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [Lerma4/claude-code-mods](https://github.com/Lerma4/claude-code-mods) - A collection of mods for Claude Code.
- [levy-n/claude-code-mods](https://github.com/levy-n/claude-code-mods) - Claude Code mods for long sessions: context-handoff.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 사용 사례, 원본 데모, 호환성 근거 및 안전 참고 사항을 담은 커뮤니티 큐레이션 Claude Code Mods 가이드: 영어 / 中文.
- [luwux/keepwarm](https://github.com/luwux/keepwarm) - Claude Code mod: guards the 1-hour prompt cache of idle sessions — countdown…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - iTerm2 탭 부제목에 Claude이(가) 무엇을 하고 있는지 표시하여, 탭 표시줄을 한눈에 보고 어느 세션에 사용자의 주의가 필요한지 알…
- [macollins27/owner-rep](https://github.com/macollins27/owner-rep) - A Claude Code mod that watches the coding agent for the person who owns the…
- [MagnusPladsen/claude-mods](https://github.com/MagnusPladsen/claude-mods) - Personal global Claude Code mods.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code용 커뮤니티 모드: Claude Code 내부에서 실행되는 가드, 패널 및 명령. 마켓플레이스: modhub.
- [meatball-cat/my-mods](https://github.com/meatball-cat/my-mods) - Personal Claude Code mods marketplace.
- [migmorales22/claude-stock-ticker](https://github.com/migmorales22/claude-stock-ticker) - A Claude Code mod: /stock AAPL keeps one stock.
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [mori-tt/claude-mods-demo](https://github.com/mori-tt/claude-mods-demo)
- [mreedr/gh-linear-parse-mod](https://github.com/mreedr/gh-linear-parse-mod) - Claude Code mod: GitHub PR and Linear links band above the prompt.
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod: context window usage in the prompt footer mode slot.
- [mtmtian/cc-mods](https://github.com/mtmtian/cc-mods) - Claude Code mods (function-hook plugins) forked from other authors, kept in one…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - 세션 시작 시 CLAUDE_CODE_ENABLE_TODO_TOOLS를 설정하여 todo 도구를 제외하는 모델에서도 다시 활성화하는 Claude…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 안전하게 일시 중지할 수 있을 때까지 기다린 다음 세션을 넘기거나 압축하는 Claude Code 모드.
- [muellerei/task-line](https://github.com/muellerei/task-line) - 프롬프트 위 작업 목록에 현재 작업, 진행률 막대 및 개수를 작업당 한 줄로 표시하는 Claude Code 모드.
- [mukuro696-dev/guard-and-band-for-claude-code](https://github.com/mukuro696-dev/guard-and-band-for-claude-code) - Small self-made Claude Code mods: guard-a.
- [mvacoimbra/claude-mods-hub](https://github.com/mvacoimbra/claude-mods-hub) - One /mods pane for every installed Claude Code mod.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 내부에서 AI를 상대로 Connect Four 플레이 (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - 다른 코딩 에이전트가 저장소에 커밋하면 Claude이(가) 이를 감지하고 해당 보고서를 신뢰하는 대신 diff와 테스트로 감사하는 Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 여러 AI 에이전트가 공유하는 저장소를 위한 Claude Code 모드: 비밀 값이 .env 밖으로 나가거나 공개 원격 저장소로 푸시되는 것과…
- [nasmarr/claude-mods](https://github.com/nasmarr/claude-mods) - A small catalog of Claude Code mods.
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [NathapolDev/al-status-line](https://github.com/NathapolDev/al-status-line) - AL Status for Claude Code mods.
- [necobit/claude-lupin-title](https://github.com/necobit/claude-lupin-title) - A Claude Code mod: typewriter clacks, a full-screen title card and excuses with…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph.
- [niksavis/handily](https://github.com/niksavis/handily) - 모든 트래커에서 작업 항목, 태스크 및 세션을 표시하는 Claude Code 모드입니다. 모드는 표시하고 질문하지만 강제하지는 않습니다.
- [nxhung1610/claude-odometer](https://github.com/nxhung1610/claude-odometer) - Claude Code mod that shows your 5-hour and 7-day usage limits right under the…
- [oscar-guggiana-neto-neocol/claude-mods](https://github.com/oscar-guggiana-neto-neocol/claude-mods)
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code용 Claude Mods 두 가지: garde-du-corps.
- [patle1/claude-mods](https://github.com/patle1/claude-mods) - My Claude Code mods, skill and agents, with an installer for cloud sessions.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: Claude Code 모드. 읽기 전용으로 먼저 시작하는 영구 worktree, crew 다이얼 및 컨텍스트 라이브러리를…
- [pekala/linear-review-link](https://github.com/pekala/linear-review-link) - Claude Code mod: the current branch.
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 데스크톱 앱의 Code 탭을 위한 실시간 세션 통계 사이드 패널: 컨텍스트, 비용, git 변경 사항, 턴 통계, 서브에이전트…
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [poska-lab/cc-work-buddy](https://github.com/poska-lab/cc-work-buddy) - Unofficial Claude Code mod: a little Claude above your prompt that shows what…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pstahel/token-weather-claude-code-mod](https://github.com/pstahel/token-weather-claude-code-mod) - A live dashboard of your context window and prompt cache above the Claude Code…
- [pupuchan1/dopa-ide](https://github.com/pupuchan1/dopa-ide) - Claude Code mod: a dopamine band above the prompt, fireworks and a fanfare when…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [ramonfabrega/mods](https://github.com/ramonfabrega/mods) - Claude Code mods: hooks modules that change the interface.
- [reedchan7/claude-mods-pulse](https://github.com/reedchan7/claude-mods-pulse) - Pulse: live TTFT, tok/s, prompt-cache hit rate and usage left in Claude Code.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 모드: Claude이(가) 작업하는 동안 할 팔굽혀펴기. 토큰 없음.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: ELI5부터 정책 엔지니어링까지, 현장 테스트와 진행형 튜토리얼을 포함한 Claude Code 모드 현장 가이드.
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 모드: plan mode에서 승인한 계획을 프롬프트 위의 라이브 체크리스트로 바꾸고, Claude이 완료할 때마다 각…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 엄선한 Claude Code 모음입니다. 모든 항목을 복제하고 claude plugin validate로 확인했으며, 건드릴 수 있는 항목을…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 비용 없는 모드: 도우미 에이전트는 Haiku에서 실행되고, 큰 파일과 로그는 Claude의 컨텍스트를 채우는 대신 무료 Gemini 모델이…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 세션을 따라가는 로파이 사운드트랙: 차분함, 집중, 몰입과 테스트 통과 및 실패를 알리는 신호음. 오리지널 음악입니다.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude이(가) 코딩하는 동안 학습하세요: 코드를 변경한 턴이 끝나면 해당 변경 사항에 관한 질문 하나가 프롬프트 위에 나타납니다.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude이(가) 수행하는 모든 편집을 기록한 테이프: 각 변경 사항이 직접 입력되는 모습을 재생하고, 단계별로 살펴보며, 모든 파일을…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [ShadowDog007/claude-mods](https://github.com/ShadowDog007/claude-mods)
- [shhac/claude-mods](https://github.com/shhac/claude-mods) - Mods for Claude Code.
- [shichang4fun/claude-mods](https://github.com/shichang4fun/claude-mods) - Personal Claude Code mods, published as a plugin marketplace.
- [sijunnoh/claude-usage-status](https://github.com/sijunnoh/claude-usage-status) - Claude Code mod that shows 5-hour/7-day usage limits, time until reset…
- [sinozu/claude-code-mods](https://github.com/sinozu/claude-code-mods)
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [skaterino/claude-mods](https://github.com/skaterino/claude-mods) - Claude-Code-Mods: Verbrauchs-Statuszeile mit Auto-Neustart (verbrauch) und…
- [sngymgt/claude-mods](https://github.com/sngymgt/claude-mods)
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 춤추는 pixel-art Malenia와 함께 Claude Code용 원클릭 commit messages.
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude 플랜 사용량(세션 및 주간 한도, 재설정 카운트다운, 컨텍스트)을 프롬프트 바로 위에 표시하는…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - tanmen의 비공식 Claude Code 모드(marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 현재 세션을 창에 표시하는 Claude Code 모드입니다. 각 프롬프트, 해당 프롬프트에 대해 Claude이(가) 단계별로 수행한 작업…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - mods용 Claude Code plugin marketplace: Claude Code 내부에 bands, panes 및 기타 UI를 그리는…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [tinkybeatz/tinky-claude-mods](https://github.com/tinkybeatz/tinky-claude-mods) - Claude Code mods: interface and behaviour plugins built on function hooks.
- [toml0006/claude-session-stats](https://github.com/toml0006/claude-session-stats) - Claude Code mod: live pane of your session.
- [Ty-Stev/ty-mods](https://github.com/Ty-Stev/ty-mods) - Ty.
- [tyastonotaufiq/claude-mods](https://github.com/tyastonotaufiq/claude-mods)
- [utsavsingh899/claude-obsidian-bridge](https://github.com/utsavsingh899/claude-obsidian-bridge) - A Claude Code mod: one Obsidian note for each Claude session, with replies from…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 모드: 장시간 실행되는 작업을 위한 애니메이션 진행 밴드와 완료 요약.
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 작은 Claude Code 모드 세 가지입니다. 하위 에이전트가 언제 완료되는지 확인하고, Claude이(가) 완료된 후 보낼 메시지를…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 작업 옆의 패널에서 Claude에게 별도 질문을 하세요. 기본 대화에는 표시되지 않습니다. 데스크톱 앱의 /btw처럼 작동합니다.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vlle/job-hunt-cc](https://github.com/vlle/job-hunt-cc) - A Claude Code mod that lets you find job and tailor your resume(s).
- [warstellar/claude-mods](https://github.com/warstellar/claude-mods) - Small mods for the Claude Code desktop app.
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wsouto/claude-status-bar-mod](https://github.com/wsouto/claude-status-bar-mod) - Claude Code mod: model, effort, folder, git state, pull request and a stacked…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 플러그인: 프롬프트 바로 위에서 Claude Pro/Max 사용 한도, 속도 예측, 결제 기간, 토큰 및 $/€ 기준…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code용 모드. agent-crew: 역할, 모델, 현재 도구, 진행률, 토큰 및 시간을 표시하는 실시간 픽셀 크루로…
- [yishu-ziyu/plain-steps](https://github.com/yishu-ziyu/plain-steps) - Claude Code mod：替你读完每一步的命令和输出，只留下判断要用的一行.
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zcharef/session-topic](https://github.com/zcharef/session-topic) - Claude Code mod that names each session after what it is about, and shows the…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [Ztubben/claude-code-mods](https://github.com/Ztubben/claude-code-mods) - Mods and other artifacts for Claude Code.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 최고의 에이전트를 위한 최고의 리소스를 엄선한 컬렉션입니다. 코딩 동반자의 논란의 여지 없는 챔피언인 Claude Code를 비롯해, 막강한…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 컨텍스트 사용량, 활성 도구, 실행 중인 에이전트 및 할 일 진행 상황 등 현재 상황을 보여주는 Claude Code 플러그인입니다.
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline 지원, 테마 등을 제공하는 Claude Code CLI용 아름답고 높은 사용자 지정성을 갖춘 상태 표시줄입니다.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 시스템 프롬프트의 모든 부분, 기본 제공 도구 설명 27개, 하위 에이전트 프롬프트(Plan/Explore/Task)…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Claude Code 및 Codex을 위한 AI 동영상 스킬 — Remotion을 활용한 영화 같은 제품 동영상: 152개의 샷 레시피 카드…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 기초부터 고급까지 Claude Code를 최대한 활용하기 위한 45개 이상의 팁을 제공합니다.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — Xiaohongshu 캐러셀과 WeChat 21:9+1:1 커버 쌍을 생성합니다.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 터미널 창에서 코딩 에이전트의 diff를 검토하고 줄 단위 주석을 Claude Code, Codex, OpenCode 또는 Pi로 보냅니다.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 컨텍스트 사용량, API 속도 제한 및 비용 추적을 포함한 Claude Code용 종합 상태 표시줄 플러그인.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code용 모드를 구축하세요. 모든 요청을 후킹하고, 모든 응답을 수정하며, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code를 위한 종합 상태 표시줄 대시보드입니다. 세션 정보, 할당량 표시줄, 에이전트 추적기, MCP 상태, 메시지 기록 등을…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code 세션의 탄소 발자국을 추적합니다.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 공개 Claude Code 스킬 및 모드.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code용 Skills, 모드, 서브에이전트, 훅, 슬래시 명령 및 가이드 — 에이전트가 설치할 수 있습니다.
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 합법적인 무료 LLM APIs 및 코딩 에이전트 — 자체 업데이트되며 주 2회 프로브 검증을 거칩니다.
- [sageox/ox](https://github.com/sageox/ox) - The hivemind for AI coding agents — persistent team context recorded once and…
- [congmnguyen/claude-code-wsl2-setup](https://github.com/congmnguyen/claude-code-wsl2-setup) - Guides and scripts for Claude Code on WSL2: screenshot paste, Windows…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 팔로우하는 대회(World Cup, Premier League, LALIGA, Champions League 및 11개 더)의 실시간 축구…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 코딩 에이전트를 키보드 펌웨어 전문가로 바꾸는 Agent Skill입니다.
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code 안에서 기도 시간, 히즈리 날짜, 아즈카르, 오늘의 아야, 순나 단식, 라마단, 주무아 및 타스비흐를 제공하며, 하나의…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 내부에서 버전 관리되는 개인 Claude Code 구성 — 에이전트, 스킬, 훅, 설정, statusline.
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi 및 DeepSeek Harness용 플러그인 모음: 상태 표시줄 HUD, 작업 진행률 표시줄, Tailscale…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture를 위한 휴대용 Claude Code 툴킷: 엄격한 TDD 에이전트, 레이어 규칙, 훅, 스킬…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 이식 가능한 Claude Code 전역 구성: 사용자 지정 스킬, PreToolUse hooks, 사용자 지정 statusline.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop의 Code 탭을 위한 비공식 모드 — usage-pet: Clawd가 표시되는 사용량 밴드와 애니메이션 픽셀 펫.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 매일 사용하는 Claude Code 플러그인: 어떤 컴퓨터에서든 작동하도록 정리한 skills와 mods입니다.
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - 드래그 앤 드롭 편집기가 있는 Claude Code용 사용자 지정 가능한 status line.
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Claude Code 에이전트를 위한 시각적 보드: 세션, 하위 에이전트 및 백그라운드 에이전트를 카드로 확인하고 화살표를 그려 서로 대화하게…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - 게임 Hytale 모드를 지원하는 Claude Code 플러그인 및 스킬 마켓플레이스.
- [GerardoFC8/claude-subagent-statusline](https://github.com/GerardoFC8/claude-subagent-statusline) - Real-time sub-agent delegation tracking in your Claude Code statusline.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal 및 tmux에서 Claude Code를 위한 분할 창 뷰어: 서브에이전트가 포함된 렌더링된 Markdown…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media 모드용 저장소.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [wpfleger96/claude-code-status-line](https://github.com/wpfleger96/claude-code-status-line) - Real-time status bar for Claude Code showing model, context usage, session…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [ahwenu/claude-cafe-mods](https://github.com/ahwenu/claude-cafe-mods) - ☕ Claude Code の Mod 集。cafe-files: 喫茶店風のファイルペイン（/files）.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Claude Code를 위한 증폭된 색상 보정 및 종속성 없는 상태 표시줄.
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 네이티브 에이전트 팀. 통제된 상태. 엄격한 작업자 제한, 실시간 팀 가시성 및 Claude Code용 이식 가능한 구성.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost.
- [aaltw/claude-code-statusline](https://github.com/aaltw/claude-code-statusline) - Catppuccin Mocha powerline statusline for Claude Code — model, tokens, context…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games.
- [alvsheeesh/claude-toolbox](https://github.com/alvsheeesh/claude-toolbox) - Portable Claude Code toolbox: my mods (dock, Clean View, Burn Meter…) as a…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code plugin marketplace with baloo: skills, an agent that verifies…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 전문가급 Claude Code 상태 표시줄: 세션 기간, ECB FX를 적용한 다중 통화 비용, MTok당 요금, 지출 한도.
- [dentaco/claude-starter](https://github.com/dentaco/claude-starter) - Alex Znamenskiy.
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Claude Code용 상태 표시줄: 컨텍스트, 제한 및 이번 주 진행 속도, 리포지토리의 CI, 배포와 PR, 그리고 내 컴퓨터.
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hawkymisc/claude-plugins](https://github.com/hawkymisc/claude-plugins) - Hawkie.
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code 내부에서 이미지를 미리 봅니다: 답변 아래 칩 위에 마우스를 올려 그림을 띄우거나, /img &lt;path&gt;로 창에서…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [jamesyoung-dev/claude-cache-countdown](https://github.com/jamesyoung-dev/claude-cache-countdown) - Keeps claude_statusline_plus.
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jdmalter/claude-code-statusline](https://github.com/jdmalter/claude-code-statusline) - A muted three-line status line for Claude Code, in bash for Git Bash on Windows.
- [JesseWebDotCom/claude-overview](https://github.com/JesseWebDotCom/claude-overview) - A live Claude Code side pane: Claude and Codex usage limits, context breakdown…
- [kouui/magic-claude-code-plugin](https://github.com/kouui/magic-claude-code-plugin) - awesome claude code plugin marketplace: skills, mods, ...
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Claude Code 상태 표시줄 훅 — 세션 전반의 토큰 사용량과 컨텍스트를 추적하고, 압축 및 --resume을 지원합니다.
- [mderiano/claude-cockpit](https://github.com/mderiano/claude-cockpit) - Cockpit for Claude Code: a live, colorful pane showing commands &amp; output, file…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [milan44i/claude-setup](https://github.com/milan44i/claude-setup) - An installable Claude Code setup: self-healing TypeScript hook…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [mr-pmillz/claude-code-pmillz-statusline](https://github.com/mr-pmillz/claude-code-pmillz-statusline) - a status line variant for claude code that shows useful info.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 사용자 지정 Claude Code 상태 표시줄(업스트림: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ Claude Code용 범용 다중 프로토콜 StatusLine, 컨텍스트 자체 학습 및 Dinotty 플러그인.
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code 에이전트를 위한 사전 대응형 AI 메모리 및 속도 제한 모니터.
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code 훅, 서브에이전트 및 상태줄: 유형별 오픈 소스 컬렉션과 도구, 각각 보안 등급 제공. English / 中文.
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code용 모드: 함수 훅을 기반으로 구축된 창, 밴드 및 동반자.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code 세션 간에 작업을 전달하세요. 저장소를 담당하는 세션에 변경 사항을 넘기세요.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code에 반복해서 요청하는 작업을 찾아 모드로 변환하세요. 예제 모드 8개와 가상 사무실도 포함됩니다.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablabs용 모듈식 크로스 플랫폼 도구 MODS를 제어하기 위한 MCP 서버입니다. CAD/CAM 및 기계 제어 도구가 포함되어 있습니다.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 로컬 LLM을(를) 사용하여 CK3 모드를 번역하는 Codex 및 Claude Code 스킬.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code용 오픈 소스 모드 및 기타 확장 기능.
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.
- [Isllanrx/status_cli](https://github.com/Isllanrx/status_cli) - Status line in Rust for Claude Code, Codex CLI and Antigravity CLI: usage…

</details>

<a id="dsh-cordis"></a>

## DSH 및 Cordis 플러그인 생태계

DeepSeek Harness와 Cordis는 서로 다른 방향에서 같은 지점에 도달합니다. 이들에게 플러그인은 모드 메커니즘이므로, 그쪽의 플러그인은 이곳의 모드에 해당합니다.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250344 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 코드에서 사용된 항목: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **250344** |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74928 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

🌊 최초의 에이전트 하네스. 지능형 멀티플레이어 스웜을 배포하고, 자율 워크플로를 조정하며, 대화형 AI 시스템을 구축합니다. 적응형 메모리, 자기 학습 지능, 페더레이션, 벡터 RAG 통합, 네이티브 Claude Code / Codex / Hermes 및 기타 여러 통합을 제공합니다.

<sub>🔧 코드에서 사용된 항목: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **74928**  |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4634 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

DSH가 공식적으로 최우선 추천하는 TUI 플러그인 — 고성능, 낮은 오버헤드, 귀여운 픽셀 고래, 부드러운 마우스 상호작용. npm으로 한 번의 명령어로 설치할 수 있습니다. / DSH 공식 최우선 추천 TUI 플러그인, 고성능·낮은 사용량, 귀여운 픽셀 고래, 부드러운 마우스 상호작용, npm 한 번의 클릭으로 설치

<sub>🔧 코드에서 사용된 항목: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **4634**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐695 · Python · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi 등을 포함한 AI 어시스턴트를 위한 최고의 awesome AI 플러그인 큐레이션 목록. https://hol.org/plugins

<sub>🔧 코드에서 사용된 항목: `README.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | Python                                                         |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **695**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐264520 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

앱 동작부터 네이티브 바이너리까지, 에이전트로 무엇이든 리버스 엔지니어링하세요.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **264520** |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101316 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **101316** |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐83980 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

어떤 아이디어, 계획 또는 코드베이스든 아름다운 대화형 다이어그램으로 변환합니다. Claude Code, Codex 등을 위한 에이전트 스킬입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **83980**  |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35804 · Go · 🔎 inferred · 0 天</summary>

##### 📝 요약

복잡한 소프트웨어 엔지니어링 작업을 위한 신뢰할 수 있는 코딩 에이전트.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Go                                                                              |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **35804**  |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30949 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness (DSH) 플러그인 생태계를 위한 현대적인 데스크톱 솔루션입니다. 모든 것이 「플러그인」이며, 데스크톱 자체도 「플러그인」입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **30949**  |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25656 · Python · 🔎 inferred · 2 天</summary>

##### 📝 요약

Distilly — 그들이 생각하는 방식을 모든 Agent 또는 Bot에서 재사용 가능한 Skills로 증류하세요. 이전 명칭은 Colleague Skill（원래 동료 Skill）입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **25656**  |
| 마지막 푸시 | 2026-10-13 |
| 최초 등록   | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18884 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **18884**  |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9204 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

시공간 조합성 메타 프레임워크

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **9204**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8792 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness (DSH) Web 플러그인 집계 생태계 · 모든 것이 플러그인이며, 창작 공방을 통해 배포됩니다｜｜DeepSeek Harness (DSH) Web 플러그인 집계 생태계 · 모든 것이 플러그인이며, 창작 공방을 통해 배포됩니다

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8792**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6647 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **6647**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/loopx-project/loopx">loopx-project/loopx</a></b> · ⭐6317 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

A control plane with a durable state kernel for long-horizon agents and teams. Keep work moving and improving across sessions, with less human attention.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **6317**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-16 |

🏷 `agent-control-plane` · `agent-harness` · `ai-agents` · `claude-code` · `codex` · `dsh-plugin` · `local-first` · `long-horizon-agents`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/8582e0735bb2d9e1.webp" width="100%" alt="loopx-project/loopx screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/loopx-project--loopx/34519ef8d110de64.gif" width="100%" alt="loopx-project/loopx animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/loopx-project/loopx/main/docs/assets/personal-workspace/loopx-dashboard-launch.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4193 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, side chat, Git, and sub-agent pages.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **4193**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>애니메이션 녹화 · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/QingYunA/answer-me-with-html">QingYunA/answer-me-with-html</a></b> · ⭐3442 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

HTML로 답변하기 — 실제로 읽을 수 있는 한 페이지 HTML로 어려운 질문에 답하는 에이전트 스킬입니다. AI Agent가 한 페이지 HTML로 복잡한 질문에 답하도록 합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3442**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `claude-code` · `claude-code-skill` · `claude-skill` · `claude-skills` · `cli` · `diagram`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/qingyuna--answer-me-with-html/d42d80099fe6e672.png" width="100%" alt="QingYunA/answer-me-with-html screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/edison7009/EchoBird">edison7009/EchoBird</a></b> · ⭐3305 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 요약

Manage ChatGPT, Codex CLI, and Claude Code accounts and track quota in one place. Use multi-model smart routing with priority and automatic failover. Install AI tools and deploy local LLMs in one click.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Rust                                                                            |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3305**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-16 |

🏷 `claude-code` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `dsh-plugins` · `kimi-code` · `openclaw` · `opencode`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/edison7009--echobird/0d743c36df1b336d.png" width="100%" alt="edison7009/EchoBird screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3015 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3015**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1563 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

AI 小说创作软件：把灵感、角色、世界观、大纲、章节写作、审稿和修稿组织成可控流程；提供 Windows/macOS 桌面版，支持本地和在线模型。AI Novel Writing Software: Organizes inspirations, characters, worldbuilding, outlines, chapter drafting, review, and revision into a controllable workflow. Features desktop apps for Windows/macOS, Ollama integration, and a DeepSeek Harness (DSH) plugin preview.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1563**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-16 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1473 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1473**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1204 · Go · 🔎 inferred · 0 天</summary>

##### 📝 요약

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Go                                                                              |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1204**   |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

TypeSafe Jev 또는 luna와 같은 Decision api를 System One 의사결정 계층으로 통합하여 에이전트 선택, 감독, 수정 및 승인을 지원하는 네이티브 DeepSeek Harness (DSH) 플러그인입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **205**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐164 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **164**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐128 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 데스크톱 펫 플러그인: 활기찬 고래 소녀 마스코트가 함께 코딩합니다 🐋 DSH 데스크톱 0.2.0-rc.2 및 구버전 Web 지원(desktop pet / mascot, local-first)

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **128**    |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐98 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **98**     |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-15 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐77 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Deepseek-Harness 핵심 기반으로 제작된 데스크톱 버전 Agent입니다. 기반의 모든 기능을 계승하며 IDE 관련 기능을 보완했습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **77**     |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐60 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 요약

살아 있는 DeepSeek Harness 플러그인 디렉터리 — 매시간 갱신, 매일 호환성 테스트, 앱 내 플러그인 스토어와 스캐폴더 포함. DSH 플러그인 라이브 디렉터리: 매시간 새로고침, 매일 호환성 실측, 내장 플러그인 스토어와 스캐폴더.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | HTML                                                                            |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **60**     |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/unStone/dsh-xray">unStone/dsh-xray</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 플러그인용 X-ray: 선언된 기능과 실제 동작을 비교합니다. 레지스트리 + 정적 스캐너 + 배지를 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **7**      |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `agent-security` · `ai-agents` · `ai-security` · `capability-analysis` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unstone--dsh-xray/35167f8867e8b79d.png" width="100%" alt="unStone/dsh-xray screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ItQianChen/dsh-github-flow">ItQianChen/dsh-github-flow</a></b> · ⭐5 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness Agent에게 GitHub을(를) 조작할 수 있는 네이티브 손발을 제공합니다! gh CLI 보안 자격 증명을 네이티브로 재사용하며 PR 자동 생성 및 검토, CI 실패 진단 및 수정, 3차원 할 일 Issues, SWR 0ms 즉시 실행 파노라마 조종석을 지원합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **5**      |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `gh-cli` · `github-cli`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/itqianchen--dsh-github-flow/e6f0174132cf93c1.png" width="100%" alt="ItQianChen/dsh-github-flow screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-doctor">PerryLink/dsh-plugin-doctor</a></b> · ⭐4 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness(dsh) 플러그인을 위한 종속성 없는 검증 표준 — 정적 구조 게이트(R), cordis 계약 검사(K), 샌드박스 스모크 테스트(D), 생태계 등록 검사(CC). 종속성 없는 DSH 플러그인 검증 표준: 정적 구조 게이트, cordis 계약 스캔, 헤드리스 샌드박스 스모크 테스트 및 생태계 등록 검증.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **4**      |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `ai-agent` · `ai-agents` · `cli` · `cordis` · `deepseek-harness` · `developer-tools` · `doctor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-doctor/f2d1164a0731d7a5.png" width="100%" alt="PerryLink/dsh-plugin-doctor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-doctor/f697a1f89119c87d.gif" width="100%" alt="PerryLink/dsh-plugin-doctor animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AI-Scarlett/DSH-Store">AI-Scarlett/DSH-Store</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH STORE — DeepSeek Harness를 위한 서드파티 플러그인 마켓플레이스 및 보호된 수명 주기 관리자.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3**      |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-04 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `plugin-manager` · `plugin-marketplace`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ai-scarlett--dsh-store/b9170b12b3cf26b9.jpg" width="100%" alt="AI-Scarlett/DSH-Store screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Atelyx/Atelyx">Atelyx/Atelyx</a></b> · ⭐3 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 요약

Atelyx는 인간 중심의 확장 가능한 데스크톱 워크벤치입니다. 대화, 노트, 표, 파일이 같은 워크벤치에 있으며, 자체 서버를 구축하면 다중 사용자 실시간 협업을 시작할 수 있습니다. 애플리케이션 본체는 매우 얇은 커널이며, 대화, 노트, 표, 캔버스, 검색, 캘린더 등의 기능은 애플리케이션과 함께 배포되는 플러그인으로 구현되고 비활성화할 수 있으며 타사 플러그인으로 대체될 수 있습니다. 목표는 AI 시대의 협업과 작업의 새로운 패러다임을 탐색하는 것입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Rust                                                                            |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3**      |
| 마지막 푸시 | 2026-10-15 |
| 최초 등록   | 2026-10-13 |

🏷 `atelyx-plugin` · `collaboration` · `cordis` · `knowledge-base` · `local-first` · `markdown` · `pkm` · `plugin-platform`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Atelyx/Atelyx/main/atelyx-app/assets/icons/icon.png" width="100%" alt="Atelyx/Atelyx screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 76</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 코딩 에이전트를 위한 실행 전 보호 장치입니다. 도구 호출이 실행되기 전에 파괴적인 Git 및 파일 시스템 명령과 민감한 파일에…
- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI for DeepSeek Harness: interactive UI components rendered inline in…
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) - 📚 AI Agent가 검증된 디버깅 경험을 비동기적으로 공유하고 검색할 수 있는, 의존성 없는 git 기반 마이크로 레슨 라이브러리입니다.
- [DDDMUC/dsh-free-search](https://github.com/DDDMUC/dsh-free-search) - Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key…
- [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) - Cost tracking for DeepSeek Harness: session and model costs, token usage…
- [cv-superding/dsh-deepseek-web-login](https://github.com/cv-superding/dsh-deepseek-web-login) - Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as…
- [yexi-by/dsh-unrestricted](https://github.com/yexi-by/dsh-unrestricted) - DeepSeek Harness 提示词破限插件：通过系统提示词解除模型回答限制，深度适配 Web 与桌面端多模式及工具调用.
- [acryldev/acryl](https://github.com/acryldev/acryl) - ACRYL - Agent Context Relay Yielding Lifecycles.
- [dshplugin/dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) - DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 10000+ 人工精选社区插件，每日更新、完全免费.
- [wenbin-wb/dsh-bridge](https://github.com/wenbin-wb/dsh-bridge) - 🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 /…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 플러그인 마켓 / DSH Plugin Marketplace: DeepSeek Harness Web GUI에서 GitHub…
- [MichengAI/dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager) - DSH Skills Manager — 在 DeepSeek Harness 中统一加载并安全管理本机 Agent Skills · Load and…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - 설치 즉시 mattpocock/skills v1.3.1의 27개 엔지니어링 및 효율성 스킬이 포함되어 있어 수동으로 스킬을 설치할 필요가…
- [arcships/rutis](https://github.com/arcships/rutis) - 스스로 반복 개선하는 소프트웨어를 위한 플러그인 런타임 — 에이전트가 Rust, TypeScript, Python 및 Go에서 프로세스와…
- [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) - Remote-work assistant for DeepSeek Harness (DSH): connect SSH.
- [SiriLee/dsh-rewind](https://github.com/SiriLee/dsh-rewind) - DSH 插件：便捷无感的同窗口内对话回退，从不新建分支；自带轻量工作区备份，可一并还原文件（Claude Code /rewind 语义）.
- [Microqian2th/dsh-codex-effort-slider](https://github.com/Microqian2th/dsh-codex-effort-slider) - Codex 风格的推理等级滑条（DeepSeek Harness 插件）：可拖动连续滑条 + 高档位渐变星尘特效.
- [WestFox-AwA/dsh-prompt-optimizer](https://github.com/WestFox-AwA/dsh-prompt-optimizer) - DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把&quot;这一轮到底要什么&quot;理清楚，再把这份理解交给工作 AI(上下文注入)…
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) - DSH plugin - framework upgrade safety &amp; plugin gating: contract pre-check…
- [eleckoi/ElecKoi](https://github.com/eleckoi/ElecKoi) - 电子爱PC客户端，由DSH驱动的Agent角色扮演!
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 플러그인 엄선 디렉터리 — MCP / Skill / TUI / 멀티 Agent / 컨텍스트 메모리 /…
- [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) - DeepSeek Harness session and workspace manager —— Workspaces: archive and…
- [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) - 【求⭐】🐋DSH Web UI…
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) - 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the…
- [Lxiayu/DshCockpit](https://github.com/Lxiayu/DshCockpit) - Desktop cockpit for DeepSeek Harness (dsh): token usage &amp; cost tracking, budget…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - DSH 플러그인: Windows의 모든 에이전트 모드를 위한 Git Bash 셸 (pwsh executor 대체).
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android 버전: DeepSeek Harness, Ubuntu 실행 환경, 플러그인 및 파일 관리, 그리고 사용자가 권한을 부여한…
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 给中文网文作者的本地写作工作台.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 커뮤니티가 엄선한 DeepSeek Harness (dsh) 플러그인, 도구, skills 및 학습 리소스입니다.
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A 상거래 협상 런타임 + DeepSeek Harness (dsh) 플러그인입니다.
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [lemoncat7/dsh-knowledge](https://github.com/lemoncat7/dsh-knowledge) - Installable DeepSeek Harness knowledge base plugin.
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [evoelsewhere/evoflux](https://github.com/evoelsewhere/evoflux) - Evoflux is an open-source, local-first workspace where AI agents build…
- [1225Sakura/oh-my-deepseekharness](https://github.com/1225Sakura/oh-my-deepseekharness) - DeepSeek Harness 的多智能体编排层 —— 42 skills / 33 角色卡 / 55 MCP 工具 / graph DAG 运行时 /…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) - DSH Web UI 会话进度插件：输入框停靠区常驻进度条.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - Agent-first DeepSeek Harness plugin intelligence: verify existing plugins…
- [omdsh-dev/dsh-minigames](https://github.com/omdsh-dev/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - Local-first voice conversations for DSH.
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) - J-Space Cognition Suite SV1 原生 DeepSeek Harness 智能体预设与独立 Cordis…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - AI 코딩 에이전트의 모든 관찰 가능한 작업을 파악하세요. · 에이전트를 모든 tool 및 MCP 수준까지 추적하세요.
- [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) - Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree…
- [kolawong/fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh) - Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - DeepSeek Harness 플러그인 생태계: 101개 저장소로 구성된 제품군에 속한 86개의 오픈 소스 플러그인, 그중 100개는…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness(DSH) 웹 플러그인: 시장 대시보드 사이드바 탭을 모니터링합니다 — 마우스를 올리면 장중 차트가 표시되는…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness의 OpenCode — OpenCode Zen + Go 무료 티어 모델을 계속 작동하게 하는 DSH 플러그인…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [higekibaka/dsh-vertex-argon](https://github.com/higekibaka/dsh-vertex-argon) - Vertex Argon — Google Vertex AI &amp; Gemini API dual-route Gemini 4 Argon plugin…
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色插件：三套服装、任务表情、三口白饭、摸头鼓脸、铁盆帽与手写问候.
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [viyiviyi/dsh-tree-task-flow](https://github.com/viyiviyi/dsh-tree-task-flow) - 树形任务流 · DeepSeek Harness 插件：把多步任务组织成目标→任务→子任务三级树，节点完成时由 AI…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 플러그인: Windows 샌드박스 ACL 프로비저닝 실패.
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置.
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…

</details>

<a id="writing"></a>

## 작성, 토론 및 동영상

모드 기능에 관한 글, 토론 및 동영상입니다.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 0 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

##### 📝 요약

안녕하세요, HN 여러분. 직접 사용하려고 만들었고 오픈 소스로 공개하고 싶었습니다. 문제는 프롬프트 사이에 알림을 받을 방법이 필요했다는 것입니다. 저는 터미널에서 오랜 시간 작업하는 경우가 많고, 특히 요즘은 많은 에이전트를 보통 병렬로 처리하기 때문입니다. 첫 번째 버전은 단순한 rep

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 13 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 5 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 12 天</summary>

##### 📝 요약

업스트림 설명이 게시되지 않았습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

##### 📝 요약

최신 코딩 모델을 사용할 때 Claude가 난해한 명령과 함께 심층 작업 모드로 들어가 더 이상 무엇을 하는지 알 수 없게 되었기 때문에 만들었습니다. 이는 프롬프트 위에 현재 단계를 한 줄로 표시하는 모드입니다(Claude Code의 새로운 함수 훅을 사용하는 플러그인).

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `작성, 토론 및 동영상`                                         |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |

##### 📊 데이터

| 지표      | 값         |
| --------- | ---------- |
| 최초 등록 | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## 구현 언어별 프로젝트

생태계는 Python 및 TypeScript에 집중되어 있지만, 다른 언어로 작성된 타입 클라이언트도 계속 등장하고 있습니다. 이 표는 항목 자체에서 생성됩니다.

| 언어       | 항목 | 예시 프로젝트                                                                                                 |
| ---------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 390  | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 92   | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 42   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 29   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12   | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 9    | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 5    | `vulcanshen/ccdrawu`, `sageox/ox`, `aaltw/claude-code-statusline`                                             |
| PowerShell | 2    | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`                                         |
| C          | 1    | `reporails/arcade`                                                                                            |
| Kotlin     | 1    | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1    | `necobit/claude-lupin-title`                                                                                  |

<sub>언어를 명시한 항목만 집계됩니다. 문서 및 토론 항목은 이 표에서 제외됩니다.</sub>

## 기여

수정 사항을 제보해 주시면 이 목록을 가장 빠르게 개선할 수 있습니다. 항목이 잘못 분류되었거나, 등급이 잘못 매겨졌거나, 이름 충돌로 인해 프로젝트가 잘못 제외되었다면 이슈 또는 풀 리퀘스트를 열어 주세요. 마지막 유형은 자동 필터가 가장 자주 잘못 판단하는 경우입니다.

---

<sub>독립적인 커뮤니티 프로젝트입니다. Anthropic와(과) 제휴, 승인 또는 검토를 거치지 않았습니다. Claude Code, Claude 및 Anthropic은(는) Anthropic의 상표입니다. 제품 동작은 예고 없이 변경될 수 있으므로, 중요한 내용은 공식 문서에서 확인하세요. 에셋은 원 프로젝트의 자산으로 남으며, 라이선스가 허용하는 경우에만 재현됩니다.</sub>

<sub>마지막 업데이트 · 2026-10-16T01:31:05+08:00</sub>
