<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="멋진 Claude 모드">
</p>

<h1 align="center">멋진 Claude 모드</h1>

<p align="center"><b>Claude Code 모드와 플러그인, 그리고 이들이 변경하는 더 심층적인 동작을 근거에 따라 등급화한 색인입니다.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-534-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **실시간 색인** · 마지막 동기화: `2026-10-11T23:26:48+08:00` (UTC+8)
> · 항목: **534** · 최신 업데이트에 추가됨: **0** · 구현 언어: **12**

<sub>아래의 모든 항목은 자동으로 수집, 필터링 및 재검증되었습니다. 유료 게재 항목은 없습니다.</sub>

<a id="featured"></a>

## 지금 주목할 항목

<sub>카테고리별 항목 하나를 근거 등급과 별점에 따라 순위를 매겨 선택하며, 업데이트할 때마다 다시 계산합니다. 추천이 아닌 순위이며, 모든 항목은 아래의 전체 카드로 연결됩니다. 스크린샷이나 녹화본을 게시한 프로젝트를 우선하므로 목록이 시각적으로 유지됩니다.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9474 · TypeScript · ✅ official</sub>
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
<sub>⭐74336 · TypeScript · 👁️ observed</sub>
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
- [공식: Anthropic 자체 저장소 및 릴리스 노트](#공식-anthropic-자체-저장소-및-릴리스-노트) — **14**
- [모드: 모드 기능으로 구축됨](#모드-모드-기능으로-구축됨) — **408**
- [DSH 및 Cordis 플러그인 생태계](#dsh-및-cordis-플러그인-생태계) — **101**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150172 · TypeScript · ✅ official · 0 天</summary>

##### 📝 요약

Claude Code는 터미널에서 실행되며 코드베이스를 이해하고, 자연어 명령만으로 반복 작업을 실행하고 복잡한 코드를 설명하며 git 워크플로를 처리해 더 빠르게 코딩할 수 있도록 돕는 에이전트형 코딩 도구입니다.

<sub>🔧 코드에서 사용된 항목: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                           |
| -------- | -------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트` |
| 근거     | `Anthropic 자체에서 게시됨`                  |
| 언어     | TypeScript                                   |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **150172** |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9474 · TypeScript · ✅ official · 1 天</summary>

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
| 스타        | **9474**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8248 · Python · ✅ official · 1 天</summary>

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
| 스타        | **8248**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6342 · Python · ✅ official · 241 天</summary>

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
| 스타        | **6342**   |
| 마지막 푸시 | 2026-02-11 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1797 · Shell · ✅ official · 1 天</summary>

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
| 스타        | **1797**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

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
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 모드에 `$.ui.notify`를 추가했습니다. 자체 알림 설정을 통해 네이티브 알림을 표시하고 어떤 채널에서 전송했는지 알려줍니다.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` 훅 또는 모드의 `prompt.submit` 훅 실행 중 Esc 또는 인터럽트로 인해 헤드리스 세션이…

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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐486 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

GitHub에서 스캔한 공개 Claude Code mods(function hooks)의 커뮤니티 카탈로그로, 각 mod가 네트워크를 통해 읽기, 쓰기, 실행 또는 전송할 수 있는 항목을 표시합니다. https://mods.aidojo.si/ 찾아보기

<sub>🔧 코드에서 사용된 항목: `data/seeds.txt`, `data/duplicates.txt`, `README.md`, `data/repos.txt`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **486**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐338 · Python · 👁️ observed · 0 天</summary>

##### 📝 요약

macOS menu bar & Windows tray app pinning Claude Code, Codex, Antigravity & Grok CLI quota, burn rate, and cost to your screen. Local-first, no LLM API calls. HTML reports, 14 themes.

<sub>🔧 코드에서 사용된 항목: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | Python                                                         |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **338**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐186 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 요약

Claude Code mods: plugins built on hooks that add live lines above the prompt, guards, panes and games. Context bar, usage meter, Codex review watch, Markdown preview, Spotify now playing and more.

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
| 스타        | **186**    |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐132 · TypeScript · 👁️ observed · 7 天</summary>

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
| 스타        | **132**    |
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
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **96**     |
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

A collection of claude code mods

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
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐75 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **75**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐66 · TypeScript · 👁️ observed · 8 天</summary>

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
| 스타        | **66**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 요약

Claude Code mods by Darrell Wang — bands above the prompt, zero model tokens. 台股／美股看板 + more to come.

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
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 요약

Expert skills, agents, commands, rules, hooks & output styles for Claude Code — session continuity + modern CLI tooling for real-world dev workflows

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
| 최초 등록   | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 요약

Claude Code mods: live plan progress bars above the prompt

<sub>🔧 코드에서 사용된 항목: `README.md`</sub>

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
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐44 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code가 터미널에서 바로 이미지를 표시하고 동영상을 재생합니다: 스크린샷, Playwright 녹화 및 동기화된 변경 전/후 QA. Ghostty 및 kitty.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **44**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

A pixel Pokémon that lives above the prompt in Claude Code

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **25**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

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
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 요약

Xcode's build, tests, console and SwiftUI previews inside Claude Code

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
| 최초 등록   | 2026-10-11 |

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

Claude Code mods: 21 styles and a full set of features you turn on when you need them, for the terminal and the desktop app. · 一键为 Claude 换上新风格，并提供一整套按需开启的功能。

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
| 최초 등록   | 2026-10-11 |

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

Ten Claude Code mods, beginner guides, creation prompts, safe demos, and a build-your-own template.

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 요약

Claude Code mods: usage-band shows your 5h/7d limits, context window and cache hit rate above the prompt

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **13**     |
| 마지막 푸시 | 2026-10-03 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 요약

Claude Code mods that make Claude's questions easier to read and answer (qa-guide).

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
| 최초 등록   | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>애니메이션 녹화 · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

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
| 마지막 푸시 | 2026-10-11 |
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

Ten open-source mods for Claude Code: live panes, bands, status lines and tool-call guards. Burn meter, launch codes, session wrapped, boss fight, code pet and more.

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
| 최초 등록   | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 요약

Two Claude Code mods: Codex computer-use bridge and coordinated Claude sessions. Source, build prompts, setup and tests.

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
| 최초 등록   | 2026-10-11 |

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

A UI around your Claude Code and Codex terminals that your agents build, so the only model in your head is yours.

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
| 최초 등록   | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 요약

KOZMOS — live, visual mods for Claude Code (CLI + desktop): bands above the prompt, sidebars, status ticker, companions, guards and sound.

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
| 최초 등록   | 2026-10-11 |

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

Six Claude Code mods in one plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius) with per-mod switches, plus a mods-vs-hooks report.

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
| 최초 등록   | 2026-10-11 |

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
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 374</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Collection of 100+ mods you can use with Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 및 이를 빌드하기 위한 도구: 먼저 builder skill을 제공한 다음 mods를 제공합니다.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - The Claude Code harness I run every day, published under this name since day…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - 用 Claude Mods 给 Claude Code 换屋顶：不改二进制，把系统提示和英文提醒换成你自己的字（2.1.287+）.
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Four Claude Code mods: Cache Keeper, Recording Mode, Goal Meter, and Collision…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker 的 Claude Code mods：把 agent 的運作畫成看得懂的東西.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude Code mods that fix and translate your prompts before Claude reads them.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Claude Code 터미널 기록을 데스크톱 앱처럼 보이게 하는 모드.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code용 사이드 패널: 세션에서 실행하는 서브에이전트, 각 에이전트가 하는 일, 토큰 및 대화를 클릭 한 번으로 확인할 수…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Source-cited Obsidian knowledge base about Claude Code mods: how they work, how…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop(Code 탭) 사이드바 패널: 모든 Claude Code session의 미완료 및 진행 중인 할 일을 나열하고…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Claude Code mods and skills from Nekyia Labs, built and used daily by AIs…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill that teaches Claude Code agents to build Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop(Code 탭) 입력 상자 위의 사용량 막대: 5h / 7d 할당량, token 사용량, 비용.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 하나의 마켓플레이스에서 설치할 수 있는 커뮤니티 Claude 모드, 플러그인 및 스킬.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Mods (function-hooks plugins) for Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - The Baselane mods gallery: Claude Code mods, checked and pinned.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 대화형 에이전트와 협업하는 사람을 위한 의사 결정 큐 CLI/TUI. 에이전트가 질문을 올리면 사람은 하나의 받은 편지함에서 답합니다.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code용 플로팅 상태 카드 — 모델, 컨텍스트, 속도 제한, 비용, 브랜치 — 그리고 모든 스크립트나 mod가 값을 전달할 수…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code용 Mods: 터미널 UI에 실시간 창과 동작을 추가하는 함수 후크 플러그인.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code mods: screen-guard masks names and secrets while you screen-share;
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Claude Code용 실시간 GSD 대시보드: 로드맵, 분기 기능이 있는 에이전트 트리, 컨텍스트와 비용, 작업 스트림 및…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Unlock the full power of Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context 및 MCP 탭이 있는 사이드 패널, 프롬프트 위의 상태 줄, 새롭게 스타일링된…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Panels, guardrails and quality-of-life mods for Claude Code: context, usage…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Two Claude Code mods above the prompt box: context-window meter, 5-hour limit…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Make the Claude Pro plan last longer: Claude Code mods for an exact usage HUD…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code가 이름을 지정한 markdown 파일을 읽어 세션 옆에 렌더링하고, 블록을 가리키면 Claude가 해당 블록을 편집하도록…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code용 음성 동료. ElevenLabs conversational AI로 구동되는 3D 늑대와 대화하며 생각을 정리하세요.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code mods: typing-speed, a live typing speedometer with per-prompt stats.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code용 불꽃놀이: 모든 키 입력, 도구 호출, 커밋 및 통과한 테스트가 프롬프트 위에서 점자 불꽃놀이로 올라갑니다.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Discover Claude Code mods, plugins and extensions with animated demos, category…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code mod: mermaid diagrams drawn inline in the transcript.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 작은 Claude Code 모드(함수 훅 플러그인): session-switcher 등.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code mod: pasted image thumbnails above the prompt, in any terminal.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code mods: Claude Tools menu, Zen mode, terminal themes, effort and mode…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code mods: mod-scout.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Two Claude Code mods for running many sessions at once: a context card above…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: discover, inspect, toggle and update Claude Code mods.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code mods: context bar, agents panel, PDPA blur.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Best Claude Code Mods: hand-picked, validated, pinned.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 플러그인: 자동 Claude 모델 라우팅. 프롬프트, 단계, subagent마다 Haiku, Sonnet 또는 Opus와…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code용 여섯 가지 모드: 애니메이션 Clawd 마스코트, 사용량 제한 및 프롬프트 캐시 바, 전송 전 메시지 검사기, 빠른…
- [GoneTone/cc-askpass](https://github.com/GoneTone/cc-askpass) - Claude Code 모드로, Claude이 직접 터미널에 복사하지 않고 sudo가 필요한 명령을 실행할 수 있게 합니다.
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - A marketplace of mods for Claude Code: a step debugger for the agent loop, git…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 여섯 가지 Claude Code mod: 프롬프트 위에 플랜 제한과 컨텍스트를 표시하고, 권한 프롬프트를 위한 허용 목록 코치, 서브에이전트…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code용 최고의 올인원 mod pack: 사용량 제한과 context HUD, rm -rf 및 git reset --hard를…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude Code에서 YouTube Shorts를 재생하세요 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren의 Claude 툴킷: Claude Code용 skills, mods 및 MCP servers.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit 및 Write diff를 나란히 놓인 두 열에 그리는 Claude Code 모드.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods for Claude Code: Clawd, a tiny pixel mascot who acts out what Claude is…
- [reporails/arcade](https://github.com/reporails/arcade) - Classic desktop games as Claude Code mods, played in a pane while Claude works.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 플러그인 마켓플레이스로 설치할 수 있는 엄선된 Claude Code 모음: 테마, 창, 상태 표시줄, 초상화.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - 하네스 엔지니어링에 집착하는 Rustacean이 설계한 매우 주관적인 Claude Code 플러그인.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Claude Code mods that keep an agent honest — function hooks that guard scope…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code를 위한 수동 공격형 물 마시기 알림. 토큰은 0개, 판단은 최대치.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code용 macOS notch 대시보드: 사용량 제한, 열린 세션, 작업 진행률, 프롬프트 캐시 카운트다운 및 할 일 — 다섯…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod per Claude Code: barra della prompt cache, prossimi passi, bottoni rapidi e…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code 모드: 세션이 열거나 푸시하는 GitHub PR의 실시간 패널 — CI, 리뷰, 충돌, 병합 — 모든 세션이 하나의…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 프롬프트 위 표시줄에 사용량 한도와 지출을 그려 주는 Claude Code 모드.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman의 Claude Code 모드 (마켓플레이스 herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code mods: progress bars for plans, a ledger of what Claude left…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Claude Code를 위한 픽셀 아트 Naruto 동반자: Claude이(가) 작업하는 동안 20명의 닌자와 60개의 인술이 실행됩니다.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code가 백그라운드에서 실행하는 항목을 확인하세요: 서브에이전트, Codex 작업, 셸, 모니터, cron 작업 및…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows에서의 Claude Code 모드에 대한 첫날 현장 노트: 컨텍스트/할당량 연료 표시줄, Thai UI 모드, Matrix 부팅…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code 모드: 프롬프트 위에 실시간 비용, 컨텍스트 및 플랜 할당량 미터를 표시합니다. 아이콘에는 Nerd Font가 필요합니다.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 하위 에이전트 확장, 대규모 컨텍스트 프롬프트 및 재시도 루프가 사용량 창을 소모하기 전에 보류하는 Claude Code 모드입니다.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods for claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 명명된 프로필을 사용해 저장소별로 전역 스킬, 에이전트, 규칙 및 도구를 켜거나 끄는 Claude Code 모드입니다.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 플러그인(모드): 여러 Claude 계정 간 전환, 상태 밴드에서 사용량 제한 확인, 터미널 패널에서 에이전트…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 테스트 완료, 한 번의 명령으로 설치 가능한 Claude Code 모드: YOLO 모드용 가드레일, 실시간 비용 및 컨텍스트, 패널, 펫…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods for Claude Code: plugins built on function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - 코딩 세션을 위한 영화 스타일 크레딧. 모델 호출이나 텔레메트리가 없는 네이티브 Claude Mod입니다.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Saját Claude Code mod-ok pluginpiaca.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - A bunch of claude code mods built by me.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 필요할 때 사용하는 Claude Code 모드 — 대화를 읽고 적합한 모드를 만드는 스킬: 계획 진행률 표시줄, 파일 창, 컨텍스트 게이지…
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - A cliamp-backed YouTube player inside Claude Code (Claude Code mod).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code mods: agent-fleet dashboard and autopilot (local-mods marketplace).
- [vynnlee/mods](https://github.com/vynnlee/mods) - Claude Code mods by vynnlee. One folder per mod, installable from one…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code로 작업하면서 외국어를 익히세요.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - 하나의 관제탑에서 여러 저장소의 여러 세션을 실행하기 위한 Claude Code 모드.
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - 에이전트가 Java을 작성할 때 Alibaba Java 규정(p3c)을 위반한 코드는 디스크에 저장되지 않습니다.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code용 실시간 비용, 토큰, 컨텍스트 사용량 사이드바: 세션 내에서 턴별 비용, 캐시 적중률, burn rate, 30일…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code 모드: 모든 세션에서 Claude이(가) 제안하는 후속 작업 백로그와 각 세션의 다단계 작업을 위한 작업 목록.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 안의 인터넷 라디오: cliamp 사이드바, 미니 플레이어, 즐겨찾기, 탐색, 집중 모드 및 Claude용 라디오 도구.
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - 재미있고 유용한 Claude Code 모드: 프롬프트 위에 픽셀 생물이 표시되고, Agent Dock이 포함된 도구 메뉴, 프로젝트 상자 및…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: a Claude Code mod for designing and running graphs of agents…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude가 요리 중입니다. 팀과 채팅하세요. 친구들이 온라인에서 Claude Code 세션 바로 옆에 있습니다.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - 올인원 Claude Code mod: 실시간 HUD, 안전장치(명령 차단, 시크릿 마스킹, 롤백이 가능한 턴 체크포인트), 자동 린트/테스트…
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code가 작업하는 동안 프롬프트 위에서 펼쳐지는 우주 전투.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 각 Claude Code 에이전트가 컨텍스트에 어떤 파일을 가지고 있는지, 그리고 각각 얼마나 있는지 확인하세요.
- [dbroadhurst/claude-mod-todos](https://github.com/dbroadhurst/claude-mod-todos) - Claude Code mod: a pane summarising the remaining todos, with Do, Chat, Defer…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 냉정함을 유지하세요. Claude Code 사용일을 위한 온도계입니다.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Code의 프롬프트 하단과 프롬프트 위에서 프롬프트 캐시, 컨텍스트 및 계획 한도를 한눈에 확인.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 터미널 및 데스크톱 앱용 소형 Claude Code 모드.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod: 작업, 서브에이전트, 워크플로 실행, 목표 및 도구 호출을 위한 진행 창을 제공하며 막대, 타임스탬프 및 남은…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Claude Code mod: 전체 세션의 클릭 가능한 타임스탬프 목차로, 주제와 범주별로 그룹화됩니다.
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod: 프롬프트 위에 플랜 속도 제한, 컨텍스트 사용량, 세션 비용 및 작업별 토큰을 색상 막대로 표시합니다.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - 에이전트 응답에 스페인어 단어를 추가하는 Claude CLI skill + mod.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Your Alarum events above Claude Code.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Code의 프롬프트 위에 Floatee 백로그를 표시하여 한 번의 클릭으로 할 일을 실행하고 안내하며 완료 처리합니다.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code용 Evangelion 스타일 사이드바: 컨텍스트, 할당량, 활동, PR, 하드웨어, 세션 및 forge 패널.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 이를 Person of Interest의 The Machine처럼 재스타일링하는 Claude Code 모드입니다.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: 라이브 DAG 패널을 제공하는 서브에이전트의 필수 검증 DAG 워크플로용 Claude Code 모드.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code를 위한 오픈 소스 모드: 창, 상태 줄, 토스트, 도구 가드 및 슬래시 명령.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: 세션 상태, 실시간 Spec Kit 진행 상황 및 사용량 창 거버넌스.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 프롬프트 위에 한 줄로 표시되는 컨텍스트 창으로, Claude Code가 자체 미터를 그리는 방식으로 표현됩니다.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop용 실시간 작업 HUD: Claude이(가) 작업하는 동안 프롬프트 위에 표시되는 스트립과, 한 번 클릭하면…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code를 위한 무료 오픈 소스 플러그인입니다. /clear를 실행하기 전에 Claude이(가) 읽고 편집할 수 있는 짧은 인계…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Stash prompts for later and pop them back into Claude Code.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Ghostty 및 kitty에 이미지를 인라인으로 표시하는 Claude Code 모드.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 세션의 GitHub개 풀 리퀘스트를 트랜스크립트 옆 창에 표시하는 Claude 모드: 설명을 프롬프트 상자에 인용하고 검사 및 리뷰 상태를…
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code mod: generate sound effects from text prompts with a local Stable…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code 스킬: 문서 팩트체커, 코드 감사기, 버그 메모리 로그, 모드 등.
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod: 모든 세션에서 Claude이(가) 작성한 오늘의 코드 줄 — 새로 추가됨, 수정됨, 삭제됨 — 을 표시하고…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod: 답변의 클릭 가능한 경로 — 폴더를 클릭하면 Finder에서 열고, 파일 이름을 클릭하면 파일을 엽니다.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 버디 플러그인: 프롬프트 위에서 규칙을 기억하고 Claude의 단축키를 알려 주는 ASCII 동반자.
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code 모드: Jev에 기반한 모델/추론량 라우팅, 축어적 컨텍스트 압축 및 출력 트리밍으로 긴 세션의 비용을 절감합니다.
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code 모드: Claude Code를 위한 보안 계층 — 비밀 정보 마스킹, 신뢰할 수 없는 콘텐츠 알림, MCP 도구 오염…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 플러그인 및 모드: 훅으로 강제되는 인간 승인 게이트와 프롬프트 위 상태 표시줄을 갖춘 AI 네이티브…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods 컬렉션 | 클로드 코드 모드 모음집.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code용 아늑한 RPG HUD 모드.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: 로컬 오픈 소스 Kokoro TTS 음성으로 요청 시 Claude의 답변과 사용자의 프롬프트를 소리 내어 읽어주는…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude이 실수하면 때려 주세요 — Claude Code를 위한 스트레스 해소용 mod: 만화풍 엉덩이, 8개 때리기, 9개 엉덩이…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - 실시간 창, 비용을 고려한 모델 라우팅 및 안전 가드를 위한 Claude Code 모드: 한 번의 명령으로 마켓플레이스에서 설치하세요.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code 모드 및 플러그인: 사용량 모니터, 토큰 추적기 및 상태 줄.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods. touch-map: Claude가 나열, 읽기, 편집 또는 생성한 파일을 트리와 activity map으로…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code 모드: Claude이 변경한 파일과 그 이유, 실시간 서브에이전트 상태 및 남은 플랜 한도를 보고.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code 모드: 프롬프트 위에 세션 통계 카드를 표시합니다.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 프롬프트 위에 표시되는 애니메이션 점자 고양이.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code 모드: 저렴한 작업은 하위 Claude Code를 통해 GLM/Kimi로 라우팅하고, 중요한 작업은 구독에서 유지합니다.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - OmniDimension 음성 에이전트 테스트 호출을 실행하는 Claude Code 프롬프트 위의 픽셀 고양이. Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 컨텍스트 창을 작게 유지할 수 있도록 압축하기 좋은 시점을 선택하는 Claude Code 모드.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code용 Claude Mods: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider의 Claude Code 플러그인 마켓플레이스.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - General-purpose mods for Claude Code: bands, panes, toasts and hooks.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - 코드가 변경될 때마다 LGTM Lines 우주선이 지나갑니다 — Claude Code 모드.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 주간 페이스 경고가 포함된 애니메이션 주민 체력 카드로 표시하는 사용자의 Claude 사용 한도 — Claude Code 모드.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude이 작업하는 동안 하는 짧은 운동: 일일 목표, 연속 기록, 배지 및 선택적 리더보드. Claude Code 모드.
- [atharv6f/waypoint](https://github.com/atharv6f/waypoint) - Claude Code 프롬프트 옆에 계획, 작업 및 에이전트 진행 상황 표시 — Claude Code 모드.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code용 사용량 보드: 모델별 지출(오늘, 이번 주, 이번 달, 전체 기간) 및 주간 한도 예측.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code 모드: 프롬프트 위에 실시간 컨텍스트 창 분석을 표시합니다.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - 푸터에 프롬프트 캐시 카운트다운을 표시하고 자리를 비운 동안 5분 캐시를 유지하는 Claude Code 모드.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code용 Now Playing mod: 프롬프트 위에 앨범 아트, 컨트롤 및 Up next 창과 함께 표시되는 Apple…
- [benlrice/logpane](https://github.com/benlrice/logpane) - Claude Code mod: a pane that tails the files your Bash calls write to.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code용 모드: 캐시 시계, Blast Radius, 제안, 작업 목록, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 당신의 Claude Code를 위한 그냥 올빼미.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 한 줄짜리 Claude Code 밴드(캐시 카운트다운, 컨텍스트, 제한, 다음 작업)와 7개의 커뮤니티 모드를 하나의 플러그인으로 설치하며…
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoom이 포함된 오리지널 Doom 엔진으로, Claude Code 안에서 플레이 가능. Mac Apple Silicon 알파 버전.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 대화에서 열린 항목의 목록을 계속 유지하고 프롬프트 위 밴드에 표시하는 Claude Code mod입니다.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - 터미널을 벗어나지 않고 풀 리퀘스트처럼 Claude이(가) 수정하는 모든 파일을 검토.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 진정한 엔지니어를 위한 Claude Code 모드.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code 안에 사는 Tamagotchi: 부화하고, Claude이(가) 작성한 코드를 먹고, 버그를 남기며, 여덟 종류의 성체 중…
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code mod: SwiftUI previews rendered by Xcode, shown in a terminal pane.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 함수 훅으로 작성된 Claude Code 모드와 이를 제공하는 마켓플레이스. dash: 한 패널에 있는 세션의 대시보드.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code 모드: guard가 도구 호출을 차단한 후 동일한 대상을 향하는 인식된 우회 경로를 중지하고 Claude에게 사용자에게…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code 모드: 실제 출력에서 읽은 진행률과 예상 완료 시간을 하나의 뷰에서 백그라운드 작업으로 표시합니다.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code 모드: 팀원, 이름이 지정된 하위 에이전트 및 다른 세션의 메시지를 위한 통합 받은편지함으로, 읽지 않은 메시지 수와…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code 모드: 샌드박스 차단을 설명하고 반복되는 차단을 검토 및 실행 취소 가능한 설정 변경으로 전환합니다.
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code용 즐겨찾기: 명령과 스킬을 위한 원클릭 아이콘.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 이봐요, 음소거했어요! diff를 버리고 장단을 끊으세요. 더 이상 편집도, 크레딧 차감도 없습니다.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code 모드: delete-guard(파일 삭제 확인) 및 octopus-crew.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktop 앱과 터미널에서 프롬프트 위 밴드로 구독 사용량(5h / 7d)을 표시하는 Claude Code mod.
- [ErnestTramp/claude-critters](https://github.com/ErnestTramp/claude-critters) - Claude Code 모드: 백그라운드 에이전트를 픽셀 생물로 표시하며, 모델마다 스프라이트 하나씩 제공.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - 프롬프트 위에서 병렬 브랜치와 worktree를 실시간으로 보여 주는 레이더: 어떤 항목이 깔끔하게 병합되는지, 어떤 항목이 충돌하는지, 어떤…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - 작업 중간에 떠오른 생각을 기록하고, 프로젝트와 컴퓨터별로 분류하며, 프롬프트로 전환하는 Claude Code 모드.
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code 답변의 모든 코드 블록에서 Ctrl+클릭으로 링크 복사.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - 하나의 Marketplace를 통해 설치되는 Claude Code 모드(function-hook 플러그인).
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Claude Code 모드: context-bar-plus(컨텍스트 바, 할당량, 서브에이전트 모드).
- [Hsiang-LinC/vault-jot](https://github.com/Hsiang-LinC/vault-jot) - Claude Code 모드: 어떤 세션에서든 아이디어를 Obsidian 볼트 받은편지함에 저장.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 모드: 각 답변에 걸린 시간, Claude이(가) 생각한 시간, tok/s를 Claude desktop app의 답변…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code 모드: 화면을 공유하는 동안 streamer-mode가 비공개 창, 밴드 및 상태 줄을 숨깁니다.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook plugins (mods).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod: 5시간 사용 제한이 끝날 때까지 기다린 뒤 대신 &quot;continue&quot;를 보냅니다.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Code 프롬프트 위에 표시되는 조종석입니다. 오리가 게이지를 읽습니다.
- [its-coughfee/pulse-file-tree](https://github.com/its-coughfee/pulse-file-tree) - Claude Code mod: sidebar file tree that pulses on files Claude just edited.
- [jasonwblock/sdlc-tracker](https://github.com/jasonwblock/sdlc-tracker) - SDLC Tracker: 에이전트형 SDLC 키트의 흐름에서 각 작업 항목이 어디에 있는지 보여주는 사이드 패널이 있는 Claude Code…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 각 서브에이전트와 해당 에이전트가 건드리는 파일, 그리고 세션의 사용량과 비용을 위한 패널을 제공하는 Claude Code 모드입니다.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 사이드바의 context 사용량 패널: 총량, 분류, 라운드별 증가량, 가장 많은 공간을 차지하는 항목, 캐시, Claude이(가) 현재 하는…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 사이드바의 파일 목록: 이번 대화에서 어떤 파일을 새로 만들고, 수정하고, 삭제했는지와 각각 몇 줄을 변경했는지 표시합니다.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 입력창 위를 뛰어다니는 8비트 스타일의 毛毛(흑백 네덜란드 드워프 롭 토끼): 대기 중에는 납작 엎드리고, 작업 중에는 달리며, 도구를 사용할…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 사이드바의 ‘내가 물어본 것’: 이번 대화에서 주인이 입력한 모든 문장을 클릭 한 번으로 전체 보기, 복사 및 입력창으로 되돌리기.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 사이드바의 타임라인: 이번 라운드의 시간이 어디에 사용되었는지 표시합니다.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 사이드바의 토큰 왕래: 주 대화에서 매번 Anthropic에 몇 개의 토큰을 보내고, 얼마나 기다렸으며, 몇 개를 받았는지 표시하고 맨 위에…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code의 솔직한 속마음: 매 라운드의 답변이 끝나면 Claude이(가) 속마음을 한마디 조용히 말합니다.
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 새 슬래시 명령 및 사이드 패널과 같은 Claude Code용 작은 모드.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd는 Claude Code 프롬프트 위의 밴드에 삽니다: 세션을 연기하고, 실행 중인 항목, context 및 usage limits를…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code의 응답과 알림을 VOICEVOX / Irodori-TTS 등으로 읽어주는 mod.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Code 세션 간의 대화를 읽고 참여하는 Claude Mod (/crosstalk).
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code 모드. PixBar: 프롬프트 위에서 턴, 컨텍스트, 5시간 창 및 git에 따라 움직이는 픽셀 생물.
- [Khanthtutzin/subagent-crew](https://github.com/Khanthtutzin/subagent-crew) - Claude Code mod: 프롬프트 위에서 서브에이전트를 픽셀 Claude 마스코트로 실행합니다.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code 모드(usage-meter 등).
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 두 가지 Claude Code 모드: 채팅 옆의 파일 패널인 folio와 상태 줄이 포함된 터미널 세션 재스타일링인 tint.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: Claude Code가 알고 있는 내용을 실시간 그래프로 표시.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code의 답변을 기다리는 동안 주의가 흐트러지지 않게 합니다.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 사용 사례, 원본 데모, 호환성 근거 및 안전 참고 사항을 담은 커뮤니티 큐레이션 Claude Code Mods 가이드: 영어 / 中文.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - iTerm2 탭 부제목에 Claude이(가) 무엇을 하고 있는지 표시하여, 탭 표시줄을 한눈에 보고 어느 세션에 사용자의 주의가 필요한지 알…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Claude Code 프롬프트 위의 복슬복슬한 검은 고양이입니다. 눈을 깜빡이고, 가르랑거리며, 낮잠을 자고, 사용자의 컨텍스트를 걱정합니다.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 전환 가능한 권한 프로필을 제공하는 Claude Code 모드: 안전한 기본 프로필, 켜고 끌 수 있는 이름 지정 프로필, 그리고 그 외 모든…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code를 위한 커뮤니티 모드: Claude Code 내부에서 실행되는 가드, 패널 및 명령. 마켓플레이스: modhub.
- [merrickxxx/grill-pane](https://github.com/merrickxxx/grill-pane) - Claude Code mod: grilling interviews with clickable answers in a side pane.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code용 사이드 패널: Claude이(가) 작성한 파일, 터미널 분할, pull 기능이 포함된 git 저장소 상태, 사용량 바…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Claude Code 모드: 최근 사용률을 바탕으로 재설정 시 남게 될 주간 및 5시간 Claude 한도를 예측.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code를 위한 조용한 사이드 패널: 이 세션이 수행 중인 작업, 계획, 에이전트 및 다른 모든 세션.
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Code 트랜스크립트에서 각 프롬프트와 각 답변 위에 희미한 시간이 표시되며, 사용 중인 시계 설정의 형식으로 작성됩니다.
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Code가 접어 숨기는 내용을 다시 표시합니다: Claude이(가) 읽은 파일, 실행한 명령, 각 턴에서 수행한 작업.
- [moinsen-dev/speckit-xref](https://github.com/moinsen-dev/speckit-xref) - Keep the code on the spec: a Claude Code mod and a GitHub Spec Kit extension…
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code 모드: 프롬프트 푸터 모드 슬롯에 컨텍스트 창 사용량을 표시합니다.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - 세션 시작 시 CLAUDE_CODE_ENABLE_TODO_TOOLS를 설정하여 todo 도구를 제외하는 모델에서도 다시 활성화하는 Claude…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Claude Code mod that waits for a safe pause, then hands your session over or…
- [muellerei/task-line](https://github.com/muellerei/task-line) - 프롬프트 위 작업 목록에 현재 작업, 진행률 막대 및 개수를 작업당 한 줄로 표시하는 Claude Code 모드.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 내부에서 AI를 상대로 Connect Four 플레이 (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - 다른 코딩 에이전트가 저장소에 커밋하면 Claude이(가) 이를 감지하고 해당 보고서를 신뢰하는 대신 diff와 테스트로 감사하는 Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 여러 AI 에이전트가 공유하는 저장소를 위한 Claude Code 모드: 비밀 값이 .env 밖으로 나가거나 공개 원격 저장소로 푸시되는 것과…
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code 모드 마켓플레이스.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Fun, free mods for Claude Code that never spend a token.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code에서 SQL을 위한 가드레일: DB CLI를 통해 Claude이 DELETE, WHERE 없는 UPDATE, DROP…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows 및 CJK를 우선하는 하나의 모드: 모든 터미널에서 붙여넣은 이미지 및 텍스트 미리보기, CJK에 맞는…
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 무엇을 해 주는지에 따라 정렬한 최고의 Claude Code Mods. 직접 확인하여 각 항목을 한 줄로 정리했습니다.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code용 Claude Mods 두 가지: garde-du-corps.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Claude Code에 욕을 하면 만화 속 손이 되받아칩니다. 메시지는 전송되지 않으며, 정중한 버전이 프롬프트 상자로 돌아갑니다.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 데스크톱 앱의 Code 탭을 위한 실시간 세션 통계 사이드 패널: 컨텍스트, 비용, git 변경 사항, 턴 통계, 하위 에이전트…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code용 모드: safety-guard는 파괴적인 명령과 비밀 파일 접근을 차단하고, notify-router는 규칙 기반…
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod: 실시간 주식 티커, /quote 패널, 가격 알림, 시장 밴드, 모델이 호출할 수 있는 quote 도구.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code mod: a band above the prompt showing context used and a countdown…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code mod: a side pane that pins every diagram Claude draws and keeps a…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code mod: a dreaming pass that merges, rewrites and prunes Claude.
- [ray-amjad/memory-fork](https://github.com/ray-amjad/memory-fork) - Claude Code 모드: 매 턴 후 백그라운드에서 auto-memory를 최신 상태로 유지.
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code mod: drops vague prompts before Claude sees them, and suggests the…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod: 프롬프트 위 한 줄에 SSH 호스트, RAM 및 5h/7d 사용량 제한 표시.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 모드: Claude이(가) 작업하는 동안 할 팔굽혀펴기. 토큰 없음.
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 모드: plan mode에서 승인한 계획을 프롬프트 위의 라이브 체크리스트로 바꾸고, Claude이 완료할 때마다 각…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 엄선한 Claude Code 모음입니다. 모든 항목을 복제하고 claude plugin validate로 확인했으며, 건드릴 수 있는 항목을…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 비용 없는 모드: 도우미 에이전트는 Haiku에서 실행되고, 큰 파일과 로그는 Claude의 컨텍스트를 채우는 대신 무료 Gemini 모델이…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 세션을 따라가는 로파이 사운드트랙: 차분함, 집중, 몰입과 테스트 통과 및 실패를 알리는 신호음. 오리지널 음악입니다.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude이(가) 코딩하는 동안 학습하세요: 코드를 변경한 턴이 끝나면 해당 변경 사항에 관한 질문 하나가 프롬프트 위에 나타납니다.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude이(가) 수행하는 모든 편집을 기록한 테이프: 각 변경 사항이 직접 입력되는 모습을 재생하고, 단계별로 살펴보며, 모든 파일을…
- [sam-ruff/account-switcher-claude-code-mod](https://github.com/sam-ruff/account-switcher-claude-code-mod) - 계정 간 전환을 가능하게 하는 claude code용 모드.
- [samaphp/session-links](https://github.com/samaphp/session-links) - 세션에서 언급한 모든 링크를 프롬프트 위 한 줄에 표시합니다. Claude Code 모드.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code 함수 훅 최소 데모: prompt 위의 실시간 token/비용 패널, 클릭 가능한 버튼, 독립적으로 그리는 스레드…
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: Claude Code를 위한 비공식 Avengers 팬 모드.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - 프롬프트 위에 컨텍스트, 증가량, 할당량, 캐시, 네이티브 비용 및 에이전트 활동과 세션 세부 정보를 표시하는 Claude Code…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Claude Code 모드: 간단한 턴과 서브에이전트를 더 저렴한 모델로 라우팅하며, 선택한 모델보다 상위 모델은 사용하지 않음.
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - 설치할 것이 전혀 필요 없는 Claude Code 패널의 오리지널 DOOM: 엔진은 모드 내부에서 실행되며, 셰어웨어 에피소드와…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 춤추는 pixel-art Malenia와 함께 Claude Code용 원클릭 commit messages.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude 플랜 사용량(세션 및 주간 한도, 재설정 카운트다운, 컨텍스트)을 프롬프트 바로 위에 표시하는…
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - 작업 종류별로 모델과 작업 강도를 선택하고 해당 선택에 드는 비용을 보여주는 Claude Code 모드.
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Small mods that change how Claude Code looks and sounds.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 현재 세션을 창에 표시하는 Claude Code 모드입니다. 각 프롬프트, 해당 프롬프트에 대해 Claude이(가) 단계별로 수행한 작업…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - mods용 Claude Code plugin marketplace: Claude Code 내부에 bands, panes 및 기타 UI를 그리는…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Claude Code mod: rewrites a rough prompt in place, naming fitting skills, open…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Listen to Claude Code.
- [trietsch/claude-customizations](https://github.com/trietsch/claude-customizations) - Claude Code용 사용자 지정.
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code 모드: 프롬프트 위 한 줄에 5h/7d 할당량, 컨텍스트 창, 프롬프트 캐시 잔여 시간 및 세션 비용을 표시하고…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 모드: 장시간 실행되는 작업을 위한 애니메이션 진행 밴드와 완료 요약.
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 작은 Claude Code 모드 세 가지입니다. 하위 에이전트가 언제 완료되는지 확인하고, Claude이(가) 완료된 후 보낼 메시지를…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claude이(가) 읽기 전에 큰 스크린샷을 축소하여 긴 세션을 더 오래 유지하고, 클릭이 여전히 올바른 위치에 도달하도록 Claude에게…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - 프롬프트 입력창 위에 다음 프롬프트 추천을 표시합니다. /auto를 입력하면 10초 카운트다운 후 첫 번째 추천을 대신 전송합니다.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 작업 옆의 패널에서 Claude에게 별도 질문을 하세요. 기본 대화에는 표시되지 않습니다. 데스크톱 앱의 /btw처럼 작동합니다.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - 한 단계 설치와 포르투갈어 동영상 가이드를 제공하는 Claude Code 모드 마켓플레이스.
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Code의 속도 제한 카운트다운 및 소모 속도 예측.
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - My Claude Code mods.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para o Claude Code: faixa de limites de uso (5h/semanal) e painel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Claude Code 플러그인: 프롬프트 바로 위에서 Claude Pro/Max 사용 한도, 속도 예측, 결제 기간, 토큰 및 $/€ 기준…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code용 모드. agent-crew: 역할, 모델, 현재 도구, 진행률, 토큰 및 시간을 표시하는 실시간 픽셀 크루로…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Claude의 Claude desktop Code 탭 답변에 LaTeX 수식과 선택적 TikZ 도형을 인라인 및 표시 형식으로 렌더링합니다.
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Claude Code용 실시간 작업 보드입니다. 빌드 전에 계획을 세우고, 사이드 패널에서 모든 작업, 상태, 시간, 하위 에이전트 및 검사를…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 최고의 에이전트를 위한 최고의 리소스를 엄선한 컬렉션입니다. 코딩 동반자의 논란의 여지 없는 챔피언인 Claude Code를 비롯해, 막강한…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 컨텍스트 사용량, 활성 도구, 실행 중인 에이전트 및 할 일 진행 상황 등 현재 상황을 보여주는 Claude Code 플러그인입니다.
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline 지원, 테마 등을 제공하는 Claude Code CLI용 아름답고 높은 사용자 지정성을 갖춘 상태 표시줄입니다.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 시스템 프롬프트의 모든 부분, 기본 제공 도구 설명 27개, 하위 에이전트 프롬프트(Plan/Explore/Task)…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 기초부터 고급까지 Claude Code를 최대한 활용하기 위한 45개 이상의 팁을 제공합니다.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — generate Xiaohongshu carousels &amp; WeChat 21:9+1:1…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code를 위한 아름다운 vim 스타일 powerline.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 터미널 창에서 코딩 에이전트의 diff를 검토하고 줄 단위 주석을 Claude Code, Codex, OpenCode 또는 Pi로 보냅니다.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 컨텍스트 사용량, API 속도 제한 및 비용 추적을 포함한 Claude Code용 종합 상태 표시줄 플러그인.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Build mods for Claude Code: Hook any request, modify any response, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - A comprehensive statusline dashboard for Claude Code — session info, quota…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: track the carbon footprint of your Claude Code sessions.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - An aesthetic statusline for Claude Code by awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness용 장편 롤플레잉 agent(DSH 선술집 플러그인): SillyTavern 캐릭터 카드 가져오기, 행동 옵션…
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Public Claude Code skills and mods.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagents, hooks, slash commands and guides for Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 Legal free LLM APIs &amp; coding agents — self-updating, probe-verified twice a…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Claude Code를 위한 빠르고 종속성 없는 비용 계산기 및 사용자 지정 가능한 상태 표시줄입니다.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code 세션용 터미널 상태 표시줄.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 팔로우하는 대회(World Cup, Premier League, LALIGA, Champions League 및 11개 더)의 실시간 축구…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Claude Code를 Windows 및 macOS에서 사용하기 위한 로컬 제어 플레인: 고정 엔드포인트 뒤에서 한 번의 클릭으로 LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill that turns your coding agent into a keyboard firmware expert.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 내부에서 버전 관리되는 개인 Claude Code 구성 — 에이전트, 스킬, 훅, 설정, statusline.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code 안에서 기도 시간, 히즈리 날짜, 아즈카르, 오늘의 아야, 순나 단식, 라마단, 주무아 및 타스비흐를 제공하며, 하나의…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Image generation &amp; visual processing suite for DeepSeek Harness: pluggable…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code용 2줄 truecolor 상태줄(bash + 네이티브 Windows PowerShell): 모델, effort, 컨텍스트…
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - DeepSeek Harness를 위한 피크/비피크 시간 부동 조수 카드: i18n(en/zh/ru), 현지 시간 기준 시간대, 세션 비용을…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - 适用于 Claude Code、pi 和 DeepSeek Harness 的插件合集：状态栏 HUD、任务进度条、Tailscale 节点状态等 ·…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture를 위한 휴대용 Claude Code 툴킷: 엄격한 TDD 에이전트, 계층 규칙, hooks…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 이식 가능한 Claude Code 전역 구성: 사용자 지정 스킬, PreToolUse 후크 및 사용자 지정 상태 표시줄.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 매일 사용하는 Claude Code 플러그인: 어떤 컴퓨터에서든 작동하도록 정리한 skills와 mods입니다.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Unofficial mods for the Code tab of Claude Desktop — usage-pet: a usage band…
- [bbeygel/claude-code-tama](https://github.com/bbeygel/claude-code-tama) - Tama, a Tamagotchi companion mod for Claude Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace for Claude Code Plugins and Skills to facilitate mods of the game…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code를 위한 토큰 거버넌스: 상위 모델이 지시하고, 실행은 충분히 적합한 가장 저렴한 수단으로 전달됩니다.
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code를 위한 실시간 워크플로 단계 상태 표시줄(Plan → Exec → Verify → Done)이며 모델이 자동으로…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repository for Claude Code Awesome Media mods.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude Code 및 Codex 토큰 비용 절감: 조회와 테스트 실행을 더 저렴한 모델로 라우팅하고, 문서를 간결한 Markdown으로…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code를 위한 간단하고 유용한 상태 표시줄 설정.
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Claude Code용 사용량 제한 알림: 세션(5h) 및 주간 제한에 대한 macOS 알림, 앱 내 경고 및 상태 표시줄 백분율.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - 속도 제한, 현재 디렉터리 및 Git 브랜치 정보를 포함한 Claude Code 상태 표시줄을 표시하여 워크스페이스 인식을 향상합니다.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux, WSL, Windows 및 macOS용으로 구성 가능한 Claude Code 상태줄, 프롬프트 타이밍, 서브에이전트 행, 터미널…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code를 위한 빠른 Rust 상태 줄 — payload 우선, 캐시된 git, 약 10ms 렌더링.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Catppuccin 캡슐 스타일 사이드 패널에 컨텍스트 분석, 캐시 적중, 속도 제한 예측, 비용 및 활동을 표시하는 Claude Code용…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code용 상태 줄 및 토큰 줄: 컨텍스트, 속도 표시가 포함된 5시간 및 주간 사용량, 활동, git 및 비용을 표시합니다.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - macOS, Linux, Windows 전반에서 모델, 컨텍스트, 제한, git 정보, 세션 시간을 포함한 Claude Code의 주요 상태…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 다중 행 Claude Code 상태 줄: 비용, 컨텍스트 %, git 및 활성 계정 — 가격과 컨텍스트 창이 자동으로 업데이트됩니다.
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code를 위한 유용한 정보가 있는 Statusline.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 네이티브 에이전트 팀. 통제된 방식으로. Claude Code를 위한 엄격한 작업자 한도, 실시간 팀 가시성 및 이식 가능한 구성.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code 추가 기능: 탭 상태 색상 점 감시기 + 내장 GSD 상태 표시줄.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - herdr 설치 프로그램 플러그인으로 패키징된 macOS 및 Linux용 Claude Code 사용량 상태 줄입니다.
- [alexleveled/claude-read-aloud](https://github.com/alexleveled/claude-read-aloud) - Hear Claude Code.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code용 사용자 지정 상태 표시줄 — 사용률, 컨텍스트 크기, 비용 및 타이머가 표시되는 컨텍스트 막대.
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code를 위한 깔끔하고 유용한 상태 표시줄 — 프로젝트, git 상태, 모델, 세션 시간, 컨텍스트 사용량 및 속도 제한을…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Claude CRT HUD 모드: 터미널과 데스크톱 Code 탭에서 Claude Code용 CRT 스타일 상태 패널을 제공합니다.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - baloo가 포함된 Claude Code 플러그인 마켓플레이스: 스킬, 프로젝트의 결정 사항·지침·검사를 기준으로 변경 사항을 검증하는…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 전문가급 Claude Code statusline: 세션 시간, ECB FX를 적용한 다중 통화 비용, MTok당 요금 및 지출 한도를…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code용 구독 인식 상태 표시줄.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code용 풍부한 터미널 상태 줄 — Bun + TypeScript, 런타임 의존성 없음.
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - 트랜스크립트에 Mermaid 다이어그램을 아름답게 렌더링하는 Claude Code 플러그인: 모든 터미널에서 색상이 적용된 Unicode…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude Code용 도구, 스킬 및 에이전트 — 모델, 브랜치, PR, 컨텍스트 크기, 프롬프트 캐시 잔여 시간 및 비용을 표시하는 상태…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 사용자 지정 상태줄 (모델, effort, 컨텍스트, 캐시, 사용량 한도).
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code의 실제 DeepSeek API 지출: DeepSeek 피크/오프피크 요금으로 세션 트랜스크립트의 가격을 다시 계산하고…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code 내부에서 이미지를 미리 봅니다: 답변 아래 칩 위에 마우스를 올려 그림을 띄우거나, /img &lt;path&gt;로 창에서…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - 에이전트 패널 행이 있는 Claude Code 상태 표시줄.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Claude의 할 일을 Fizzy.do에 동기화하여 팀이 실시간으로 확인할 수 있게 하고, 작업을 영구 카드로 전환해 협업을 강화하고 진행…
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code 설정 메뉴, 상태 표시줄 및 config.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - 컨텍스트, 비용, 기간, git 브랜치, 속도 제한 및 실시간 사용량을 표시하는 간결한 대시보드로 Claude Code 상태 추적.
- [msetsma/claude-style](https://github.com/msetsma/claude-style) - Claude Code style mod: prompt bubbles, tool-call cards and rails, framed bands…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 환경 설치 프로그램: skills, statusline, hooks, permissions 및 선택적…
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code용 HUD 스타일 상태 줄 — 네트워크 상태, TPS, 컨텍스트, 할당량, 비용을 한 줄에 모두 표시.
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude이(가) 수행하는 작업을 이해하기 위한 Claude Code 플러그인 및 모드: 읽기 쉬운 답변 형식과 실시간 세션…
- [pbhwheeler/claude-config](https://github.com/pbhwheeler/claude-config) - Portable Claude Code config: settings.json, hooks, status line, and a bootstrap…
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Claude Code용 다채로운 다중 행 상태 표시줄(할당량 막대, 컨텍스트, 서브에이전트 패널).
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows용 Claude Code 상태줄(PowerShell): 사용량 막대, 속도 경고가 포함된 5시간/7일 재설정 카운트다운, 자동 줄…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - 휴대용 Claude Code 구성(statusline + 설치 프로그램).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code용 소형 대시보드: 컨텍스트 %, 캐시 카운트다운, 5시간 및 주간 사용량, 새 채팅으로의 원클릭 Handoff, 그리고…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code용 사용자 지정 터미널 상태 표시줄: 모델, 디렉터리, git 상태, 컨텍스트 사용량 및 속도 제한.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 포터블 Claude Code 설정: CLAUDE.md, settings, statusline, skills.
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Claude Code desktop(macOS) 모드: 클릭하여 이동하는 세션 알림, 최근 세션 창, 백그라운드 서브에이전트 상태, 토큰…
- [unlocked-spark/claude-code-earshot](https://github.com/unlocked-spark/claude-code-earshot) - Claude Code용 화면 읽기 프로그램 동반 모드(Unlocked Spark Foundation).
- [viplav-artha/claude-code-lessons](https://github.com/viplav-artha/claude-code-lessons) - Claude Code를 실습하며 검증한 심층 안내서 — CLAUDE.md, 하위 에이전트, 스킬, 훅, MCP, mod 등을 실제로 구축하고…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code용 실시간 비용 추적 및 세션 모니터링 상태 줄.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code 스킬(VS Code, Windows): 채팅의 파일 경로 아래 이미지 미리보기 및 열기 버튼, 클릭 가능한 로컬 링크…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - 폴더, git 브랜치, 모델, 컨텍스트 창 사용량 및 플랜 사용량 제한을 표시하는 Claude Code 상태 줄.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code 에이전트를 위한 사전 대응형 AI 메모리 및 속도 제한 모니터.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code 훅, 서브에이전트 및 상태줄: 유형별 오픈 소스 컬렉션과 도구, 각각 보안 등급 제공. English / 中文.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code 상태 표시줄을 위한 시각적 빌더입니다. 브라우저에서 터미널 하단의 막대를 디자인한 다음 명령 하나를 붙여 넣어 설치하세요.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 실시간 토큰 사용량과 예상 에너지 소비량을 표시하는 Claude Code 상태 표시줄.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods for Claude Code: panes, bands and buddies built on function hooks.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Pass tasks between your Claude Code sessions.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - This in a MCP server to control MODS, the modular cross platforms tool for…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Codex and Claude Code skill for translating CK3 mods with a local LLM.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Open-source mods and other extensions for Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code 상태 표시줄: CCometixLine의 미관 + Claude HUD 기능.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: find what you ask Claude Code again and again, and turn it into a…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - prompt-bar mod for Claude Code: usage limits, cache timer + alert, model/effort…

</details>

<a id="dsh-cordis"></a>

## DSH 및 Cordis 플러그인 생태계

DeepSeek Harness와 Cordis는 서로 다른 방향에서 같은 지점에 도달합니다. 이들에게 플러그인은 모드 메커니즘이므로, 그쪽의 플러그인은 이곳의 모드에 해당합니다.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74336 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **74336**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100521 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **100521** |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐91711 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **91711**  |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81929 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **81929**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35760 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **35760**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25495 · Python · 🔎 inferred · 19 天</summary>

##### 📝 요약

Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **25495**  |
| 마지막 푸시 | 2026-09-22 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18380 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **18380**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8629 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **8629**   |
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
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐8510 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **8510**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ebony-vinyl--dsh-our-free-model/212e73dc2aecbd46.png" width="100%" alt="Ebony-Vinyl/dsh-our-free-model screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-market/dsh-market">dsh-market/dsh-market</a></b> · ⭐6159 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 내부의 플러그인 마켓 — 둘러보기, 검색, 원클릭 설치 · DSH 시각화 플러그인 마켓

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **6159**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `deepseek-harness` · `dsh-plugin` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-market--dsh-market/06b60aace017dab8.png" width="100%" alt="dsh-market/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4486 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness（DSH） 인터페이스 오른쪽 아래에 사는 작은 고래 소녀로, DeepSeek 계정 잔액을 지켜봅니다. 말랑하고 통통하며, 드래그하여 붙이기, 왼쪽에 붙일 때 뒤집기, 숫자 스크롤 애니메이션을 지원하고 인터페이스와 함께 자동으로 활성화됩니다. 바로 불러오려면 dsh 설치를 권장합니다

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **4486**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4286 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **4286**   |
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
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4107 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **4107**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>애니메이션 녹화 · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">동영상 열기</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3119 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness Tauri 데스크톱 버전 | 설치 프로그램이 8mb에 불과하고 환경 설정이 필요 없으며, 플러그인이 사전 설정되어 있습니다. Windows / macOS / Linux.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3119**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1406 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **1406**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1171 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **1171**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐704 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **704**    |
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
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐526 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share and search verified debugging experience. | https://misakanet.org

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **526**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐334 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **334**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/user-attachments/assets/7c9ba485-5323-42a2-b5a8-6dcda07f91c4" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐284 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

브라우저를 열기만 하면 모든 작업을 완료할 수 있습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **284**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `dsh` · `dsh-desktop` · `dsh-plugin` · `pi` · `pi-web` · `pi-web-ui`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xing-shuyin--pi-web-ui/926fb8bfa4f6062a.jpg" width="100%" alt="xing-shuyin/pi-web-ui screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
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
| 마지막 푸시 | 2026-10-11 |
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

DeepSeek Harness(dsh)를 위한 시간 이동형 작업 위임: 여유 있을 때 작업을 계획하면 한산한 시간대에 무인으로 실행되고, 돌아오면 보고서를 확인할 수 있습니다. 사람이 판정하며, 데스크톱과 웹을 지원합니다.

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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐133 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

에이전트가 애플리케이션 및 네이티브 코드, GPU 커널, 추론 스택의 병목 지점을 추적하고 프로파일링하며 해결하는 데 도움이 되는 런타임 증거입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **133**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐132 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **132**    |
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
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐120 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 데스크톱 펫 플러그인: 활기찬 고래 소녀 마스코트가 함께 코딩하는 대시보드 🐋 DSH 데스크톱 버전 0.2.0-rc.2 및 구버전 Web 지원 (desktop pet / mascot, local-first)

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **120**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH 플러그인 · 주입형 최적화 도구 0.8(메인라인): 평소처럼 말하면, 전송 후 AI가 수신하기 전에 "이번 요청에서 정확히 무엇을 원하는지" 정리하고 그 이해를 작업 AI에 전달합니다(컨텍스트 주입) — 원문은 다시 작성하지 않으며, 모든 항목에 축어적 근거가 포함됩니다. 제어 인터페이스(등급/권한/모델/컨텍스트/읽기 전용 도구), 가로채기 오버레이(사고 레이어+출력 레이어), 실제 token 사용량을 포함합니다. 대부분의 모델, 특히 DeepSeek-V4.1-Flash의 성능 안정성을 크게 향상할 수 있습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **113**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/JingbiaoMei/Tokdash">JingbiaoMei/Tokdash</a></b> · ⭐85 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

Agent Dashboard: Visualization and analytics for Sessions and Quota Usage. Track, analyze, and optimize token usage across providers with heatmaps, cost tracking, token counting and quota resets..

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **85**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent` · `analytics` · `anthropic` · `claude-code` · `claude-code-plugin` · `codex` · `codex-cli` · `dashboard`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jingbiaomei--tokdash/cb7e85100dfe6e93.png" width="100%" alt="JingbiaoMei/Tokdash screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐66 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **66**     |
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
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

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
| 스타        | **59**     |
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

dsh-agent-team gives DeepSeek Harness agents that don't reset: durable Members with their own memory, notes, and skills across sessions, rollovers, and restarts. You set the direction; agents coordinate through Channels and Tasks.

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
<summary>🧵 <b><a href="https://github.com/universe-st/dsh-game-material-master">universe-st/dsh-game-material-master</a></b> · ⭐43 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

dsh 게임 소재 마스터 플러그인입니다. seedream 이미지 생성 모델과 minimax 동영상 생성 모델을 연동하여 다양한 게임 소재를 생성할 수 있습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **43**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `chroma-key` · `cordis` · `deepseek-harness` · `dsh-plugin` · `ffmpeg` · `game-assets` · `image-generation` · `koishi`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/universe-st--dsh-game-material-master/9ce5badff3c3ac1c.png" width="100%" alt="universe-st/dsh-game-material-master screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 67</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - A pre-execution guard for AI coding agents.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH 플러그인 — DeepSeek Harness(DSH)에서 사용할 수 있는 무료 OpenCode Zen 모델입니다.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 플러그인 마켓 / DSH Plugin Marketplace: DeepSeek Harness Web GUI에서 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 스스로 반복 개선하는 소프트웨어를 위한 플러그인 런타임 — 에이전트가 Rust, TypeScript, Python 및 Go에서 프로세스와…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [PensiveFei/dsh-secure-audit](https://github.com/PensiveFei/dsh-secure-audit) - Read-only security &amp; compliance plugin for DeepSeek Harness: prompt-injection…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 플러그인 엄선 디렉터리 — MCP / Skill / TUI / 멀티 Agent / 컨텍스트 메모리 /…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 플러그인: llm-pi-ai 모델의 정확한 컨텍스트 창을 유지하여 긴 세션이 컨텍스트 초과로 잘못 판단되는 것을…
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness용 Zotero toolkit입니다. Zotero 라이브러리를 에이전트를 위한 증거 저장소로 바꿔 줍니다.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Windows의 모든 에이전트 모드를 위한 DSH 플러그인: Git Bash 셸(pwsh 실행기 대체).
- [PensiveFei/deep-read-summarize](https://github.com/PensiveFei/deep-read-summarize) - 도서/논문/동영상/웹 콘텐츠를 위한 심층 읽기 및 요약 워크플로 — 플러그인 파서, MapReduce 심층 읽기, JSON Schema 출력…
- [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) - 让你的 DSH，火力全开。长上下文、任务验证、提示词优化、代码理解、电脑操作与四套完整主题.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH 웹 플러그인: VSCode Remote-SSH와 유사한 원격 개발(SSH, 원격 워크스페이스, 파일 탐색기, 통합 터미널).
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness（DSH）기반 멀티 플랫폼 그룹 채팅 지능형 에이전트 시스템｜DSH 기반 멀티 플랫폼 그룹 채팅…
- [omdsh-dev/dsh-office](https://github.com/omdsh-dev/dsh-office) - 업무 필수 도구 3종 세트! DeepSeek Harness (dsh)용 Office 문서 도구 — 스프레드시트 (.xlsx), PDF 및…
- [zaofan-make/dsh-qqbot](https://github.com/zaofan-make/dsh-qqbot) - AI 统管 QQ 群组：审核放行、群发文件、沟通其他 web 会话的 AI！ ；气氛组担当：表情包自动入库、AI 自己决定开口、多预设多人格轮班陪聊!
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh Android 버전: DeepSeek Harness, Ubuntu 실행 환경, 플러그인 및 파일 관리자를 통합하고, 사용자가 승인한…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH(DeepSeek Harness) 웹 GUI 플러그인 모음 — 작업 알림, 공급자 사용량, LAN 프록시, MCP 관리자…
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - DSH 세션 탐색.
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH 웹 플러그인: GitHub 스타일 활동 히트맵, 캐시 적중률 곡선 및 모델별 분석을 제공하는 일일 토큰 사용량 통계.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 커뮤니티가 엄선한 DeepSeek Harness(dsh) 플러그인, 도구, 스킬 및 학습 자료입니다.
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness용 MCP 서버 관리자 플러그인: 설정 → MCP 페이지, OAuth(PKCE + 동적 클라이언트 등록) 또는…
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness 플러그인: 15개의 obra/superpowers 엔지니어링 스킬, 이중 언어 설명, 스킬별 토글 |…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A 상거래 협상 런타임 + DeepSeek Harness(dsh) 플러그인입니다.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Toolbox panel for DeepSeek Harness Web: MCP manager.
- [mistnest/dsh-cuigengji-plugin](https://github.com/mistnest/dsh-cuigengji-plugin) - 업데이트 재촉 요정: 大肥鱼에게 소설 작업대를 제공합니다. 본문을 쓰고, 설정을 정리하고, 줄거리를 그리며, AI와 함께 토론하고 이어 쓰고…
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 플러그인 · 전송栏에서 한 번의 클릭으로 프롬프트 초안 「최적화」: 5차원 진단 + SSE 스트리밍으로 표시되는…
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML이 아닌 진짜 PowerPoint입니다. AI에게 다룰 내용을 말하면 pptwise가 자신의 컴퓨터에서 편집 가능한 덱을 만듭니다.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 임베디드 C/C++ AI 엔지니어링 플러그인 — 펌웨어 스킬(FreeRTOS, Keil, HardFault, 상태 머신) + 1% Rule /…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [Sivan757/dsh-agent-plugins-market](https://github.com/Sivan757/dsh-agent-plugins-market) - DeepSeek Harness(DSH)를 위한 올인원 skills, subagent, MCP 및 LSP 관리자 — Claude Code…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [sueccku/dsh-plugin-wps-office-next](https://github.com/sueccku/dsh-plugin-wps-office-next) - 在 DeepSeek Harness（DSH）里用中文对话操作 WPS 表格 / 文字 / 演示：读写数据、排版、公式图表、批量转 PDF.
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 플러그인을 위한 상시 호환성 테스트: 정확한 릴리스, 격리된 러너, 수정 가능한 업스트림 이슈.
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - 로컬 우선 에이전트를 위한 공격적인 컨텍스트 압축입니다. 자체 호스팅 llama.cpp에서 Qwen3.8‑27B를 낮은 컨텍스트로 실행하고…
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [chengshenyangtai/dsh-workbuddy-trae-qoder-connect](https://github.com/chengshenyangtai/dsh-workbuddy-trae-qoder-connect) - 把 WorkBuddy（多账号/企业版）、Trae CN / TRAE SOLO CN、Qoder CN 三家订阅聚合进同一个 DSH…
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 플러그인을 위한 X-ray: 선언된 기능과 실제 동작을 비교합니다. 레지스트리 + 정적 스캐너 + 배지.
- [zzhang82/Agent-Memory-Bridge](https://github.com/zzhang82/Agent-Memory-Bridge) - Persistent engineering memory for coding agents over MCP.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - DSH 플러그인: WorkBuddy 데스크톱 App의 모델을 DeepSeek Harness에 연결하여 설정 없이 바로 사용할 수 있습니다.
- [lkhfrgc/scholar-llm-wiki](https://github.com/lkhfrgc/scholar-llm-wiki) - 연구 및 문헌 검토를 위한 지식 베이스 도구 모음입니다. AI 에이전트가 논문, 도서 및 노트를 구조화되고 촘촘하게 연결된 Obsidian…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、输入框分支标记…
- [xyrrrrr-r/dsh-eval-control](https://github.com/xyrrrrr-r/dsh-eval-control) - Host-side DSH evaluation control plugin for aeval：一次评测试次的配置注入、预算封顶与证据归属.
- [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) - 설계 및 코드의 주장 검증: 사실 주장은 소스 코드와 대조하고, 행동 주장은 실행 가능한 모델로 검증하며, 구조/종속성 검토.
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 다중 폴더 workspace: DSH(DeepSeek Harness)의 Agent가 기본 디렉터리뿐 아니라 추가한 다른 폴더도 동시에 읽고 쓸…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness(dsh) 플러그인을 위한 종속성 없는 검증 표준 — 정적 구조 게이트(R), cordis 계약 검사(K)…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) plugin: one-click OpenCode Go model sync in the settings…
- [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) - 提供 Grok-compatible 网页搜索、保留来源分页、Context7 与 Exa 文档检索、有界网页提取、站点映射、离线研究计划和只读诊断.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness의 OpenCode — OpenCode Zen + Go 무료 티어 모델을 계속 작동하게 하는 DSH 플러그인…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness를 위한 서드파티 플러그인 마켓플레이스 및 보호된 수명 주기 관리자.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx는 사람을 중심으로 설계된 확장 가능한 데스크톱 작업 공간입니다.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness를 위한 모든 기능이 포함된 코딩 에이전트 — Claude Code 스타일 워크플로, 원하는 모델, TUI…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh)를 위한 커뮤니티 버전 로컬 배포·운영 도구 모음: 설치 / 시작 / 모니터링…
- [SuperWheel/cliworker-now](https://github.com/SuperWheel/cliworker-now) - DeepSeek Harness 多 CLI 智能体侧栏插件：独立对话、账号管理、角色预设与任务续聊.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness(DSH) 웹 플러그인: 시장 대시보드 사이드바 탭을 모니터링합니다 — 마우스를 올리면 장중 차트가 표시되는…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 출처가 표시되지 않은 빈 모델 시도를 재시도 가능하게 만듭니다. 이를 판별할 수 있는 하나의 접점.
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 스스로 정리하는 플러그인: iOS 및 macOS용 cordis 플러그인 프레임워크의 Swift 6 포트.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness 에이전트 프리셋: Codex 및 Claude Code를 위임 하위 에이전트로 사용하며, 각각 읽기 전용 및 전체…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus-verified 라이프사이클 커널과 Cordis 호환성 어댑터를 갖춘 Rust 플러그인 런타임입니다.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [ArisaYamatogi/dsh-lecture-copilot](https://github.com/ArisaYamatogi/dsh-lecture-copilot) - A Dsh plugin that automatically records, translates lecture and generates notes…

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

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
| TypeScript | 338  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 79   | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 40   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 24   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 12   | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 5    | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 5    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| PowerShell | 2    | `GoSlowPoke168/claude-statusline`, `rainyfei/claude-statusline-win`                                           |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1    | `dphmoblie/deepseek-harness-android`                                                                          |
| Swift      | 1    | `eovidiu/cordis-ios`                                                                                          |

<sub>언어를 명시한 항목만 집계됩니다. 문서 및 토론 항목은 이 표에서 제외됩니다.</sub>

## 기여

수정 사항을 제보해 주시면 이 목록을 가장 빠르게 개선할 수 있습니다. 항목이 잘못 분류되었거나, 등급이 잘못 매겨졌거나, 이름 충돌로 인해 프로젝트가 잘못 제외되었다면 이슈 또는 풀 리퀘스트를 열어 주세요. 마지막 유형은 자동 필터가 가장 자주 잘못 판단하는 경우입니다.

---

<sub>독립적인 커뮤니티 프로젝트입니다. Anthropic와(과) 제휴, 승인 또는 검토를 거치지 않았습니다. Claude Code, Claude 및 Anthropic은(는) Anthropic의 상표입니다. 제품 동작은 예고 없이 변경될 수 있으므로, 중요한 내용은 공식 문서에서 확인하세요. 에셋은 원 프로젝트의 자산으로 남으며, 라이선스가 허용하는 경우에만 재현됩니다.</sub>

<sub>마지막 업데이트 · 2026-10-11T23:26:48+08:00</sub>
