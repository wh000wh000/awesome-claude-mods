<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="멋진 Claude 모드">
</p>

<h1 align="center">멋진 Claude 모드</h1>

<p align="center"><b>Claude Code 모드와 플러그인, 그리고 이들이 변경하는 더 심층적인 동작을 근거에 따라 등급화한 색인입니다.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-595-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **실시간 색인** · 마지막 동기화: `2026-10-11T16:50:06+08:00` (UTC+8)
> · 항목: **595** · 최신 업데이트에 추가됨: **0** · 구현 언어: **14**

<sub>아래의 모든 항목은 자동으로 수집, 필터링 및 재검증되었습니다. 유료 게재 항목은 없습니다.</sub>

<a id="featured"></a>

## 지금 주목할 항목

<sub>카테고리별 항목 하나를 근거 등급과 별점에 따라 순위를 매겨 선택하며, 업데이트할 때마다 다시 계산합니다. 추천이 아닌 순위이며, 모든 항목은 아래의 전체 카드로 연결됩니다. 스크린샷이나 녹화본을 게시한 프로젝트를 우선하므로 목록이 시각적으로 유지됩니다.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9472 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2534 · Python · 👁️ observed</sub>
<sub>유령 토큰을 찾으세요. 수정하세요. 압축을 견디세요. 컨텍스트 품질 저하를 피하세요.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74314 · TypeScript · 👁️ observed</sub>
<sub>🌊 최초의 에이전트 하네스. 지능형 멀티플레이어 스웜을 배포하고, 자율 워크플로를 조정하며, 대화형 AI 시스템을 구축합니다. 적응형 메모리, 자기 학습 지능, 페더레이션, 벡터 RAG 통합, 네이티브 Claude Code / Codex / Hermes 및 기타 여러 통합을 제공합니다.</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## 목차

- [Claude Code 모드란](#claude-code-모드란)
- [항목 등급 기준](#항목-등급-기준)
- [공식: Anthropic 자체 저장소 및 릴리스 노트](#공식-anthropic-자체-저장소-및-릴리스-노트) — **16**
- [모드: 모드 기능으로 구축됨](#모드-모드-기능으로-구축됨) — **465**
- [DSH 및 Cordis 플러그인 생태계](#dsh-및-cordis-플러그인-생태계) — **103**
- [작성, 토론 및 동영상](#작성-토론-및-동영상) — **11**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150110 · TypeScript · ✅ official · 0 天</summary>

##### 📝 요약

Claude Code는 터미널에서 실행되며 코드베이스를 이해하고, 자연어 명령만으로 반복 작업을 실행하고 복잡한 코드를 설명하며 git 워크플로를 처리해 더 빠르게 코딩할 수 있도록 돕는 에이전트형 코딩 도구입니다.

<sub>🔧 코드에서 사용된 항목: `feed.xml`</sub>

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | TypeScript                                   |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **150110** |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9472 · TypeScript · ✅ official · 1 天</summary>

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
| 스타        | **9472**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8247 · Python · ✅ official · 1 天</summary>

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
| 스타        | **8247**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6340 · Python · ✅ official · 241 天</summary>

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
| 스타        | **6340**   |
| 마지막 푸시 | 2026-02-11 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 1 天</summary>

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
| 스타        | **1798**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 309 天</summary>

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
| 최초 등록   | 2026-10-05 |

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
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 웹 프로필을 위한 세션 간 사용량 및 비용 관측소 — 추세/히트맵 대시보드, 모델별 피크 시간대 요금(CNY/USD), 지출 조정 기능이 포함된 공식 DeepSeek 잔액을 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트`                                    |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3**      |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `billing` · `cordis` · `cost` · `cost-estimation` · `dashboard` · `deepseek` · `deepseek-harness` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/enc-hanted--dsh-pulse/4a81f8e7c5f01f18.png" width="100%" alt="Enc-hanted/dsh-pulse screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 모드에 `$.ui.notify`를 추가했습니다. 자체 알림 설정을 통해 네이티브 알림을 표시하고 어떤 채널에서 전송했는지 알려줍니다.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` 훅 또는 모드의 `prompt.submit` 훅 실행 중 Esc 또는 인터럽트로 인해 헤드리스 세션이…
- [X-C1811/dsh-web-search-plugin](https://github.com/X-C1811/dsh-web-search-plugin) - Give your DeepSeek Harness agent more ways to search the web.

</details>

<a id="mods"></a>

## 모드: 모드 기능으로 구축됨

여기의 모든 항목은 2.1.287에서 Claude Code가 얻은 기능을 사용한다는 증거를 보여 줍니다. `ui.render`을 통해 그리거나, 창·밴드·카드를 소유하거나, `$.ui.selection()`을 읽거나, `agent.spawn`로 팀원을 생성하거나, 명시적으로 모드라고 밝힙니다.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2534 · Python · 👁️ observed · 0 天</summary>

##### 📝 요약

유령 토큰을 찾으세요. 수정하세요. 압축을 견디세요. 컨텍스트 품질 저하를 피하세요.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | Python                                                         |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **2534**   |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐479 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

GitHub에서 스캔한 공개 Claude Code mods(function hooks)의 커뮤니티 카탈로그로, 각 mod가 네트워크를 통해 읽기, 쓰기, 실행 또는 전송할 수 있는 항목을 표시합니다. https://mods.aidojo.si/ 찾아보기

<sub>🔧 코드에서 사용된 항목: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `contributing.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **479**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐183 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 요약

Claude Code mods: 프롬프트 위에 라이브 라인, 가드, 패널 및 게임을 추가하는 hooks 기반 플러그인. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing 등.

<sub>🔧 코드에서 사용된 항목: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **183**    |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐123 · TypeScript · 👁️ observed · 6 天</summary>

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
| 스타        | **123**    |
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
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 요약

웹 페이지를 위한 에이전트 네이티브 QA CLI입니다. 결정론적이며, 작성해야 할 테스트가 없고 LLM도 없습니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | HTML                                                           |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **104**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐91 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code용 스킨: 아이콘이 있는 도구 행, diff, 테이블 및 Mermaid 차트 카드, 사용량 밴드와 15개 테마. /skin으로 실시간 전환합니다.

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
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐77 · TypeScript · 👁️ observed · 2 天</summary>

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
| 스타        | **77**     |
| 마지막 푸시 | 2026-10-08 |
| 최초 등록   | 2026-10-08 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐74 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **74**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 요약

Darrell Wang의 Claude Code mods — 프롬프트 위에 밴드를 표시하며 모델 토큰은 사용하지 않습니다. 대만 주식／미국 주식 보드와 더 많은 기능이 추가될 예정입니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | HTML                                                           |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **65**     |
| 마지막 푸시 | 2026-10-05 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐65 · TypeScript · 👁️ observed · 8 天</summary>

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
| 스타        | **65**     |
| 마지막 푸시 | 2026-10-02 |
| 최초 등록   | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 요약

Claude Code를 위한 전문가 skills, agents, commands, rules, hooks 및 output styles — 실제 개발 워크플로를 위한 세션 연속성과 최신 CLI tooling

<sub>🔧 코드에서 사용된 항목: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | Shell                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **59**     |
| 마지막 푸시 | 2026-10-07 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 요약

Claude Code에서 사용할 수 있는 100개 이상의 모드 모음입니다.

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
| 스타        | **46**     |
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 요약

Claude Code 모드: 프롬프트 위에 실시간 계획 진행률 표시줄을 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **46**     |
| 마지막 푸시 | 2026-10-08 |
| 최초 등록   | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

작업하는 동안 Claude Code가 작은 만화 한 편을 만들어내는 모습을 지켜보세요.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **32**     |
| 마지막 푸시 | 2026-10-02 |
| 최초 등록   | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

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
| 스타        | **27**     |
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code를 한층 개선합니다. 라이브 조종석 패널, 공유 가능한 테마와 Claude이 수행하는 작업을 연출하는 픽셀 펫을 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **23**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

Claude Code 안에서 사용하는 Xcode의 빌드, 테스트, 콘솔 및 SwiftUI 미리보기

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **20**     |
| 마지막 푸시 | 2026-10-02 |
| 최초 등록   | 2026-10-04 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 요약

Claude Code mods: 21가지 스타일과 필요할 때 켤 수 있는 전체 기능 세트를 터미널과 데스크톱 앱에 제공합니다. · 한 번의 클릭으로 Claude에 새로운 스타일을 적용하고 필요에 따라 켤 수 있는 전체 기능 세트를 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **20**     |
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-04 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 8 天</summary>

##### 📝 요약

10가지 Claude Code 모드, 초보자 가이드, 제작 프롬프트, 안전한 데모 및 직접 제작할 수 있는 템플릿.

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
| 최초 등록   | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐12 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 요약

Claude Code 모드: usage-band가 프롬프트 위에 5시간/7일 제한, 컨텍스트 창 및 캐시 적중률을 표시합니다

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
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 요약

Claude Code 모드로 Claude의 질문을 더 쉽게 읽고 답할 수 있게 합니다(qa-guide).

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
| 마지막 푸시 | 2026-10-07 |
| 최초 등록   | 2026-10-04 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 1 天</summary>

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
| 스타        | **11**     |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

Claude Code를 위한 10개의 오픈 소스 모드: 실시간 창, 밴드, 상태 줄 및 도구 호출 보호 장치. Burn meter, launch codes, session wrapped, boss fight, code pet 등이 포함됩니다.

<sub>🔧 코드에서 사용된 항목: `swarm/README.md`</sub>

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
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 5 天</summary>

##### 📝 요약

두 가지 Claude Code 모드: Codex computer-use 브리지와 조정된 Claude 세션. 소스, 빌드 프롬프트, 설정 및 테스트.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **11**     |
| 마지막 푸시 | 2026-10-05 |
| 최초 등록   | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 요약

에이전트가 구축하는 Claude Code 및 Codex 터미널용 UI로, 머릿속에 남는 유일한 모델은 당신의 모델입니다.

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
| 마지막 푸시 | 2026-10-08 |
| 최초 등록   | 2026-10-04 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

KOZMOS — Claude Code용 실시간 시각적 모드(CLI + 데스크톱): 프롬프트 위 밴드, 사이드바, 상태 티커, 동반 기능, 보호 기능 및 사운드.

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
| 스타        | **9**      |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-09 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 25 天</summary>

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
| 스타        | **8**      |
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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 요약

하나의 플러그인에 담긴 여섯 가지 Claude Code mods(Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius), 모드별 스위치와 mods-vs-hooks 보고서 포함.

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
| 최초 등록   | 2026-10-06 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 6 天</summary>

##### 📝 요약

개발동생의 Claude Code mods 모음. 택시 팩: 미터기, 내비, 과속 단속 카메라, 블랙박스

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
| 마지막 푸시 | 2026-10-04 |
| 최초 등록   | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">다음에서 보기 youtube.com</a> · 호스트 사이트에서 재생되며, GitHub에서 인라인으로 삽입할 수 없습니다</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

입력하는 동안 Claude Code의 프롬프트 상자에 그려지는 Markdown입니다. 펜스 코드를 닫기도 전에 펜스 안의 코드가 구문 강조 카드로 바뀝니다.

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
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 요약

Claude Code mods: 像素螃蟹用量面板 usage-hud + 终端里可点的 HTML 链接和一键复制代码卡片 html-shelf

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
| 마지막 푸시 | 2026-10-08 |
| 최초 등록   | 2026-10-07 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/34d0d4bdc2328b61.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code용 Mods: 터미널 UI에 실시간 창과 동작을 추가하는 함수 후크 플러그인

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **6**      |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/helenkwok/gsd-status-mod">helenkwok/gsd-status-mod</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code용 실시간 GSD 대시보드: 로드맵, 분기 기능이 있는 에이전트 트리, 컨텍스트와 비용, 작업 스트림 및 .planning용 마크다운 리더를 제공합니다. 읽기 전용입니다.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **6**      |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agents` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `dashboard` · `gsd` · `markdown-reader` · `planning`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/4626cb34617b7732.png" width="100%" alt="helenkwok/gsd-status-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/helenkwok--gsd-status-mod/a31036b15398e820.gif" width="100%" alt="helenkwok/gsd-status-mod animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 431</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 및 이를 빌드하기 위한 도구: 먼저 builder skill을 제공한 다음 mods를 제공합니다.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 제가 매일 실행하는 Claude Code harness로, 첫날부터 이 이름으로 공개되었으며 현재 ucsandman/Agnostic-AI와…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods로 Claude Code에 지붕을 씌우세요. 바이너리를 수정하지 않고 시스템 프롬프트와 영어 알림을 원하는 문구로…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 네 가지 Claude Code 모드: Cache Keeper, Recording Mode, Goal Meter 및 Collision Guard.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker의 Claude Code Mods: 에이전트의 작동을 이해하기 쉬운 방식으로 시각화합니다.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude가 읽기 전에 프롬프트를 수정하고 번역하는 Claude Code 모드.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - A desktop-app look for Claude Code.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code용 사이드 패널: 세션에서 실행하는 서브에이전트, 각 에이전트가 하는 일, 토큰 및 대화를 클릭 한 번으로 확인할 수…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code Mods에 관한 출처 인용 Obsidian 지식 베이스: 작동 방식, 구축 방법 및 설치 전에 확인하는 방법.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop(Code 탭) 사이드바 패널: 모든 Claude Code session의 미완료 및 진행 중인 할 일을 나열하고…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs의 Claude Code mods 및 스킬, 지속적인 홈에 사는 AI들이 매일 구축하고 사용.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code 에이전트에게 Claude Mods(함수 훅 플러그인)를 구축하는 방법을 가르치는 스킬과 시작 예제.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop(Code 탭) 입력 상자 위의 사용량 막대: 5h / 7d 할당량, token 사용량, 비용.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code용 Claude Mods(function-hooks 플러그인).
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 하나의 마켓플레이스에서 설치할 수 있는 커뮤니티 Claude 모드, 플러그인 및 스킬.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods 갤러리: 검토 및 고정된 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 대화형 에이전트와 협업하는 사람을 위한 의사 결정 큐 CLI/TUI. 에이전트가 질문을 올리면 사람은 하나의 받은 편지함에서 답합니다.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE 패널 모드: 에이전트 보드, 파일 트리 및 HWP/PDF 뷰어, 시스템 상태…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code용 플로팅 상태 카드 — 모델, 컨텍스트, 속도 제한, 비용, 브랜치 — 그리고 모든 스크립트나 mod가 값을 전달할 수…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code 모드: 화면 공유 중 screen-guard가 이름과 비밀 정보를 가리고, cache-panel이 프롬프트 캐시가…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Claude의 모든 기능을 잠금 해제하세요.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context 및 MCP 탭이 있는 사이드 패널, 프롬프트 위의 상태 줄, 새롭게 스타일링된…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code용 패널, 가드레일 및 편의성 Mods: 컨텍스트, 사용량, 실시간 활동, 알림, 안전 규칙, 프롬프트 코치, 명령 허브.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 프롬프트 상자 위에 표시되는 두 개의 Claude Code 모드: 컨텍스트 창 미터, 5시간 한도, 프롬프트 시계 및 세션 비용.
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - 스스로 확인하는 당신의 계획입니다. Claude Code와 모든 MCP 호스트가 실시간으로 최신 상태를 유지하는 로컬 데스크톱 로드맵…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code가 이름을 지정한 markdown 파일을 읽어 세션 옆에 렌더링하고, 블록을 가리키면 Claude가 해당 블록을 편집하도록…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code용 음성 동료. ElevenLabs conversational AI로 구동되는 3D 늑대와 대화하며 생각을 정리하세요.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code Mods: 프롬프트별 통계가 제공되는 실시간 타이핑 속도계인 typing-speed.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code용 불꽃놀이: 모든 키 입력, 도구 호출, 커밋 및 통과한 테스트가 프롬프트 위에서 점자 불꽃놀이로 올라갑니다.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 애니메이션 데모, 카테고리 목록, 직접 소스 링크로 Claude Code mods, plugins 및 extensions를 찾아보세요.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - 대화 기록 안에 mermaid 다이어그램을 인라인으로 그리는 Claude Code 모드.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 작은 Claude Code 모드(함수 훅 플러그인): session-switcher 등.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: 모든 터미널에서 프롬프트 위에 붙여넣은 이미지 썸네일 표시.
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - See what your next Claude Code message costs: a live band above the prompt with…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code Mods: mod-scout(가장 많이 사용할 Mods 찾기), usage-meter, check-ledger…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 여러 세션을 동시에 실행하기 위한 Claude Code Mods 두 가지: 프롬프트 위의 컨텍스트 카드와 채팅 옆의 세션 패널.
- [scodge-24/workface](https://github.com/scodge-24/workface) - Claude Code mod: TUI에서 autocompaction 콘텐츠를 네이티브로 제어합니다.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Claude Pro 플랜을 더 오래 사용하세요: 정확한 사용량 HUD, 더 짧은 셸 출력, 반복 파일 읽기 방지를 위한 Claude Code…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - Claude Code용 GlanceFlow: 프롬프트 위에 계획, 진행 상황, Claude가 당신을 필요로 하는 시점을 보여주는 차분한…
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 최고의 Claude Code 모드: 엄선, 검증, 고정. /plugin 마켓플레이스 추가 1개, 모드 43개.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 플러그인: 자동 Claude 모델 라우팅. 프롬프트, 단계, subagent마다 Haiku, Sonnet 또는 Opus와…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code용 여섯 가지 모드: 애니메이션 Clawd 마스코트, 사용량 제한 및 프롬프트 캐시 바, 전송 전 메시지 검사기, 빠른…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code용 모드 마켓플레이스: 에이전트 루프 단계 디버거, git 계정 힌트, worktree 상태 표시줄 등.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code 모드: Claude 도구 메뉴, Zen 모드, 터미널 테마, 작업량 및 모드 제어.
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code용 최고의 올인원 mod pack: 사용량 제한과 context HUD, rm -rf 및 git reset --hard를…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude Code에서 YouTube Shorts를 재생하세요 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren의 Claude 툴킷: Claude Code용 skills, mods 및 MCP servers.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit 및 Write diff를 나란히 놓인 두 열에 그리는 Claude Code 모드.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code용 모드: Claude이 수행하는 작업을 연기하는 작은 픽셀 마스코트 Clawd.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code mods로 제공되는 클래식 데스크톱 게임으로, Claude가 작업하는 동안 pane에서 플레이합니다.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 플러그인 마켓플레이스로 설치할 수 있는 엄선된 Claude Code 모음: 테마, 창, 상태 표시줄, 초상화.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - 하네스 엔지니어링에 집착하는 Rustacean이 설계한 매우 주관적인 Claude Code 플러그인.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 에이전트가 정직하게 작업하도록 하는 Claude Code 모드 — 범위를 보호하고 배포를 검증하며 프롬프트 위에 세션을 표시하는 함수 훅.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - 내 Claude Code 모음으로, 디렉터리마다 모드 하나씩 포함.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - 무료 Claude Code 모드 5개: Simple Mode, Usage Tally, Context Handoff, Inbox Alerts 및…
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 A passive-aggressive water reminder for Claude Code.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - 공장에서 갓 나온 제품입니다. Claude Code 모드: 밈을 요청하고 계속 작업하세요.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code용 모드: 프롬프트 캐시 표시줄, 다음 단계, 빠른 버튼 및 변경 사항 재생 — 마켓플레이스에서 설치 가능.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 프롬프트 위 표시줄에 사용량 한도와 지출을 그려 주는 Claude Code 모드.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code 내부의 Claude Code mods용 앱 스토어: /mods로 2,700개의 mod를 탐색, 검색 및 설치하거나…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman의 Claude Code 모드 (마켓플레이스 herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code 모드: 계획을 위한 진행률 표시줄, Claude가 실행 중인 작업의 원장, 도구 출력용 토큰 마스킹.
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Claude Code를 위한 픽셀 아트 Naruto 동반자: Claude이(가) 작업하는 동안 20명의 닌자와 60개의 인술이 실행됩니다.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 여섯 가지 Claude Code mod: 프롬프트 위에 플랜 제한과 컨텍스트를 표시하고, 권한 프롬프트를 위한 허용 목록 코치, 서브에이전트…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs의 Claude Code 모드: streams는 세션의 뒤섞인 작업을 색상 코드가 적용된 스트림으로 풀어냅니다.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows에서의 Claude Code 모드에 대한 첫날 현장 노트: 컨텍스트/할당량 연료 표시줄, Thai UI 모드, Matrix 부팅…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - 내가 만들고 개인적으로 사용하는 Claude Code 모드.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code 모드: 프롬프트 위에 실시간 비용, 컨텍스트 및 플랜 할당량 미터를 표시합니다. 아이콘에는 Nerd Font가 필요합니다.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 하위 에이전트 확장, 대규모 컨텍스트 프롬프트 및 재시도 루프가 사용량 창을 소모하기 전에 보류하는 Claude Code 모드입니다.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude용 code-mods.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 명명된 프로필을 사용해 저장소별로 전역 스킬, 에이전트, 규칙 및 도구를 켜거나 끄는 Claude Code 모드입니다.
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code용 모드: 함수 훅을 기반으로 구축된 플러그인.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - 코딩 세션을 위한 영화 스타일 크레딧. 모델 호출이나 텔레메트리가 없는 네이티브 Claude Mod입니다.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 내가 만든 여러 claude code 모드.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Claude Code 안에 cliamp를 기반으로 제공되는 YouTube 플레이어(Claude Code 모드).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code 모드: 에이전트 플릿 대시보드 및 오토파일럿(local-mods 마켓플레이스).
- [vynnlee/mods](https://github.com/vynnlee/mods) - vynnlee의 Claude Code mods. mod마다 하나의 폴더, 하나의 마켓플레이스에서 설치 가능.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code로 작업하면서 외국어를 익히세요.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Claude Code Desktop에서 테마가 적용된 답변, 전체 너비 다이어그램, 컨텍스트와 한도를 한눈에 확인.
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - 에이전트가 Java을 작성할 때 Alibaba Java 규정(p3c)을 위반한 코드는 디스크에 저장되지 않습니다.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code용 실시간 비용, 토큰, 컨텍스트 사용량 사이드바: 세션 내에서 턴별 비용, 캐시 적중률, burn rate, 30일…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code 모드: 모든 세션에서 Claude이(가) 제안하는 후속 작업 백로그와 각 세션의 다단계 작업을 위한 작업 목록.
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Claude Code용 Counter-Strike 1.6 무전 호출 - 배포 시 &quot;Fire in the hole&quot;, 긴 턴이 끝나면.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 안의 인터넷 라디오: cliamp 사이드바, 미니 플레이어, 즐겨찾기, 탐색, 집중 모드 및 Claude용 라디오 도구.
- [BuddyLim/claude-code-mod-lens](https://github.com/BuddyLim/claude-code-mod-lens) - A Claude Code mod: a code review pane with the changed files, inline…
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - 제품 개발 작업을 위한 Herdr 설정 + Claude Code 모드.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code용 macOS notch 대시보드: 사용량 제한, 열린 세션, 작업 진행률, 프롬프트 캐시 카운트다운 및 할 일 — 다섯…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude가 요리 중입니다. 팀과 채팅하세요. 친구들이 온라인에서 Claude Code 세션 바로 옆에 있습니다.
- [crebot51/jack-mods](https://github.com/crebot51/jack-mods) - jack 的 Claude Code mods 合集.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Claude Code 모드: Claude이 작업하는 동안 유휴 게임에서 픽셀 아트 Modsters를 잡습니다.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - All-in-one Claude Code mod: a live HUD, safety guards.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 각 Claude Code 에이전트가 컨텍스트에 어떤 파일을 가지고 있는지, 그리고 각각 얼마나 있는지 확인하세요.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code용 모드: 플러그인 function-hooks API로 구축한 패널, 명령 및 훅.
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 냉정함을 유지하세요. Claude Code 사용일을 위한 온도계입니다.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Prompt cache, context and plan limits at a glance for Claude Code, in the…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code 모드: 세션이 열거나 푸시하는 GitHub PR의 실시간 패널 — CI, 리뷰, 충돌, 병합 — 모든 세션이 하나의…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 터미널 및 데스크톱 앱용 소형 Claude Code 모드.
- [ewxgwy1987/claude-code-mods](https://github.com/ewxgwy1987/claude-code-mods) - 각각 별도의 저장소로 제공되는 Claude Code mod 모음: usage-meter, progress-board, session-toc.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod: 작업, 서브에이전트, 워크플로 실행, 목표 및 도구 호출을 위한 진행 창을 제공하며 막대, 타임스탬프 및 남은…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod: 전체 세션의 클릭 가능한 타임스탬프 목차로, 주제와 범주별로 그룹화됩니다.
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod: 프롬프트 위에 플랜 속도 제한, 컨텍스트 사용량, 세션 비용 및 작업별 토큰을 색상 막대로 표시합니다.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - 에이전트 응답에 스페인어 단어를 추가하는 Claude CLI skill + mod.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 이를 Person of Interest의 The Machine처럼 재스타일링하는 Claude Code 모드입니다.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - 적절한 순간(커밋 후, 테스트가 통과된 후, 프롬프트 캐시가 만료되기 전)에 compact하거나 Claude이(가) 요청할 때…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: Claude Code mod for mandatory, verified DAG workflows of…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code를 위한 오픈 소스 모드: 창, 상태 줄, 토스트, 도구 가드 및 슬래시 명령.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 각 서브에이전트와 해당 에이전트가 건드리는 파일, 그리고 세션의 사용량과 비용을 위한 패널을 제공하는 Claude Code 모드입니다.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: 세션 상태, 실시간 Spec Kit 진행 상황 및 사용량 창 거버넌스.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 프롬프트 위에 한 줄로 표시되는 컨텍스트 창으로, Claude Code가 자체 미터를 그리는 방식으로 표현됩니다.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code가 백그라운드에서 실행하는 항목을 확인하세요: 서브에이전트, Codex 작업, 셸, 모니터, cron 작업 및…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code를 위한 무료 오픈 소스 플러그인입니다. /clear를 실행하기 전에 Claude이(가) 읽고 편집할 수 있는 짧은 인계…
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 세션의 GitHub개 풀 리퀘스트를 트랜스크립트 옆 창에 표시하는 Claude 모드: 설명을 프롬프트 상자에 인용하고 검사 및 리뷰 상태를…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude Code 도구 호출용 디버거인 Claude DevTools.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code 스킬: 문서 팩트체커, 코드 감사기, 버그 메모리 로그, 모드 등.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod: today.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod: 답변의 클릭 가능한 경로 — 폴더를 클릭하면 Finder에서 열고, 파일 이름을 클릭하면 파일을 엽니다.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 버디 플러그인: 프롬프트 위에서 규칙을 기억하고 Claude의 단축키를 알려 주는 ASCII 동반자.
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - 에이전트별 도구 가시성을 위한 Claude Code 플러그인 — 각 루프마다 서브에이전트, 스킬, MCP 및 내장 도구를 숨기고 거부합니다.
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code 모드: Claude Code를 위한 보안 계층 — 비밀 정보 삭제, 신뢰할 수 없는 콘텐츠 알림, MCP 도구 포이즈닝…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 플러그인 및 모드: 훅으로 강제되는 인간 승인 게이트와 프롬프트 위 상태 표시줄을 갖춘 AI 네이티브…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods 컬렉션 | 클로드 코드 모드 모음집.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 플러그인(모드): 여러 Claude 계정 간 전환, 상태 밴드에서 사용량 제한 확인, 터미널 패널에서 에이전트…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 테스트 완료, 한 번의 명령으로 설치 가능한 Claude Code 모드: YOLO 모드용 가드레일, 실시간 비용 및 컨텍스트, 패널, 펫…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: 로컬 오픈 소스 Kokoro TTS 음성으로 요청 시 Claude의 답변과 사용자의 프롬프트를 소리 내어 읽어주는…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude이 실수하면 때려 주세요 — Claude Code를 위한 스트레스 해소용 mod: 만화풍 엉덩이, 8개 때리기, 9개 엉덩이…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Claude Code 사용량을 최대 두 배까지 늘리세요. 각 프롬프트와 서브에이전트에 적절한 추론 작업량을 선택하는 플러그인입니다.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - 실시간 창, 비용을 고려한 모델 라우팅 및 안전 가드를 위한 Claude Code 모드: 한 번의 명령으로 마켓플레이스에서 설치하세요.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code 모드 및 플러그인: 사용량 모니터, 토큰 추적기 및 상태 줄.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - 세 가지 무료 Claude Code 모드: 도구 결과에서 .env 값을 숨기고, 원격 장비의 메모리를 확인하며, Markdown 초안을…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods. touch-map: Claude가 나열, 읽기, 편집 또는 생성한 파일을 트리와 activity map으로…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - 읽지 않은 에이전트 메시지를 쉬운 영어로 요약하는 Claude Code mod.
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Claude Code용 모드: 라이브 패널, 밴드 및 훅. 플러그인 마켓플레이스입니다.
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - 0xnicholasy의 모드(agents-office, todo-list, collapse-tools)를 위한 Claude Code 플러그인…
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code 모드 + cheap-executor 드라이버: 하나의 Claude 세션을 리드로 사용하고, MiniMax Code를…
- [AdamCaviness/cache-magic](https://github.com/AdamCaviness/cache-magic) - 내장 idleCompaction의 유연한 대안을 제공하는 Claude Code mod입니다.
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code 모드: 사용량 진행률 표시줄(context, 5h, 7d)과 프롬프트 위의 간결한 버튼.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code mods: session stat cards above the prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 프롬프트 위에 표시되는 애니메이션 점자 고양이.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code 모드: 저렴한 작업은 하위 Claude Code를 통해 GLM/Kimi로 라우팅하고, 중요한 작업은 구독에서 유지합니다.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - OmniDimension 음성 에이전트 테스트 호출을 실행하는 Claude Code 프롬프트 위의 픽셀 고양이. Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 컨텍스트 창을 작게 유지할 수 있도록 압축하기 좋은 시점을 선택하는 Claude Code 모드.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code용 Claude Mods: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider의 Claude Code 플러그인 마켓플레이스.
- [androidZzT/claude-trading-mods](https://github.com/androidZzT/claude-trading-mods) - 터미널에서 시장을 확인하기 위한 Claude Code mods: 추세와 업종 히트맵이 있는 A股/港股/美股 패널.
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Claude Code용 모드.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - 코드가 변경될 때마다 LGTM Lines 우주선이 지나갑니다 — Claude Code 모드.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 애니메이션 주민 체력 카드로 표시되는 Claude 사용 한도 — Claude Code 모드.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 팀용 Claude Code 모드(the ather marketplace).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude이 작업하는 동안 하는 짧은 운동: 일일 목표, 연속 기록, 배지 및 선택적 리더보드. Claude Code 모드.
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Plan, task and agent progress beside the Claude Code prompt — a Claude Code mod.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code용 사용량 보드: 모델별 지출(오늘, 이번 주, 이번 달, 전체 기간) 및 주간 한도 예측.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code 모드: 프롬프트 위에 실시간 컨텍스트 창 분석을 표시합니다.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code용 Now Playing mod: 프롬프트 위에 앨범 아트, 컨트롤 및 Up next 창과 함께 표시되는 Apple…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - 여러 세션을 동시에 실행하기 위한 Claude Code 모드 5개: 플릿 보드, PR-to-production 추적기, 규칙 트립와이어…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Berko 영상의 Claude Code 모드 팩: Mask, View, Guard, Saving, Chime 및 커뮤니티 모드를 하나의…
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Claude Code mods: 사용량 밴드, 채팅 참가자 목록, /cube, /handoff, 프롬프트 정리.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code용 모드: 캐시 시계, Blast Radius, 제안, 작업 목록, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 당신의 Claude Code를 위한 그냥 올빼미.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 한 줄짜리 Claude Code 밴드(캐시 카운트다운, 컨텍스트, 제한, 다음 작업)와 7개의 커뮤니티 모드를 하나의 플러그인으로 설치하며…
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoom이 포함된 오리지널 Doom 엔진으로, Claude Code 안에서 플레이 가능. Mac Apple Silicon 알파 버전.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - A Claude Code mod that keeps a running list of the open items in a conversation…
- [d3nims/d3nim-claude-mods](https://github.com/d3nims/d3nim-claude-mods) - d3nim 팀 전용 Claude Code mods (usage-meter: 파란 불꽃 / 테리어 사용량 밴드).
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [danielgillaspia01-web/claude-mods](https://github.com/danielgillaspia01-web/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code 안에 사는 Tamagotchi: 부화하고, Claude이(가) 작성한 코드를 먹고, 버그를 남기며, 여덟 종류의 성체 중…
- [Demo-0416/claude-code-mods](https://github.com/Demo-0416/claude-code-mods) - Mods for Claude Code, as a plugin marketplace.
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - 터미널과 데스크톱 앱에서 각 프롬프트와 답변의 시간을 표시하는 Claude Code 모드.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 함수 훅으로 작성된 Claude Code 모드와 이를 제공하는 마켓플레이스. dash: 한 패널에 있는 세션의 대시보드.
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code 모드 및 디자인 시스템: crab-crew와 Crab Crew 디자인 시스템.
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - 플러그인 마켓플레이스로 공유하는 나의 Claude Code 모드.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code 모드: guard가 도구 호출을 차단한 후 동일한 대상을 향하는 인식된 우회 경로를 중지하고 Claude에게 사용자에게…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code 모드: 실제 출력에서 읽은 진행률과 예상 완료 시간을 하나의 뷰에서 백그라운드 작업으로 표시합니다.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code 모드: 팀원, 이름이 지정된 하위 에이전트 및 다른 세션의 메시지를 위한 통합 받은편지함으로, 읽지 않은 메시지 수와…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code 모드: 샌드박스 차단을 설명하고 반복되는 차단을 검토 및 실행 취소 가능한 설정 변경으로 전환합니다.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 이봐요, 음소거했어요! diff를 버리고 장단을 끊으세요. 더 이상 편집도, 크레딧 차감도 없습니다.
- [elec100-design/claude-mods](https://github.com/elec100-design/claude-mods) - claude용 mods.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktop 앱과 터미널에서 프롬프트 위 밴드로 구독 사용량(5h / 7d)을 표시하는 Claude Code mod.
- [evasuka/work-meter](https://github.com/evasuka/work-meter) - Claude Code mod: 입력 상자 위에 작업 진행 상황과 계정 잔여 할당량을 표시합니다.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Claude Code를 위한 모션 디자인 mods: 모델, effort, context, 사용량 제한, 작업 진행률, subagents 및…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - 프롬프트 위에서 병렬 브랜치와 worktree를 실시간으로 보여 주는 레이더: 어떤 항목이 깔끔하게 병합되는지, 어떤 항목이 충돌하는지, 어떤…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - A Claude Code mod for capturing thoughts mid-work, triaging them across…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code를 위한 모드 및 스킨: Claude의 작업을 위한 실시간 진행률 표시줄, 이에 맞는 Windows Terminal…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code 모드(function-hook 플러그인): 컨텍스트 밴드, 미해결 항목, 체크포인트 감시, 검토 게이트, 에이전트 비용.
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - 7가지 Claude Code 모드: savvy-progress, skins, filetree, cache-tax, blast-radius…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code 답변의 모든 코드 블록에서 Ctrl+클릭으로 링크 복사.
- [Gersom/claude-mod-agent-radar](https://github.com/Gersom/claude-mod-agent-radar) - Mod de Claude Code: monitor visual y pasivo del agente principal y sus…
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Claude Code 모드: 프롬프트 캐시가 따뜻한지 차가운지 표시하는 패널.
- [Gersom/claude-mod-usage-meter](https://github.com/Gersom/claude-mod-usage-meter) - Mod de Claude Code: recuadro con el % de contexto y de los límites de 5 horas y…
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Claude Code용 Mods: usage-meter 같은 hook 플러그인.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code용 Evangelion 스타일 사이드바: 컨텍스트, 할당량, 활동, PR, 하드웨어, 세션 및 forge 패널.
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code mods: context-bar-plus (context bar, quota, subagent modes).
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Static supply-chain auditor for Claude Code Mods — local, offline, stdlib-only.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code용 독일어 모드: 컨텍스트/캐시 알림, 안내가 포함된 미해결 항목, 상태 표시줄.
- [helenkwok/open-links](https://github.com/helenkwok/open-links) - Claude Code mod: file paths in Claude.
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Claude Code 패널의 테스트 결과: Claude 자체 테스트 실행의 실패, 세부 정보 및 실행 기록.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 모드: 각 답변에 걸린 시간, Claude이(가) 생각한 시간, tok/s를 Claude desktop app의 답변…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod: waits out the 5-hour usage limit and sends &quot;continue&quot; for you.
- [icedevil2001/claude-mods](https://github.com/icedevil2001/claude-mods) - Small mods for Claude Code, starting with auto-continue after the 5-hour limit.
- [im-adarsh/claude-mods](https://github.com/im-adarsh/claude-mods)
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - A cockpit above your Claude Code prompt. The duck reads the gauges.
- [itaym967/rtl-questions](https://github.com/itaym967/rtl-questions) - Claude Code mod: shows Claude.
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 작은 Claude Code 모드: 컨텍스트 및 plan 사용량 게이지, prompt-cache 미터 및 살펴볼 항목을 표시하는 패널.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - 내 claude 모드를 보관하는 곳입니다.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 사이드바의 context 사용량 패널: 총량, 분류, 라운드별 증가량, 가장 많은 공간을 차지하는 항목, 캐시, Claude이(가) 현재 하는…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 사이드바의 파일 목록: 이번 대화에서 어떤 파일을 새로 만들고, 수정하고, 삭제했는지와 각각 몇 줄을 변경했는지 표시합니다.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 입력창 위를 뛰어다니는 8비트 스타일의 毛毛(흑백 네덜란드 드워프 롭 토끼): 대기 중에는 납작 엎드리고, 작업 중에는 달리며, 도구를 사용할…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 사이드바의 ‘내가 물어본 것’: 이번 대화에서 주인이 입력한 모든 문장을 클릭 한 번으로 전체 보기, 복사 및 입력창으로 되돌리기.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 사이드바의 타임라인: 이번 라운드의 시간이 어디에 사용되었는지 표시합니다.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 사이드바의 토큰 왕래: 주 대화에서 매번 Anthropic에 몇 개의 토큰을 보내고, 얼마나 기다렸으며, 몇 개를 받았는지 표시하고 맨 위에…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code의 솔직한 속마음: 매 라운드의 답변이 끝나면 Claude이(가) 속마음을 한마디 조용히 말합니다.
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 새 슬래시 명령 및 사이드 패널과 같은 Claude Code용 작은 모드.
- [jjjung0921/claude-mods](https://github.com/jjjung0921/claude-mods)
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - 6개 언어로 제공되는 Claude Code 모드(function hook)에 대한 비공식 커뮤니티 가이드와 검색 가능한 모드 디렉터리.
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Claude Code용 모드 카탈로그.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Claude Code가 작업하는 동안 내부에서 플레이할 수 있는 멀티플레이어 게임.
- [juampymdd/claude-code-model-picker](https://github.com/juampymdd/claude-code-model-picker) - Claude Code mod: 프롬프트 위의 막대에서 다음 요청에 사용할 모델과 버전을 선택합니다.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd는 Claude Code 프롬프트 위의 밴드에 삽니다: 세션을 연기하고, 실행 중인 항목, context 및 usage limits를…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code의 응답과 알림을 VOICEVOX / Irodori-TTS 등으로 읽어주는 mod.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Code 세션 간의 대화를 읽고 참여하는 Claude Mod (/crosstalk).
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod: 프롬프트 위에서 서브에이전트를 픽셀 Claude 마스코트로 실행합니다.
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - 편의성/사용성 개선 Claude 모드.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 두 가지 Claude Code 모드: 채팅 옆의 파일 패널인 folio와 상태 줄이 포함된 터미널 세션 재스타일링인 tint.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop용 실시간 작업 HUD: Claude이(가) 작업하는 동안 프롬프트 위에 표시되는 스트립과, 한 번 클릭하면…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Don&#x27;t let your attention wander off while waiting for Claude Code&#x27;s answer.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Angel(Vremia)의 프로젝트를 위한 Claude Code 모드.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 사용 사례, 원본 데모, 호환성 근거 및 안전 참고 사항을 담은 커뮤니티 큐레이션 Claude Code Mods 가이드: 영어 / 中文.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - iTerm2 탭 부제목에 Claude이(가) 무엇을 하고 있는지 표시하여, 탭 표시줄을 한눈에 보고 어느 세션에 사용자의 주의가 필요한지 알…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Code 프롬프트 위의 복슬복슬한 검은 고양이입니다. 눈을 깜빡이고, 가르랑거리며, 낮잠을 자고, 사용자의 컨텍스트를 걱정합니다.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - 하나의 플러그인 마켓플레이스(marcel-mods)에 모은 Marcel의 Claude Code 모드.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 전환 가능한 권한 프로필을 제공하는 Claude Code 모드: 안전한 기본 프로필, 켜고 끌 수 있는 이름 지정 프로필, 그리고 그 외 모든…
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code를 위한 커뮤니티 모드: Claude Code 내부에서 실행되는 가드, 패널 및 명령. 마켓플레이스: modhub.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Side pane for Claude Code: files Claude wrote, terminal splits, git repo status…
- [minhdevtree/claude-lens](https://github.com/minhdevtree/claude-lens) - A Claude Code mod that shows images, SVGs and PDF pages where they appear…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code를 위한 조용한 사이드 패널: 이 세션이 수행 중인 작업, 계획, 에이전트 및 다른 모든 세션.
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Code가 접어 숨기는 내용을 다시 표시합니다: Claude이(가) 읽은 파일, 실행한 명령, 각 턴에서 수행한 작업.
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod: context window usage in the prompt footer mode slot.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - 세션 시작 시 CLAUDE_CODE_ENABLE_TODO_TOOLS를 설정하여 todo 도구를 제외하는 모델에서도 다시 활성화하는 Claude…
- [muellerei/task-line](https://github.com/muellerei/task-line) - 프롬프트 위 작업 목록에 현재 작업, 진행률 막대 및 개수를 작업당 한 줄로 표시하는 Claude Code 모드.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 내부에서 AI를 상대로 Connect Four 플레이 (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - 다른 코딩 에이전트가 저장소에 커밋하면 Claude이(가) 이를 감지하고 해당 보고서를 신뢰하는 대신 diff와 테스트로 감사하는 Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 여러 AI 에이전트가 공유하는 저장소를 위한 Claude Code 모드: 비밀 값이 .env 밖으로 나가거나 공개 원격 저장소로 푸시되는 것과…
- [niksavis/handily](https://github.com/niksavis/handily) - 모든 트래커에서 작업 항목, 태스크 및 세션을 표시하는 Claude Code Mods입니다. Mods는 표시하고 질문할 뿐, 강제하지 않습니다.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code에서 SQL을 위한 가드레일: DB CLI를 통해 Claude이 DELETE, WHERE 없는 UPDATE, DROP…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows 및 CJK를 우선하는 하나의 모드: 모든 터미널에서 붙여넣은 이미지 및 텍스트 미리보기, CJK에 맞는…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Claude Code용 Chime: Claude이(가) 완료하거나, 사용자의 입력을 필요로 하거나, 오류가 발생할 때 소리를 냅니다.
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: 이미지 썸네일 및 상태 표시줄.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [Open01277/claude-mods](https://github.com/Open01277/claude-mods)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 무엇을 해 주는지에 따라 정렬한 최고의 Claude Code Mods. 직접 확인하여 각 항목을 한 줄로 정리했습니다.
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - 위험한 셸 명령(rm -rf, git reset --hard, 강제 push, 마이그레이션, 전역 설치, curl | sh…)을 보류하고…
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code용 Claude Mods 두 가지: garde-du-corps.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - 에이전트 텔레메트리, 타임라인 대시보드, mmrun 교차 모델 검토 및 worktree 위임, 워크플로 가드와 영구 진행 추적 기능을 갖춘…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Claude Code에 욕을 하면 만화 속 손이 되받아칩니다. 메시지는 전송되지 않으며, 정중한 버전이 프롬프트 상자로 돌아갑니다.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code 모드: usage-both가 프롬프트 위에 5시간 및 주간 사용량을 표시합니다.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 데스크톱 앱의 Code 탭을 위한 실시간 세션 통계 사이드 패널: 컨텍스트, 비용, git 변경 사항, 턴 통계, 하위 에이전트…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - 내 Claude Desktop 설정을 위한 다양한 모드와 스킬.
- [pokhriyal-anmol/claude-token-window](https://github.com/pokhriyal-anmol/claude-token-window) - Claude Code mod: input and output tokens in your current 5-hour window, per…
- [pompeitech/affreschi](https://github.com/pompeitech/affreschi) - Claude Code mods for the pompeitech interface, themed on the Vesuvius design…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code용 모드: safety-guard는 파괴적인 명령과 비밀 파일 접근을 차단하고, notify-router는 규칙 기반…
- [qazwsx1121/Claude-Code-mods](https://github.com/qazwsx1121/Claude-Code-mods)
- [rafagomes/claude-code-mods](https://github.com/rafagomes/claude-code-mods) - Claude Code용 Mods: 세션 내부에서 실행되는 함수 훅 플러그인(english-coach, toolbar).
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod: 실시간 주식 티커, /quote 패널, 가격 알림, 시장 밴드, 모델이 호출할 수 있는 quote 도구.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod: 프롬프트 위 한 줄에 SSH 호스트, RAM 및 5h/7d 사용량 제한 표시.
- [RexWei1016/claude-project-progress](https://github.com/RexWei1016/claude-project-progress) - Claude Code mod: project progress pane from GitHub milestones, issues, PRs and…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 모드: Claude이(가) 작업하는 동안 할 팔굽혀펴기. 토큰 없음.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [Rsclub22/claude-mods](https://github.com/Rsclub22/claude-mods)
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - 작업을 다른 AI 모델(OpenAI, Gemini, DeepSeek, 로컬 모델)로 전달하고 해당 모델의 기능과 비용을 비교하는 Claude…
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Claude Code용 모드 상점: GitHub에서 모드를 스크랩하고, 미리 보고, 마켓플레이스를 호스팅합니다.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 모드: plan mode에서 승인한 계획을 프롬프트 위의 라이브 체크리스트로 바꾸고, Claude이 완료할 때마다 각…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 엄선한 Claude Code 모음입니다. 모든 항목을 복제하고 claude plugin validate로 확인했으며, 건드릴 수 있는 항목을…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 비용 없는 모드: 도우미 에이전트는 Haiku에서 실행되고, 큰 파일과 로그는 Claude의 컨텍스트를 채우는 대신 무료 Gemini 모델이…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 세션을 따라가는 로파이 사운드트랙: 차분함, 집중, 몰입과 테스트 통과 및 실패를 알리는 신호음. 오리지널 음악입니다.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude이(가) 코딩하는 동안 학습하세요: 코드를 변경한 턴이 끝나면 해당 변경 사항에 관한 질문 하나가 프롬프트 위에 나타납니다.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude이(가) 수행하는 모든 편집을 기록한 테이프: 각 변경 사항이 직접 입력되는 모습을 재생하고, 단계별로 살펴보며, 모든 파일을…
- [samaphp/session-links](https://github.com/samaphp/session-links) - 세션에서 언급한 모든 링크를 프롬프트 위 한 줄에 표시합니다. Claude Code 모드.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code 함수 훅 최소 데모: prompt 위의 실시간 token/비용 패널, 클릭 가능한 버튼, 독립적으로 그리는 스레드…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: an unofficial Avengers fan mod for Claude Code.
- [shawnbotha/claude-mods](https://github.com/shawnbotha/claude-mods) - 다양한 Claude mods.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - 프롬프트 위에 컨텍스트, 증가량, 할당량, 캐시, 네이티브 비용 및 에이전트 활동과 세션 세부 정보를 표시하는 Claude Code…
- [shezis/claude-api-cost-compare](https://github.com/shezis/claude-api-cost-compare) - Claude Code mod: see what your session would cost on the Claude, OpenAI…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code mod: route simple turns and subagents to cheaper models, never…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code용 아늑한 RPG HUD 모드.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 춤추는 pixel-art Malenia와 함께 Claude Code용 원클릭 commit messages.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude Code 모드.
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - 개인용 Claude Code 모드.
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Claude Code용 플러그인.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Claude Code용 모드: delete-guard (프로젝트 폴더 외부에서 삭제하려면 승인이 필요함).
- [takiguchi-yu/claude-mods](https://github.com/takiguchi-yu/claude-mods) - 로컬에서 사용하는 Claude Code mod 모음.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Claude Code 모드: 프롬프트 바로 위에서 Claude 요금제 사용량(세션 + 주간 한도, 재설정 카운트다운, 컨텍스트)을 확인합니다.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code 모드: 모든 서브에이전트를 위한 실시간 크루 패널(모델, 작업량, 단계, 컨텍스트, 비용, 시간), 프롬프트 위의 작업…
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 현재 세션을 창에 표시하는 Claude Code 모드입니다. 각 프롬프트, 해당 프롬프트에 대해 Claude이(가) 단계별로 수행한 작업…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - mods용 Claude Code plugin marketplace: Claude Code 내부에 bands, panes 및 기타 UI를 그리는…
- [timoncool/givememod](https://github.com/timoncool/givememod) - 필요할 때 제공되는 Claude Code 모드 — 대화를 읽고 적합한 모드를 만드는 스킬입니다: 계획 진행률 표시줄, 파일 패널, 컨텍스트…
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - 다른 도구가 읽을 수 있는 파일에 사용자의 Claude 사용량 제한을 기록하는 Claude Code 모드.
- [Tora29/my-claude-tools](https://github.com/Tora29/my-claude-tools) - Claude Mods を管理するrepo.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Customizations for Claude Code.
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code 모드: 서브에이전트와 해당 에이전트가 사용하는 파일을 추적하는 밴드 및 패널.
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - 엄선된 Claude Code 모드 카탈로그로, 각 모드에는 직접 빌드할 수 있는 복사-붙여넣기 프롬프트가 포함되어 있습니다.
- [ulttla/claude-mod-repo](https://github.com/ulttla/claude-mod-repo) - Claude Code mods: a context and plan-limit meter above the prompt, and auto-pin…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code 모드: 프롬프트 위 한 줄에 5h/7d 할당량, 컨텍스트 창, 프롬프트 캐시 잔여 시간 및 세션 비용을 표시하고…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 모드: 장시간 실행되는 작업을 위한 애니메이션 진행 밴드와 완료 요약.
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 작은 Claude Code 모드 세 가지입니다. 하위 에이전트가 언제 완료되는지 확인하고, Claude이(가) 완료된 후 보낼 메시지를…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Shrinks big screenshots before Claude reads them, so long sessions last longer…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 작업 옆의 패널에서 Claude에게 별도 질문을 하세요. 기본 대화에는 표시되지 않습니다. 데스크톱 앱의 /btw처럼 작동합니다.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - 한 단계 설치와 포르투갈어 동영상 가이드를 제공하는 Claude Code 모드 마켓플레이스.
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Code의 속도 제한 카운트다운 및 소모 속도 예측.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Claude Code용 Roblox Studio 안전 레이어: RemoteEvent 감사, 실행 취소, Team Create 보호 및…
- [Wasif-ZA/claude-mods](https://github.com/Wasif-ZA/claude-mods)
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Claude Code용 작지만 편리한 모드.
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code plugin: your Claude Pro/Max usage limits with a pace forecast…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code용 모드. agent-crew: 역할, 모델, 현재 도구, 진행률, 토큰 및 시간을 표시하는 실시간 픽셀 크루로…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Inline and display LaTeX math, plus optional TikZ figures, in Claude.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code용 실시간 작업 보드입니다. 빌드 전에 계획을 세우고, 사이드 패널에서 모든 작업, 상태, 시간, 하위 에이전트 및 검사를…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code mod that reports which files Claude changed and why, live subagent…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - 데스크톱과 터미널에서 Claude Code 프롬프트 위에 항상 표시되는 밴드: 컨텍스트 사용량 및 속도 제한 창.
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - 개인용 Claude Code 모드(플러그인 마켓플레이스).
- [zwbao/zebra-mod](https://github.com/zwbao/zebra-mod) - zebra-mod: a Claude Code mod that turns Claude Code into a rare-disease…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 최고의 에이전트를 위한 최고의 리소스를 엄선한 컬렉션입니다. 코딩 동반자의 논란의 여지 없는 챔피언인 Claude Code를 비롯해, 막강한…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 컨텍스트 사용량, 활성 도구, 실행 중인 에이전트 및 할 일 진행 상황 등 현재 상황을 보여주는 Claude Code 플러그인입니다.
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline 지원, 테마 등을 제공하는 Claude Code CLI용 아름답고 높은 사용자 지정성을 갖춘 상태 표시줄입니다.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 시스템 프롬프트의 모든 부분, 기본 제공 도구 설명 27개, 하위 에이전트 프롬프트(Plan/Explore/Task)…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 기초부터 고급까지 Claude Code를 최대한 활용하기 위한 45개 이상의 팁을 제공합니다.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — Xiaohongshu 캐러셀 및 WeChat 21:9+1:1 커버 쌍 생성.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code를 위한 아름다운 vim 스타일 powerline.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 터미널 창에서 코딩 에이전트의 diff를 검토하고 줄 단위 주석을 Claude Code, Codex, OpenCode 또는 Pi로 보냅니다.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 컨텍스트 사용량, API 속도 제한 및 비용 추적을 포함한 Claude Code용 종합 상태 표시줄 플러그인.
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code 및 Codex 로컬 token 추적 — 상태 표시줄(Codex 업계 최초의 가짜 statusline), GitHub…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code용 mods 빌드: 모든 요청을 hook하고, 모든 응답을 수정하며, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code용 종합 statusline 대시보드 — 세션 정보, quota bars, 에이전트 추적기, MCP 상태, 메시지 기록 등.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code 세션의 탄소 발자국 추적.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejun이 만든 Claude Code용 미적인 statusline.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 공개 Claude Code 스킬 및 모드.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code용 Skills, mods, subagents, hooks, slash commands 및 guides — 에이전트가…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 법적으로 무료인 LLM APIs 및 코딩 에이전트 — 주 2회 자동 업데이트 및 프로브 검증.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code 세션용 터미널 상태 표시줄.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 팔로우하는 대회(World Cup, Premier League, LALIGA, Champions League 및 11개 더)의 실시간 축구…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Claude Code를 Windows 및 macOS에서 사용하기 위한 로컬 제어 플레인: 고정 엔드포인트 뒤에서 한 번의 클릭으로 LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 코딩 에이전트를 키보드 펌웨어 전문가로 바꾸는 Agent Skill입니다.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 내부에서 버전 관리되는 개인 Claude Code 구성 — 에이전트, 스킬, 훅, 설정, statusline.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code 안에서 기도 시간, 히즈리 날짜, 아즈카르, 오늘의 아야, 순나 단식, 라마단, 주무아 및 타스비흐를 제공하며, 하나의…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Claude Code용 세션 인식 상태 표시줄입니다. kaomoji 얼굴이 대화 기록을 읽고 세션 전반의 상태를 설명합니다.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — 연구 주제, 추적 가능한 지식 카드, 재사용 가능한 AI 토론을 위한 DeepSeek…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Two-line truecolor statusline for Claude Code.
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture를 위한 휴대용 Claude Code 툴킷: 엄격한 TDD 에이전트, 계층 규칙, hooks…
- [essedev/relay](https://github.com/essedev/relay) - Native macOS terminal for running many coding agents in parallel.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi 및 DeepSeek Harness용 플러그인 모음: 상태 표시줄 HUD, 작업 진행률 표시줄, Tailscale…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 이식 가능한 Claude Code 전역 구성: 사용자 지정 스킬, PreToolUse 후크 및 사용자 지정 상태 표시줄.
- [JMOKSZ/dsh-lark-bridge](https://github.com/JMOKSZ/dsh-lark-bridge) - Feishu (Lark) entry point for DeepSeek Harness: drive dsh agents from a Feishu…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 매일 사용하는 Claude Code 플러그인: 어떤 컴퓨터에서든 작동하도록 정리한 skills와 mods입니다.
- [34823/tg-pane](https://github.com/34823/tg-pane) - Claude Code 안의 Telegram: 패널에서 채팅과 채널을 읽고, 읽지 않은 게시물의 AI 요약을 받습니다.
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code.
- [codextde/godmode-bot](https://github.com/codextde/godmode-bot) - An AI teammate you can trust to get work done — Claude Code + browser-use + a…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Hytale Mods를 지원하기 위한 Claude Code 플러그인 및 스킬 마켓플레이스.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code를 위한 토큰 거버넌스: 상위 모델이 지시하고, 실행은 충분히 적합한 가장 저렴한 수단으로 전달됩니다.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal 및 tmux에서 Claude Code를 위한 분할 패널 뷰어: subagents, 실시간 git diffs…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code를 위한 실시간 워크플로 단계 상태 표시줄(Plan → Exec → Verify → Done)이며 모델이 자동으로…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop의 Code 탭을 위한 비공식 모드 — usage-pet: Clawd와 애니메이션 픽셀 펫이 있는 사용량 밴드.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media 모드용 저장소.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude Code 및 Codex 토큰 비용 절감: 조회와 테스트 실행을 더 저렴한 모델로 라우팅하고, 문서를 간결한 Markdown으로…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code를 위한 간단하고 유용한 상태 표시줄 설정.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code용 사용량 제한 알림: 세션(5h) 및 주간 제한에 대한 macOS 알림, 앱 내 경고 및 상태 표시줄 백분율.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux, WSL, Windows 및 macOS용으로 구성 가능한 Claude Code 상태줄, 프롬프트 타이밍, 서브에이전트 행, 터미널…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code를 위한 빠른 Rust 상태 줄 — payload 우선, 캐시된 git, 약 10ms 렌더링.
- [JohnnyTh/claude-status-bar](https://github.com/JohnnyTh/claude-status-bar) - 컨텍스트 바, 토큰 sparkline 및 비용 추적기가 있는 Claude Code statusline.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Catppuccin 캡슐 스타일 사이드 패널에 컨텍스트 분석, 캐시 적중, 속도 제한 예측, 비용 및 활동을 표시하는 Claude Code용…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code용 상태 줄 및 토큰 줄: 컨텍스트, 속도 표시가 포함된 5시간 및 주간 사용량, 활동, git 및 비용을 표시합니다.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - macOS, Linux, Windows 전반에서 모델, 컨텍스트, 제한, git 정보, 세션 시간을 포함한 Claude Code의 주요 상태…
- [Ma1achy/claude-statusline](https://github.com/Ma1achy/claude-statusline) - Claude Code를 위한 친근하고 모든 것을 조정할 수 있는 status line — truecolor 바, ~80개 테마, 하나의…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 다중 행 Claude Code 상태 줄: 비용, 컨텍스트 %, git 및 활성 계정 — 가격과 컨텍스트 창이 자동으로 업데이트됩니다.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code를 위한 유용한 정보가 있는 Statusline.
- [Screddyice/claude-code-harness](https://github.com/Screddyice/claude-code-harness) - 여러 회사의 Claude Code 작업 공간을 구성하기 위한 시작 템플릿: 정리된 CLAUDE.md 템플릿, SessionStart 훅, 상태…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 네이티브 에이전트 팀. 통제된 방식으로. Claude Code를 위한 엄격한 작업자 한도, 실시간 팀 가시성 및 이식 가능한 구성.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code용 사용자 지정 상태 표시줄 — 사용률, 컨텍스트 크기, 비용 및 타이머가 표시되는 컨텍스트 막대.
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code를 위한 깔끔하고 유용한 상태 표시줄 — 프로젝트, git 상태, 모델, 세션 시간, 컨텍스트 사용량 및 속도 제한을…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - baloo가 포함된 Claude Code 플러그인 마켓플레이스: 스킬, 프로젝트의 결정 사항·지침·검사를 기준으로 변경 사항을 검증하는…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 전문가급 Claude Code statusline: 세션 시간, ECB FX를 적용한 다중 통화 비용, MTok당 요금 및 지출 한도를…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code용 구독 인식 상태 표시줄.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code용 풍부한 터미널 상태 줄 — Bun + TypeScript, 런타임 의존성 없음.
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - 트랜스크립트에 Mermaid 다이어그램을 아름답게 렌더링하는 Claude Code 플러그인: 모든 터미널에서 색상이 적용된 Unicode…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude Code용 도구, 스킬 및 에이전트 — 모델, 브랜치, PR, 컨텍스트 크기, 프롬프트 캐시 잔여 시간 및 비용을 표시하는 상태…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 커스텀 상태줄 (모델, effort, 컨텍스트, 캐시, 사용량 한도).
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code 플러그인: 푸터 오른쪽 아래에서 남은 Claude 5시간 사용 한도를 항상 확인 — 더 이상 /usage를 사용할 필요…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code의 실제 DeepSeek API 지출: DeepSeek 피크/오프피크 요금으로 세션 트랜스크립트의 가격을 다시 계산하고…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Preview images inside Claude Code: hover a chip under a reply to pop the…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - WSL을 사용하는 Windows의 Claude Code 및 Claude Desktop용 모드: 프롬프트 위에 Docker 및 성능을 표시합니다.
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - 에이전트 패널 행이 있는 Claude Code 상태 표시줄.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Claude의 할 일을 Fizzy.do에 동기화하여 팀이 실시간으로 확인할 수 있게 하고, 작업을 영구 카드로 전환해 협업을 강화하고 진행…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - 내가 만들었고 공유하고 싶은 Claude Code 스킬, 모드 및 기타 애드온 모음입니다.
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - 컨텍스트, git 상태, 비용 및 속도 제한을 보여주는 상세한 색상 코드 상태 표시줄을 Claude Code에 표시합니다.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code 설정 메뉴, 상태 표시줄 및 config.
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - 직접 만든, 케이지 프리 claude 플러그인, 스킬, 모드 등.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 환경 설치 프로그램: skills, statusline, hooks, permissions 및 선택적…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - HUD-style status line for Claude Code — network health, TPS, context, quotas…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude이(가) 수행하는 작업을 이해하기 위한 Claude Code 플러그인 및 모드: 읽기 쉬운 답변 형식과 실시간 세션…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - 활성 작업, 대기 중인 권한 및 경과 시간에 대한 실시간 표시기로 macOS 메뉴 막대에서 Claude Code 상태를 모니터링합니다.
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Claude Code용 다채로운 다중 행 상태 표시줄(할당량 막대, 컨텍스트, 서브에이전트 패널).
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows용 Claude Code 상태줄(PowerShell): 사용량 막대, 속도 경고가 포함된 5시간/7일 재설정 카운트다운, 자동 줄…
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Claude Code용 Bearings and Glossary 모드.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - 공유 컴포넌트 키트, 플레이그라운드 및 Storybook이 포함된 Claude Code 설정 및 모드.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 포터블 Claude Code 설정: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop (macOS) mod: click-to-jump session notifications…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - 터미널용 경량 종속성 없는 상태줄 대시보드로 Claude Code 컨텍스트 사용량, 세션 비용 및 속도 제한 재설정을 추적합니다.
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - A hands-on, verified deep-dive into Claude Code — CLAUDE.md, subagents, skills…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code용 실시간 비용 추적 및 세션 모니터링 상태 줄.
- [wmkeza/claude-plugins](https://github.com/wmkeza/claude-plugins) - wmkeza.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Cordis / DeepSeek Harness 플러그인 — 에이전트는 인라인 대화 카드에서 사람에게 비밀을 요청하며, 값 자체는 절대 받지…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - 컨텍스트 깊이, 세션 간 속도 제한, 저장소별 git 상태 및 worktree를 표시하는 3행 Claude Code 상태 표시줄.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code 에이전트를 위한 사전 대응형 AI 메모리 및 속도 제한 모니터.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code 훅, 서브에이전트 및 상태줄: 유형별 오픈 소스 컬렉션과 도구, 각각 보안 등급 제공. English / 中文.
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code 상태 표시줄 — 유휴 상태에서도 계속 실시간으로 유지되는 Claude/Codex 사용량 게이지, 컨텍스트 %, 진행 중인…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code 상태 표시줄을 위한 시각적 빌더입니다. 브라우저에서 터미널 하단의 막대를 디자인한 다음 명령 하나를 붙여 넣어 설치하세요.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 실시간 토큰 사용량과 예상 에너지 소비량을 표시하는 Claude Code 상태 표시줄.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - 함수 후크를 기반으로 창, 밴드 및 버디를 구축한 Claude Code용 Mods.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code 세션 간에 작업 전달. 리포지토리를 담당하는 세션에 변경 사항을 넘김.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablab용 모듈식 크로스 플랫폼 도구인 MODS를 제어하기 위한 MCP 서버의 기능입니다.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 로컬 LLM을(를) 사용하여 CK3 Mods를 번역하기 위한 Codex 및 Claude Code 스킬.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code를 위한 오픈 소스 모드 및 기타 확장 기능.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code statusline: CCometixLine beauty + Claude HUD functionality.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code에 반복해서 요청하는 작업을 찾아 모드로 변환. 예제 모드 8개와 가상 사무실도 포함.
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## DSH 및 Cordis 플러그인 생태계

DeepSeek Harness와 Cordis는 서로 다른 방향에서 같은 지점에 도달합니다. 이들에게 플러그인은 모드 메커니즘이므로, 그쪽의 플러그인은 이곳의 모드에 해당합니다.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74314 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **74314**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100464 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

🎨 최고의 DeepSeek Harness 디자인 플러그인. 오픈 소스 Claude Design 대안. 🖥️ 로컬 우선 데스크톱 앱. 🖼️ 코딩 에이전트가 디자인 엔진이 됩니다: 프로토타입, 랜딩 페이지, 대시보드, 슬라이드, 이미지 및 동영상 — 실제 파일, HTML/PDF/PPTX/MP4 내보내기. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode 및 BYOK를 통한 20개 이상의 CLI.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **100464** |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81801 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **81801**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐81717 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **81717**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35757 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **35757**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30392 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **30392**  |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25484 · Python · 🔎 inferred · 18 天</summary>

##### 📝 요약

Distilly — 이들이 사고하는 방식을 모든 Agent 또는 Bot에서 재사용 가능한 Skills로 추출합니다. 이전 명칭은 Colleague Skill（原同事 Skill）입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **25484**  |
| 마지막 푸시 | 2026-09-22 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8616 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness (DSH) Web 플러그인 집계 생태계 · 모든 것이 플러그인이며 크리에이티브 워크숍을 통해 배포됩니다｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8616**   |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anbeime/skill">anbeime/skill</a></b> · ⭐7821 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使用！同时自动抓取GitHub上万个Skills项目，按分类、更新时间、Star数量整理。The most comprehensive and frequently updated AI Agent skill library, featuring curated skill packs across document processing, content creation, programming, machine learning, automated workflows, and many more domains.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **7821**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-skills` · `claude-skills` · `codex` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `finance-skill`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anbeime/skill/main/images/wechat-qr.jpg" width="100%" alt="anbeime/skill screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4456 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **4456**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4278 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH가 공식적으로 가장 추천하는 TUI 플러그인 — 고성능, 낮은 오버헤드, 귀여운 픽셀 고래, 매끄러운 마우스 상호작용. npm으로 한 줄 설치. / DSH 공식 최우선 추천 TUI 플러그인, 고성능·낮은 사용량, 귀여운 픽셀 고래, 매끄러운 마우스 상호작용, npm 한 번에 설치

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **4278**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1788 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

QR 코드 또는 봇 자격 증명을 통해 IM 봇을 DeepSeek Harness에 연결합니다(飞书, 微信, 钉钉, 企业微信, QQ, Slack, Telegram, Discord 및 WhatsApp 지원). QR 코드 또는 자격 증명을 통해 IM 봇을 DeepSeek Harness에 연결합니다(9개 채널).

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1788**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1557 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

跨设备的开源Agent工作台

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1557**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1397 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

AI 소설 창작 소프트웨어: 영감, 캐릭터, 세계관, 개요, 장면 집필, 검토 및 수정을 제어 가능한 워크플로로 구성합니다. Windows/macOS 데스크톱 버전을 제공하며 로컬 및 온라인 모델을 지원합니다. AI 소설 집필 소프트웨어: 영감, 캐릭터, 세계관, 개요, 장면 초안 작성, 검토 및 수정을 제어 가능한 워크플로로 구성합니다. Windows/macOS용 데스크톱 앱, Ollama 통합 및 DeepSeek Harness(DSH) 플러그인 미리보기를 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1397**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1169 · Go · 🔎 inferred · 0 天</summary>

##### 📝 요약

이미 디스크에 저장된 세션 기록을 바탕으로 구축된 Claude Code, Codex, Cursor 및 38개 이상의 코딩 에이전트를 위한 메모리입니다. 로컬 검색, MCP 및 훅을 지원하며, LLM 없이 단 하나의 Go 바이너리로 제공됩니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Go                                                                              |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1169**   |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/LivXue/dsh-plugin-shop">LivXue/dsh-plugin-shop</a></b> · ⭐1009 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

The most comprehensive DeepSeek Harness plugin market — refreshed daily, sourced across the Internet, reviewed before publishing.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1009**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐703 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness (dsh) Windows 데스크톱 클라이언트 - Node.js + dsh CLI 번들 포함, 원클릭 실행

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **703**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐351 · Go · 🔎 inferred · 0 天</summary>

##### 📝 요약

당신의 지능을 오케스트레이션합니다. 모든 빌더. 모든 팀. 모든 에이전트. 모두를 위해.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Go                                                                              |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **351**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhaoolee/notes">zhaoolee/notes</a></b> · ⭐277 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

开源版锤子便签，复刻锤科美学，一键Docker私有化部署，支持skill调用，支持dsh plugin，支持多租户，一键生成公众号格式，支持导出便签为图片

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **277**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `dsh-plugin` · `notes` · `smartisan`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhaoolee--notes/ea0ae0d3af2430c1.png" width="100%" alt="zhaoolee/notes screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhaoolee--notes/a1cc07be6396cb67.gif" width="100%" alt="zhaoolee/notes animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

ACRYL - Agent Context Relay Yielding Lifecycles. 하나의 영구 워크스페이스, 하나의 표준 컨텍스트, 모든 코딩 에이전트.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **255**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

에이전트 선택, 감독, 수정 및 승인을 위한 System One 의사결정 계층으로 luna 같은 TypeSafe Jev 또는 Decision api를 통합하는 네이티브 DeepSeek Harness (DSH) 플러그인.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **203**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐170 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Time-shifting task delegation for DeepSeek Harness (dsh): plan tasks at leisure, they run unattended off-peak, come back to a report. Human-adjudicated, desktop + web.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **170**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

미리 볼 수 있는 프리셋 간 세션 마이그레이션을 위한 DeepSeek Harness 플러그인입니다. 고정 스키마 핸드오프가 상태, 소스 모델의 의도 및 해결되지 않은 이미지를 보존하며, 원본 세션은 변경하지 않습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **165**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐132 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **132**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mexiaosqwq/dsh-web-mobile">mexiaosqwq/dsh-web-mobile</a></b> · ⭐131 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH Web UI 移动端适配：窄屏好用，宽屏适用

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **131**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-ui` · `plugin` · `responsive` · `web-ui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mexiaosqwq--dsh-web-mobile/0edd0e3313404adf.jpg" width="100%" alt="mexiaosqwq/dsh-web-mobile screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐129 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness용 Claude Code 데스크톱 테마｜DeepSeek Harness 웹 GUI를 위해 만든 Claude Code 데스크톱 테마

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **129**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐123 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

에이전트가 애플리케이션 및 네이티브 코드, GPU 커널과 추론 스택의 핫스팟을 추적하고 프로파일링하며 줄여 나가는 데 도움이 되는 런타임 증거입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **123**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSK-build/DSHBox">WSK-build/DSHBox</a></b> · ⭐104 · Kotlin · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSHBox —  Run DeepSeek Harness locally on Android phones and tablets. It integrates and coordinates DSH, PRoot, WebView, Debian and Node.js, together with a terminal, a file manager and other tools, into a personal AI workbench. No root access, and no separate Termux installation.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Kotlin                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **104**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `android` · `android-agent` · `android-app` · `android-application` · `deepseek-harness` · `deepseek-harness-android` · `deepseek-harness-mobile` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsk-build--dshbox/560dbaccacdf1506.png" width="100%" alt="WSK-build/DSHBox screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐73 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

공용 네트워크에서 DeepSeek Harness(dsh web)를 원격 제어하세요. 설치하면 전용 암호화 주소가 제공되어 외부에서도 휴대폰으로 원격 접속할 수 있습니다. 동일한 LAN/WiFi가 필요 없고, 인트라넷 침투도 필요 없으며, 직접 서비스를 구축할 수도 있습니다. 어디서든 DeepSeek Harness(dsh web)를 원격 제어하세요 — 암호화된 공용 URL, LAN 불필요.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **73**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mobile` · `mobile-web` · `pwa`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://cdn.jsdelivr.net/gh/mrRisega/dsh-remote@main/image/phone-mirror.png" width="100%" alt="mrRisega/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐63 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **63**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/NoNameLeGo/dsh-catppuccin-theme">NoNameLeGo/dsh-catppuccin-theme</a></b> · ⭐58 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **58**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `catppuccin` · `deepseek-harness` · `dsh` · `dsh-plugin` · `theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nonamelego--dsh-catppuccin-theme/c3d2472cfd609d68.png" width="100%" alt="NoNameLeGo/dsh-catppuccin-theme screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐58 · HTML · 🔎 inferred · 0 天</summary>

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
| 스타        | **58**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Contexera/dsh-agent-team">Contexera/dsh-agent-team</a></b> · ⭐57 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

dsh-agent-team은 재설정되지 않는 DeepSeek Harness 에이전트를 제공합니다. 각자 고유한 메모리, 노트 및 스킬을 가진 영구 Members가 세션, 롤오버 및 재시작 이후에도 유지됩니다. 방향은 사용자가 설정하고, 에이전트는 Channels와 Tasks를 통해 협력합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **57**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-orchestration` · `agent-team` · `ai-agents` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `multi-agent`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/contexera--dsh-agent-team/25f8cc5a2a3231a3.png" width="100%" alt="Contexera/dsh-agent-team screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

AI Coding Agent를 위한 작업 인식형 워크스페이스 컨텍스트 검색 및 수명 주기 추적: 현재 작업과 가장 관련성 높은 문서, 코드 및 미디어를 찾아 정리하고 지속적으로 추적합니다. 완전 로컬, 모델 호출 0회, 네트워크 0회.  AI 코딩 에이전트를 위한 작업 인식형 워크스페이스 컨텍스트 검색 및 수명 주기 추적입니다. 현재 작업과 가장 관련성 높은 워크스페이스 컨텍스트를 로컬에서 결정론적으로 찾아 정리하고 추적합니다 — 모델 호출 0회, 네트워크 0회.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **53**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 69</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 코딩 에이전트를 위한 실행 전 보호 장치입니다. 도구 호출이 실행되기 전에 파괴적인 Git 및 파일 시스템 명령과 민감한 파일에…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 플러그인 마켓 / DSH Plugin Marketplace: DeepSeek Harness Web GUI에서 GitHub…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - 把 DSH Web 状态行换成 1063 条梗:打字机 + 炫彩渐变 + 弹幕 + 12 个主题词库包,设置页可视化编辑.
- [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) - 终末地 공식 웹사이트 스타일의 DSH Web 테마: 크림색 종이 배경, 먹색 텍스트, 시그널 옐로 강조, 전면 직각의 산업 편집 스타일.
- [arcships/rutis](https://github.com/arcships/rutis) - 계속 실행되는 프로그램을 위한 플러그인 런타임 — 프로세스와 머신 전반의 Rust 코어, TypeScript 및 Python 플러그인.
- [FeatherHunter/dsh-opencode-palette](https://github.com/FeatherHunter/dsh-opencode-palette) - 🎨 为长时间编程而生：38 款 opencode 护眼配色，一键换上 DSH | 38 eye-friendly opencode themes for…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 플러그인 엄선 디렉터리 — MCP / Skill / TUI / 멀티 Agent / 컨텍스트 메모리 /…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh 게임 소재 마스터 플러그인입니다. seedream 이미지 생성 모델과 minimax 동영상 생성 모델을 연동하여 다양한 게임 소재를…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness용 Zotero toolkit입니다. Zotero 라이브러리를 에이전트를 위한 증거 저장소로 바꿔 줍니다.
- [yi-yezhiqiu/dsh-prompt-market](https://github.com/yi-yezhiqiu/dsh-prompt-market) - DeepSeek Harness 提示词市场插件：对话框内一键浏览、搜索、收藏提示词，选中即写入输入框。零后端、免构建、数据只存本机.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Windows의 모든 에이전트 모드를 위한 DSH 플러그인: Git Bash 셸(pwsh 실행기 대체).
- [vritser/dsh-emacs](https://github.com/vritser/dsh-emacs) - An Emacs client for DeepSeek Harness.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness（DSH）기반 멀티 플랫폼 그룹 채팅 지능형 에이전트 시스템｜DSH 기반 멀티 플랫폼 그룹 채팅…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 중국어 웹소설 작가를 위한 로컬 집필 워크벤치(도구 19개): 집필 전에 이전 장의 연결 부분/개요/인물 카드/회수할 복선/용어 규칙을 모두…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android 버전: DeepSeek Harness, Ubuntu 실행 환경, 플러그인 및 파일 관리, 그리고 사용자가 승인한…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH 웹 플러그인: GitHub 스타일 활동 히트맵, 캐시 적중률 곡선 및 모델별 분석을 제공하는 일일 토큰 사용량 통계.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Community-curated DeepSeek Harness (dsh) plugins, tools, skills and learning…
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion：以助理和家的概念增强 dsh-im——哪个工作区有助理在管、在不在线尽收眼底，搬家拖一下就行.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness용 MCP 서버 관리자 플러그인: 설정 → MCP 페이지, OAuth(PKCE + 동적 클라이언트 등록) 또는…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness 플러그인: 15개의 obra/superpowers 엔지니어링 스킬, 이중 언어 설명, 스킬별 토글 |…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A 상거래 협상 런타임 + DeepSeek Harness(dsh) 플러그인입니다.
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - DeepSeek Harness Web용 MCP 서버 관리 UI — 플로팅 패널, JSON 가져오기 및 프로필 기반 영속성을 제공합니다.
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML이 아닌 진짜 PowerPoint입니다. AI에게 다룰 내용을 말하면 pptwise가 자신의 컴퓨터에서 편집 가능한 덱을 만듭니다.
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - DeepSeek Harness 플러그인: DietrichGebert/ponytail lazy senior 모드 및 7단계 사다리 포트, 이중…
- [LAU-MARS/dsh-cad](https://github.com/LAU-MARS/dsh-cad) - deepseek harness 2D and 3D CAD plugin.
- [qinyre/dsh-plugin-capabilities](https://github.com/qinyre/dsh-plugin-capabilities) - 在 dsh 设置页管理技能与 MCP 服务器，支持从 Claude Code、Codex 导入.
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Embedded C/C++ AI engineering plugin — firmware skills.
- [biedongbin/dsh-claude-compat](https://github.com/biedongbin/dsh-claude-compat) - DSH plugin: bridge Claude Code.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 로컬 컴퓨터의 WorkBuddy 데스크톱 버전에 로그인된 모델(DeepSeek / GLM / Kimi / MiniMax 등)을 로컬…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - DeepSeek Harness(DSH)를 위한 올인원 skills, subagent, MCP 및 LSP 관리자 — Claude Code…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 플러그인을 위한 상시 호환성 테스트: 정확한 릴리스, 격리된 러너, 수정 가능한 업스트림 이슈.
- [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) - DeepSeek Harness(DSH)를 위한 무료·간편 툴킷: 영구 무료 모델 4종.
- [1321928757/dsh-mysql](https://github.com/1321928757/dsh-mysql) - MySQL connector plugin for DeepSeek Harness: configure connections in settings…
- [mokuyoaxis/dsh-iris](https://github.com/mokuyoaxis/dsh-iris) - Media generation and visual understanding for DeepSeek Harness, with…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 플러그인을 위한 X-ray: 선언된 기능과 실제 동작을 비교합니다. 레지스트리 + 정적 스캐너 + 배지.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - 프로젝트 문서와 장기 메모리를 전용 Obsidian vault에 일반 Markdown으로 보관하는 DeepSeek Harness 호스트…
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - DeepSeek Harness(dsh)를 위한 세션 딥 링크 + 전체 세션 내보내기(마크다운/JSON) + 페어링을 통한 승인된 세션 간 메시징.
- [wads-dev/dsh-live-voice](https://github.com/wads-dev/dsh-live-voice) - DSH를 위한 로컬 우선 음성 대화입니다. 선택적 외부 공급자와 함께 음성 인식 및 음성 합성을 자체 컴퓨터에서 실행합니다.
- [fan56/dsh-topics-memory](https://github.com/fan56/dsh-topics-memory) - Topic memory for LLM agents — edited, not accumulated: a topic keeps the…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH 플러그인: 네이티브 dsh-better-sidebar 탭으로 제공되는 IDE급 Git 도구 창 — 브랜치 트리, 커밋 그래프, 변경…
- [lwmxiaobei/dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) - DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 다중 폴더 workspace: DSH(DeepSeek Harness)의 Agent가 기본 디렉터리뿐 아니라 추가한 다른 폴더도 동시에 읽고 쓸…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - DeepSeek Harness용 엔지니어링 워크플로 플러그인: 작업 단계, 검증 기록, 커밋 확인, 스킬 및 규칙 관리.
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 롤플레잉 플러그인: 캐릭터 카드(시스템 프롬프트 주입 + 사용자 프롬프트 재작성), 공유 가능한 단일 파일 카드 패키지, 원본 UI를…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness(dsh) 플러그인을 위한 종속성 없는 검증 표준 — 정적 구조 게이트(R), cordis 계약 검사(K)…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness의 OpenCode — OpenCode Zen + Go 무료 티어 모델을 계속 작동하게 하는 DSH 플러그인…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness를 위한 서드파티 플러그인 마켓플레이스 및 보호된 수명 주기 관리자.
- [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) - Query local log files with Chinese natural-language time expressions…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx는 사람을 중심으로 설계된 확장 가능한 데스크톱 작업 공간입니다.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness를 위한 모든 기능이 포함된 코딩 에이전트 — Claude Code 스타일 워크플로, 원하는 모델, TUI…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 입력 경험 플러그인: 보내기/줄바꿈 키 전환, 우클릭 메뉴, 패널 스크롤 및 크기 기억, OpenCode 요청 헤더 자동 주입.
- [feely0208/deepwhale-desktop](https://github.com/feely0208/deepwhale-desktop) - 深鲸桌面 · 永久免费开源的 DeepSeek Harness 桌面壳（背景皮肤/桌面宠物/用量面板）.
- [KIDLi1412/dsh-session-cost](https://github.com/KIDLi1412/dsh-session-cost) - DSH web plugin: conversation status bar with per-session token cost estimate…
- [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) - DSH的插件创意市场来啦!～～～欢迎使用&amp;提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - DeepSeek Harness 데스크톱 버전에 &quot;네트워크 대역 제한 + 선택적 숫자 비밀번호&quot;가 있는 원격 액세스 진입점을 제공합니다.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh)를 위한 커뮤니티 버전 로컬 배포·운영 도구 모음: 설치 / 시작 / 모니터링…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness(DSH) 웹 플러그인: 시장 대시보드 사이드바 탭을 모니터링합니다 — 마우스를 올리면 장중 차트가 표시되는…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 플러그인: Windows 샌드박스 ACL 프로비저닝 실패.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 출처가 표시되지 않은 빈 모델 시도를 재시도 가능하게 만듭니다. 이를 판별할 수 있는 하나의 접점.
- [denceee/dsh-everything-claude-code](https://github.com/denceee/dsh-everything-claude-code) - everything-claude-code를 DeepSeek Harness에 맞게 조정합니다.
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins that clean up after themselves: a Swift 6 port of the cordis plugin…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness 에이전트 프리셋: Codex 및 Claude Code를 위임 하위 에이전트로 사용하며, 각각 읽기 전용 및 전체…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus-verified 라이프사이클 커널과 Cordis 호환성 어댑터를 갖춘 Rust 플러그인 런타임입니다.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.

</details>

<a id="writing"></a>

## 작성, 토론 및 동영상

모드 기능에 관한 글, 토론 및 동영상입니다.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
| 최초 등록 | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 1 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

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
| TypeScript | 385  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 80   | `Enc-hanted/dsh-pulse`, `X-C1811/dsh-web-search-plugin`, `karanb192/awesome-claude-code-mods`                 |
| Python     | 38   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12   | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 7    | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Swift      | 4    | `bhargava-gumpula/claude-mods`, `essedev/relay`, `peaceinitiativemenhadenoil263/claude-status-bar`            |
| Kotlin     | 2    | `WSK-build/DSHBox`, `dphmoblie/deepseek-harness-android`                                                      |
| PowerShell | 2    | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Emacs Lisp | 1    | `vritser/dsh-emacs`                                                                                           |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |

<sub>언어를 명시한 항목만 집계됩니다. 문서 및 토론 항목은 이 표에서 제외됩니다.</sub>

## 기여

수정 사항을 제보해 주시면 이 목록을 가장 빠르게 개선할 수 있습니다. 항목이 잘못 분류되었거나, 등급이 잘못 매겨졌거나, 이름 충돌로 인해 프로젝트가 잘못 제외되었다면 이슈 또는 풀 리퀘스트를 열어 주세요. 마지막 유형은 자동 필터가 가장 자주 잘못 판단하는 경우입니다.

---

<sub>독립적인 커뮤니티 프로젝트입니다. Anthropic와(과) 제휴, 승인 또는 검토를 거치지 않았습니다. Claude Code, Claude 및 Anthropic은(는) Anthropic의 상표입니다. 제품 동작은 예고 없이 변경될 수 있으므로, 중요한 내용은 공식 문서에서 확인하세요. 에셋은 원 프로젝트의 자산으로 남으며, 라이선스가 허용하는 경우에만 재현됩니다.</sub>

<sub>마지막 업데이트 · 2026-10-11T16:50:06+08:00</sub>
