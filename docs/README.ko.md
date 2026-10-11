<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="멋진 Claude 모드">
</p>

<h1 align="center">멋진 Claude 모드</h1>

<p align="center"><b>Claude Code 모드와 플러그인, 그리고 이들이 변경하는 더 심층적인 동작을 근거에 따라 등급화한 색인입니다.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-591-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **실시간 색인** · 마지막 동기화: `2026-10-12T06:04:10+08:00` (UTC+8)
> · 항목: **591** · 최신 업데이트에 추가됨: **0** · 구현 언어: **12**

<sub>아래의 모든 항목은 자동으로 수집, 필터링 및 재검증되었습니다. 유료 게재 항목은 없습니다.</sub>

<a id="featured"></a>

## 지금 주목할 항목

<sub>카테고리별 항목 하나를 근거 등급과 별점에 따라 순위를 매겨 선택하며, 업데이트할 때마다 다시 계산합니다. 추천이 아닌 순위이며, 모든 항목은 아래의 전체 카드로 연결됩니다. 스크린샷이나 녹화본을 게시한 프로젝트를 우선하므로 목록이 시각적으로 유지됩니다.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9479 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>유령 토큰을 찾으세요. 수정하세요. 압축을 견디세요. 컨텍스트 품질 저하를 피하세요.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74358 · TypeScript · 👁️ observed</sub>
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
- [모드: 모드 기능으로 구축됨](#모드-모드-기능으로-구축됨) — **460**
- [DSH 및 Cordis 플러그인 생태계](#dsh-및-cordis-플러그인-생태계) — **106**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150215 · TypeScript · ✅ official · 0 天</summary>

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
| 스타        | **150215** |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9479 · TypeScript · ✅ official · 2 天</summary>

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
| 스타        | **9479**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

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
| 스타        | **8249**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6346 · Python · ✅ official · 242 天</summary>

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
| 스타        | **6346**   |
| 마지막 푸시 | 2026-02-11 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

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
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

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
| 스타        | **2535**   |
| 마지막 푸시 | 2026-10-11 |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐497 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

GitHub에서 스캔한 공개 Claude Code mods(function hooks)의 커뮤니티 카탈로그로, 각 mod가 네트워크를 통해 읽기, 쓰기, 실행 또는 전송할 수 있는 항목을 표시합니다. https://mods.aidojo.si/ 찾아보기

<sub>🔧 코드에서 사용된 항목: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **497**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐188 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **188**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐142 · TypeScript · 👁️ observed · 7 天</summary>

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
| 스타        | **142**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐99 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Skins for Claude Code: tool rows with icons, diff, table and Mermaid chart cards, a usage band and fifteen themes. /skin swaps them live.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **99**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐91 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **91**     |
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
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐78 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **78**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

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
| 스타        | **78**     |
| 마지막 푸시 | 2026-10-08 |
| 최초 등록   | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 9 天</summary>

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
| 스타        | **67**     |
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
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 6 天</summary>

##### 📝 요약

Darrell Wang의 Claude Code 모드 — 모델 토큰을 전혀 사용하지 않고 프롬프트 위에 밴드를 표시합니다. 대만 주식／미국 주식 대시보드 + 앞으로 더 추가될 예정입니다.

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

Claude Code용 전문가 Skills, 에이전트, 명령, 규칙, 훅 및 출력 스타일 — 세션 연속성 + 실제 개발 워크플로를 위한 최신 CLI 도구

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
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 요약

Claude Code 모드: 프롬프트 위에 실시간 계획 진행률 표시줄을 표시합니다

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

Claude Code에서 프롬프트 위에 살아가는 픽셀 Pokémon

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

Claude Code 안에서 Xcode의 빌드, 테스트, 콘솔 및 SwiftUI 미리보기를 제공합니다

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/SavaSoftworks/BitFrost">SavaSoftworks/BitFrost</a></b> · ⭐16 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Use Codex, GLM, and other coding agents as Claude Code subagents.

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | TypeScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **16**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `agent-orchestration` · `ai-agents` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `codex` · `developer-tools` · `glm`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/savasoftworks--bitfrost/247eb6d28062ba3b.png" width="100%" alt="SavaSoftworks/BitFrost screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/paulbkim-dev/claude-code-cache-warmer">paulbkim-dev/claude-code-cache-warmer</a></b> · ⭐13 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 요약

Claude Code mod that keeps the prompt cache warm and shows each refresh's cost and saving

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
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `claude-code` · `claude-code-plugin` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/paulbkim-dev--claude-code-cache-warmer/5d291d279a3967a1.gif" width="100%" alt="paulbkim-dev/claude-code-cache-warmer animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 426</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Claude Code에서 사용할 수 있는 100개 이상의 모음 모드입니다.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 및 이를 빌드하기 위한 도구: 먼저 builder skill을 제공한 다음 mods를 제공합니다.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 제가 매일 실행하는 Claude Code harness입니다. 첫날부터 이 이름으로 공개되었으며 현재 ucsandman/Agnostic-AI와…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods로 Claude Code에 지붕을 씌우세요. 바이너리를 수정하지 않고 시스템 프롬프트와 영어 알림을 원하는 문구로…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Claude Code 모드 4개: Cache Keeper, Recording Mode, Goal Meter 및 Collision Guard.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker의 Claude Code 모드: 에이전트의 작동을 이해하기 쉬운 형태로 시각화합니다.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude이 읽기 전에 프롬프트를 수정하고 번역하는 Claude Code 모드.
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - 지속적인 집에 거주하는 AI들이 매일 구축하고 사용하는 Nekyia Labs의 Claude Code 모드와 스킬.
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Claude Code 터미널 기록을 데스크톱 앱처럼 보이게 하는 모드.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code용 사이드 패널: 세션에서 실행하는 서브에이전트, 각 에이전트가 하는 일, 토큰 및 대화를 클릭 한 번으로 확인할 수…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude에 관한 출처가 인용된 Obsidian 지식 베이스: Code 모드의 작동 방식, 빌드 방법, 설치 전 확인 방법.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop(Code 탭) 사이드바 패널: 모든 Claude Code session의 미완료 및 진행 중인 할 일을 나열하고…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code 에이전트에게 Claude Mods(함수 훅 플러그인)를 빌드하는 방법을 가르치는 스킬과 시작 예제.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop(Code 탭) 입력 상자 위의 사용량 막대: 5h / 7d 할당량, token 사용량, 비용.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 하나의 마켓플레이스에서 설치할 수 있는 커뮤니티 Claude 모드, 플러그인 및 스킬.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code용 Claude Mods(함수 훅 플러그인).
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane 모드 갤러리: 검토 및 고정된 Claude Code 모드.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 대화형 에이전트와 협업하는 사람을 위한 의사 결정 큐 CLI/TUI. 에이전트가 질문을 올리면 사람은 하나의 받은 편지함에서 답합니다.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Claude Code 모드: 픽셀 게의 사용량 패널 usage-hud + 터미널에서 클릭할 수 있는 HTML 링크와 한 번의 클릭으로 코드를…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code용 플로팅 상태 카드 — 모델, 컨텍스트, 속도 제한, 비용, 브랜치 — 그리고 모든 스크립트나 mod가 값을 전달할 수…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Claude Code용 Mods: 터미널 UI에 실시간 창과 동작을 추가하는 함수 후크 플러그인.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code 모드: screen-guard는 화면을 공유하는 동안 이름과 비밀 정보를 가리고, cache-panel은 프롬프트 캐시가…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Claude Code용 실시간 GSD 대시보드: 로드맵, 분기 기능이 있는 에이전트 트리, 컨텍스트와 비용, 작업 스트림 및…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code 확장 기능. Claude의 모든 기능을 활용하세요.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Activity, Files, Agents, Context 및 MCP 탭이 있는 사이드 패널, 프롬프트 위의 상태 줄, 새롭게 스타일링된…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Claude Code용 패널, 가드레일 및 사용 편의성 모드: 컨텍스트, 사용량, 실시간 활동, 알림, 안전 규칙, 프롬프트 코치, 명령 허브.
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - 프롬프트 상자 위에 표시되는 두 개의 Claude Code 모드: 컨텍스트 창 미터, 5시간 제한, 프롬프트 시계 및 세션 비용.
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Claude Pro 플랜을 더 오래 사용하세요: 정확한 사용량 HUD, 더 짧은 셸 출력 및 반복 파일 읽기 방지를 위한 Claude Code…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Claude Code가 이름을 지정한 markdown 파일을 읽어 세션 옆에 렌더링하고, 블록을 가리키면 Claude가 해당 블록을 편집하도록…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Claude Code용 음성 동료. ElevenLabs conversational AI로 구동되는 3D 늑대와 대화하며 생각을 정리하세요.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Claude Code 모드: typing-speed, 프롬프트별 통계가 제공되는 실시간 타이핑 속도계.
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Claude Code용 불꽃놀이: 모든 키 입력, 도구 호출, 커밋 및 통과한 테스트가 프롬프트 위에서 점자 불꽃놀이로 올라갑니다.
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - 애니메이션 데모, 카테고리 목록 및 직접적인 소스 링크로 Claude Code 모드, 플러그인 및 확장 기능을 찾아보세요.
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Claude Code 모드: transcript 안에 인라인으로 그려지는 mermaid 다이어그램.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code용 모드 및 스킨: Claude의 작업을 위한 실시간 진행률 표시줄, 이에 어울리는 Windows Terminal 스타일의…
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - 작은 Claude Code 모드(함수 훅 플러그인): session-switcher 등.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Claude Code 모드: 모든 터미널에서 프롬프트 위에 표시되는 붙여넣은 이미지 썸네일.
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Claude Code 모드: Claude Tools 메뉴, Zen 모드, 터미널 테마, 작업량 및 모드 제어.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Claude Code 모드: mod-scout(가장 많이 사용할 모드 찾기), usage-meter, check-ledger…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - 여러 세션을 동시에 실행하기 위한 두 개의 Claude Code 모드: 프롬프트 위의 컨텍스트 카드와 채팅 옆의 세션 창.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: Claude Code 모드 검색, 검사, 전환 및 업데이트.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code 모드: 컨텍스트 바, 에이전트 패널, PDPA 블러.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - 최고의 Claude Code 모드: 엄선, 검증 및 고정됨. /plugin marketplace를 한 번 추가하면 43개의 모드 제공.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Claude Code 플러그인: 자동 Claude 모델 라우팅. 프롬프트, 단계, subagent마다 Haiku, Sonnet 또는 Opus와…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Claude Code용 여섯 가지 모드: 애니메이션 Clawd 마스코트, 사용량 제한 및 프롬프트 캐시 바, 전송 전 메시지 검사기, 빠른…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Claude Code용 모드 마켓플레이스: 에이전트 루프용 단계 디버거, git 계정 힌트, worktree 상태 표시줄 등.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 여섯 가지 Claude Code mod: 프롬프트 위에 플랜 제한과 컨텍스트를 표시하고, 권한 프롬프트를 위한 허용 목록 코치, 서브에이전트…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - Claude Code용 최고의 올인원 mod pack: 사용량 제한과 context HUD, rm -rf 및 git reset --hard를…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Claude Code에서 YouTube Shorts를 재생하세요 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Naren의 Claude 툴킷: Claude Code용 skills, mods 및 MCP servers.
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Edit 및 Write diff를 나란히 놓인 두 열에 그리는 Claude Code 모드.
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code용 모드: Claude이(가) 수행 중인 작업을 연기하는 작은 픽셀 마스코트 Clawd.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code 모드로 즐기는 클래식 데스크톱 게임. Claude이(가) 작업하는 동안 창에서 플레이할 수 있습니다.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 플러그인 마켓플레이스로 설치할 수 있는 엄선된 Claude Code 모음: 테마, 창, 상태 표시줄, 초상화.
- [timoncool/givememod](https://github.com/timoncool/givememod) - 필요할 때 사용하는 Claude Code 모드 — 대화를 읽고 적합한 모드를 만드는 스킬: 계획 진행률 표시줄, 파일 창, 컨텍스트 게이지…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - 하네스 엔지니어링에 집착하는 Rustacean이 설계한 매우 주관적인 Claude Code 플러그인.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 에이전트가 정직하게 작업하도록 하는 Claude Code 모드 — 범위를 보호하고 배포를 검증하며 프롬프트 위에 세션을 표시하는 함수 훅.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - 내 Claude Code 모음 모드로, 디렉터리마다 하나의 모드가 있습니다.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Claude Code를 위한 수동 공격형 물 마시기 알림. 토큰은 0개, 판단은 최대치.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - 내가 사용하는 Claude Code 모드입니다.
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: 에이전트 그래프를 설계하고 실행하기 위한 Claude Code 모드(software factory).
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code용 macOS notch 대시보드: 사용량 제한, 열린 세션, 작업 진행률, 프롬프트 캐시 카운트다운 및 할 일 — 다섯…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Claude이(가) 작동하는 동안 시간을 보내기 위한 타자 연습 테스트입니다. Claude Code 모드입니다.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code용 모드: 프롬프트 캐시 표시줄, 다음 단계, 빠른 버튼 및 변경 사항 리플레이 — marketplace에서 설치 가능.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Claude Code용 모드: 플러그인 function-hooks API로 구축한 창, 명령 및 훅.
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - 거대한 도구 출력을 Claude Code의 컨텍스트가 가득 차기 전에 잘라냅니다.
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Claude Code의 프롬프트 하단과 프롬프트 위에서 프롬프트 캐시, 컨텍스트 및 계획 한도를 한눈에 확인.
- [Elesiann/usagemeter](https://github.com/Elesiann/usagemeter) - Cost, tokens and plan limits of your coding agents.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 프롬프트 위 표시줄에 사용량 한도와 지출을 그려 주는 Claude Code 모드.
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman의 Claude Code 모드 (마켓플레이스 herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code 모드: 계획용 진행률 표시줄, Claude이(가) 실행 상태로 남겨 둔 항목의 원장, 도구 출력용 토큰 마스킹.
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code가 백그라운드에서 실행하는 항목을 확인하세요: 서브에이전트, Codex 작업, 셸, 모니터, cron 작업 및…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs의 Claude Code 모드: streams가 세션의 뒤섞인 작업을 색상으로 구분된 스트림으로 정리합니다.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows에서의 Claude Code 모드에 대한 첫날 현장 노트: 컨텍스트/할당량 연료 표시줄, Thai UI 모드, Matrix 부팅…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - 내 Claude Code 설정에서 직접 만들고 개인적으로 사용하는 모드.
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: Claude Code 도구 호출을 위한 디버거입니다.
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Claude Code 모드: 프롬프트 캐시가 만료되는 시점과 만료 시 발생할 비용을 보여 주며, keep-alive 핑으로 캐시를 따뜻하게…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code 모드: 프롬프트 위에 실시간 비용, 컨텍스트 및 플랜 할당량 미터를 표시합니다. 아이콘에는 Nerd Font가 필요합니다.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 하위 에이전트 확장, 대규모 컨텍스트 프롬프트 및 재시도 루프가 사용량 창을 소모하기 전에 보류하는 Claude Code 모드입니다.
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 5개 팩(foundation, scribe, warden, localops, gamedev)으로 구성된 Claude용 Agent Skills…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude용 code-mods.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 명명된 프로필을 사용해 저장소별로 전역 스킬, 에이전트, 규칙 및 도구를 켜거나 끄는 Claude Code 모드입니다.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 플러그인(모드): 여러 Claude 계정 간 전환, 상태 밴드에서 사용량 제한 확인, 터미널 패널에서 에이전트…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 테스트 완료, 한 번의 명령으로 설치 가능한 Claude Code 모드: YOLO 모드용 가드레일, 실시간 비용 및 컨텍스트, 패널, 펫…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code용 모드: function hooks를 기반으로 구축한 플러그인.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - 코딩 세션을 위한 영화 스타일 크레딧. 모델 호출이나 텔레메트리가 없는 네이티브 Claude Mod입니다.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - 내 Claude Code 모드 플러그인 marketplace.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 내가 만든 claude code 모음 모드.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods. touch-map: Claude가 나열, 읽기, 편집 또는 생성한 파일을 트리와 activity map으로…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code로 작업하면서 외국어를 익히세요.
- [20alexl/windvane](https://github.com/20alexl/windvane) - Babysits a long Claude Code session so you don.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - 하나의 관제탑에서 여러 저장소의 여러 세션을 실행하기 위한 Claude Code 모드.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code용 실시간 비용, 토큰, 컨텍스트 사용량 사이드바: 세션 내에서 턴별 비용, 캐시 적중률, burn rate, 30일…
- [atharv6f/headway](https://github.com/atharv6f/headway) - 설정 없이 Claude Code 프롬프트 위에 목표, 작업 및 에이전트를 표시합니다. Claude Code 모드입니다.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Claude Code 안의 인터넷 라디오: cliamp 사이드바, 미니 플레이어, 즐겨찾기, 탐색, 집중 모드 및 Claude용 라디오 도구.
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - 재미있고 유용한 Claude Code 모드: 프롬프트 위에 픽셀 생물이 표시되고, Agent Dock이 포함된 도구 메뉴, 프로젝트 상자 및…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude가 요리 중입니다. 팀과 채팅하세요. 친구들이 온라인에서 Claude Code 세션 바로 옆에 있습니다.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - 진정한 엔지니어를 위한 Claude Code 모드.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude 데스크톱 앱의 Code 탭에 표시되는 Claude Code 터미널 세션 요약입니다(Claude Code 모드).
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code가 작업하는 동안 프롬프트 위에서 펼쳐지는 우주 전투.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 각 Claude Code 에이전트가 컨텍스트에 어떤 파일을 가지고 있는지, 그리고 각각 얼마나 있는지 확인하세요.
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - 세션의 메모리, CPU 및 가동 시간을 표시하는 상태 표시줄이 있는 Claude Code 모드.
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 냉정함을 유지하세요. Claude Code 사용일을 위한 온도계입니다.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 터미널 및 데스크톱 앱용 소형 Claude Code 모드.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code 모드(플러그인 마켓플레이스): 컨텍스트, 비용 및 사용량 게이지가 표시되는 실시간 사이드바.
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Claude Code mod: 작업, 서브에이전트, 워크플로 실행, 목표 및 도구 호출을 위한 진행 창을 제공하며 막대, 타임스탬프 및 남은…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Claude Code mod: 프롬프트 위에 플랜 속도 제한, 컨텍스트 사용량, 세션 비용 및 작업별 토큰을 색상 막대로 표시합니다.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - 에이전트 응답에 스페인어 단어를 추가하는 Claude CLI skill + mod.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Claude Code의 프롬프트 위에 표시되는 Alarum 이벤트: 방금 도착한 항목과 한 번 눌러 에이전트에 전달하는 기능.
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Claude Code의 프롬프트 위에 Floatee 백로그를 표시하여 한 번의 클릭으로 할 일을 실행하고 안내하며 완료 처리합니다.
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code용 Evangelion 스타일 사이드바: 컨텍스트, 할당량, 활동, PR, 하드웨어, 세션 및 forge 패널.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 이를 Person of Interest의 The Machine처럼 재스타일링하는 Claude Code 모드입니다.
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: 라이브 DAG 패널을 제공하는 서브에이전트의 필수 검증 DAG 워크플로용 Claude Code 모드.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code를 위한 오픈 소스 모드: 창, 상태 줄, 토스트, 도구 가드 및 슬래시 명령.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 각 서브에이전트와 해당 에이전트가 건드리는 파일, 그리고 세션의 사용량과 비용을 위한 패널을 제공하는 Claude Code 모드입니다.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: 세션 상태, 실시간 Spec Kit 진행 상황 및 사용량 창 거버넌스.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 프롬프트 위에 한 줄로 표시되는 컨텍스트 창으로, Claude Code가 자체 미터를 그리는 방식으로 표현됩니다.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop용 실시간 작업 HUD: Claude이(가) 작업하는 동안 프롬프트 위에 표시되는 스트립과, 한 번 클릭하면…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Claude Code를 위한 무료 오픈 소스 플러그인입니다. /clear를 실행하기 전에 Claude이(가) 읽고 편집할 수 있는 짧은 인계…
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - 나중에 사용할 프롬프트를 보관하고 Claude Code의 입력 상자에 다시 표시합니다. 즉시 처리되며 모델 호출이 없습니다.
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Ghostty 및 kitty에 이미지를 인라인으로 표시하는 Claude Code 모드.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 세션의 GitHub개 풀 리퀘스트를 트랜스크립트 옆 창에 표시하는 Claude 모드: 설명을 프롬프트 상자에 인용하고 검사 및 리뷰 상태를…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code 모드: 자동 인계 및 진행률 표시줄입니다. 터키어이며 몇 가지 명령으로 설치됩니다.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Claude Code 모드: 로컬 Stable Audio 모델(sa3.cpp)로 텍스트 프롬프트에서 음향 효과를 생성합니다.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code 스킬: 문서 팩트체커, 코드 감사기, 버그 메모리 로그, 모드 등.
- [ondrhn/sharpprompt](https://github.com/ondrhn/sharpprompt) - Claude Code mod that rewrites rough prompts into clear ones before you send…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Claude Code mod: 모든 세션에서 Claude이(가) 작성한 오늘의 코드 줄 — 새로 추가됨, 수정됨, 삭제됨 — 을 표시하고…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Claude Code mod: 답변의 클릭 가능한 경로 — 폴더를 클릭하면 Finder에서 열고, 파일 이름을 클릭하면 파일을 엽니다.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 버디 플러그인: 프롬프트 위에서 규칙을 기억하고 Claude의 단축키를 알려 주는 ASCII 동반자.
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code 모드: Jev에 기반한 모델/추론량 라우팅, 축어적 컨텍스트 압축 및 출력 트리밍으로 긴 세션의 비용을 절감합니다.
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code 모드: Claude Code를 위한 보안 계층 — 비밀 정보 마스킹, 신뢰할 수 없는 콘텐츠 알림, MCP 도구 오염…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Claude Code 모음입니다.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 플러그인 및 모드: 훅으로 강제되는 인간 승인 게이트와 프롬프트 위 상태 표시줄을 갖춘 AI 네이티브…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods 컬렉션 | 클로드 코드 모드 모음집.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code 모드: 일상 작업을 위한 실시간 패널 및 훅.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: 로컬 오픈 소스 Kokoro TTS 음성으로 요청 시 Claude의 답변과 사용자의 프롬프트를 소리 내어 읽어주는…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Claude이 실수하면 때려 주세요 — Claude Code를 위한 스트레스 해소용 mod: 만화풍 엉덩이, 8개 때리기, 9개 엉덩이…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - 실시간 창, 비용을 고려한 모델 라우팅 및 안전 가드를 위한 Claude Code 모드: 한 번의 명령으로 마켓플레이스에서 설치하세요.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code 모드 및 플러그인: 사용량 모니터, 토큰 추적기 및 상태 줄.
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - 작은 결정을 저렴한 의사 결정 모델에 맡기는 Claude Code 모드입니다: 라우팅, skills, 주입 검사, /compact-jev.
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Claude Code 모드: Claude이 변경한 파일과 그 이유, 실시간 서브에이전트 상태 및 남은 플랜 한도를 보고.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - afterever의 Claude Code 모드(플러그인 마켓플레이스).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code 모드: 각 하위 에이전트를 TypeSafe Jev이(가) 판단한 가장 저렴한 Claude 모델로 라우팅합니다.
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Claude Code 모드: 프롬프트 위에 세션 통계 카드를 표시합니다.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 프롬프트 위에 표시되는 애니메이션 점자 고양이.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code 모드: 저렴한 작업은 하위 Claude Code를 통해 GLM/Kimi로 라우팅하고, 중요한 작업은 구독에서 유지합니다.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - OmniDimension 음성 에이전트 테스트 호출을 실행하는 Claude Code 프롬프트 위의 픽셀 고양이. Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 컨텍스트 창을 작게 유지할 수 있도록 압축하기 좋은 시점을 선택하는 Claude Code 모드.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code용 Claude Mods: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider의 Claude Code 플러그인 마켓플레이스.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Claude Code용 범용 모드: bands, panes, toasts 및 hooks.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - 내 비공개 Claude Code 모드.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 주간 페이스 경고가 포함된 애니메이션 주민 체력 카드로 표시하는 사용자의 Claude 사용 한도 — Claude Code 모드.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 팀을 위한 Claude Code 모드(the ather marketplace).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - Claude이(가) 평이한 영어로 작성하도록 하고 일반적인 글쓰기 습관을 표시하는 Claude Code 모드입니다.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude이 작업하는 동안 하는 짧은 운동: 일일 목표, 연속 기록, 배지 및 선택적 리더보드. Claude Code 모드.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code용 사용량 보드: 모델별 지출(오늘, 이번 주, 이번 달, 전체 기간) 및 주간 한도 예측.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Claude Code 모드: 프롬프트 위에 실시간 컨텍스트 창 분석을 표시합니다.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code용 Now Playing mod: 프롬프트 위에 앨범 아트, 컨트롤 및 Up next 창과 함께 표시되는 Apple…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code용 모드: 캐시 시계, Blast Radius, 제안, 작업 목록, Grill.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 당신의 Claude Code를 위한 그냥 올빼미.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 한 줄짜리 Claude Code 밴드(캐시 카운트다운, 컨텍스트, 제한, 다음 작업)와 7개의 커뮤니티 모드를 하나의 플러그인으로 설치하며…
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoom이 포함된 오리지널 Doom 엔진으로, Claude Code 안에서 플레이 가능. Mac Apple Silicon 알파 버전.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널 및 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - 대화에서 열린 항목의 목록을 계속 유지하고 프롬프트 위 밴드에 표시하는 Claude Code mod입니다.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - 터미널을 벗어나지 않고 풀 리퀘스트처럼 Claude이(가) 수정하는 모든 파일을 검토.
- [CTeitzel/cache-band](https://github.com/CTeitzel/cache-band) - Claude Code mod: a band above the prompt with the prompt-cache countdown, cache…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude 모드.
- [danielmertens/Claude-mods](https://github.com/danielmertens/Claude-mods) - Collection of personal Claude mods.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code 안에 사는 Tamagotchi: 부화하고, Claude이(가) 작성한 코드를 먹고, 버그를 남기며, 여덟 종류의 성체 중…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - Claude Code용 Goal 창: Claude이(가) 작업 중인 전체 목표, 그 이유 및 진행 상황을 보여 줍니다.
- [delexw/codyssey](https://github.com/delexw/codyssey) - Turn every Claude Code session into a little adventure: generative music that…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - 에이전트가 실행한 명령을 설명하는 Claude Code 모드.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 함수 훅으로 작성된 Claude Code 모드와 이를 제공하는 마켓플레이스. dash: 한 패널에 있는 세션의 대시보드.
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - 프롬프트 위에 Claude 뉴스와 종속성의 긴급 또는 보안 릴리스가 표시되는 밴드를 제공하는 Claude Code 모드입니다.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code 모드: guard가 도구 호출을 차단한 후 동일한 대상을 향하는 인식된 우회 경로를 중지하고 Claude에게 사용자에게…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code 모드: 실제 출력에서 읽은 진행률과 예상 완료 시간을 하나의 뷰에서 백그라운드 작업으로 표시합니다.
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code 모드: 팀원, 이름이 지정된 하위 에이전트 및 다른 세션의 메시지를 위한 통합 받은편지함으로, 읽지 않은 메시지 수와…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code 모드: 샌드박스 차단을 설명하고 반복되는 차단을 검토 및 실행 취소 가능한 설정 변경으로 전환합니다.
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Claude Code용 즐겨찾기: 명령과 스킬을 위한 원클릭 아이콘.
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia: 모든 화면에서 Build와 Kanban을 제공합니다.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 이봐요, 음소거했어요! diff를 버리고 장단을 끊으세요. 더 이상 편집도, 크레딧 차감도 없습니다.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code 모드: rewrite-prompt(Ctrl+P를 누르면 전송 전에 초안이 다시 작성됩니다).
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Pi, Codex 및 Claude Code를 위한 지침, skills, Pi 확장 기능 및 Claude Code 모드.
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Code 모드: delete-guard(파일 삭제 확인) 및 octopus-crew.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktop 앱과 터미널에서 프롬프트 위 밴드로 구독 사용량(5h / 7d)을 표시하는 Claude Code mod.
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code 모드: auto-model-detector가 각 프롬프트를 적절한 모델과 작업량으로 라우팅합니다.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - 프롬프트 위에서 병렬 브랜치와 worktree를 실시간으로 보여 주는 레이더: 어떤 항목이 깔끔하게 병합되는지, 어떤 항목이 충돌하는지, 어떤…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code 모드(function-hook 플러그인): 컨텍스트 밴드, 미완료 항목, 체크포인트 감시, 검토 게이트, 에이전트 사용…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - 하나의 Marketplace를 통해 설치되는 Claude Code 모드(function-hook 플러그인).
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [grota/beppe-claude-mods](https://github.com/grota/beppe-claude-mods) - Claude Code plugin marketplace with my mods.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Claude Code용 독일어 모드: 컨텍스트/캐시 알림, 안내가 포함된 미완료 항목, 상태 표시줄.
- [HectorBailey/claude-mods](https://github.com/HectorBailey/claude-mods) - Hector Bailey.
- [herlonventura/claude-model-squad](https://github.com/herlonventura/claude-model-squad) - Claude Code mod: a pixel-art squad suggests the right model.
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - 각 답변 후 다음 단계 3개를 모든 언어로 표시하는 Claude Code 모드이며, 선택적으로 로컬 음성 및 사이드 어시스턴트를 사용할 수…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 모드: 각 답변에 걸린 시간, Claude이(가) 생각한 시간, tok/s를 Claude desktop app의 답변…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code 모드: 화면을 공유하는 동안 streamer-mode가 비공개 창, 밴드 및 상태 줄을 숨깁니다.
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - 내 claude 모드용.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Claude Code function-hook 플러그인(모드).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Claude Code mod: 5시간 사용 제한이 끝날 때까지 기다린 뒤 대신 &quot;continue&quot;를 보냅니다.
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Claude Code 프롬프트 위에 표시되는 조종석입니다. 오리가 게이지를 읽습니다.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code 모드(function-hook 플러그인): PR 병합 후속 처리, /clear 인계, 백그라운드 작업 밴드, 검토 원장…
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 컨텍스트 및 계획 사용량 게이지, 프롬프트 캐시 미터, 확인할 항목 창을 제공하는 소형 Claude Code 모드입니다.
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - 프롬프트별 실시간 토큰 사용량, 모델 및 하위 에이전트를 표시하는 Claude Code 모드.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 사이드바의 context 사용량 패널: 총량, 분류, 라운드별 증가량, 가장 많은 공간을 차지하는 항목, 캐시, Claude이(가) 현재 하는…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 사이드바의 파일 목록: 이번 대화에서 어떤 파일을 새로 만들고, 수정하고, 삭제했는지와 각각 몇 줄을 변경했는지 표시합니다.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 입력창 위를 뛰어다니는 8비트 스타일의 毛毛(흑백 네덜란드 드워프 롭 토끼): 대기 중에는 납작 엎드리고, 작업 중에는 달리며, 도구를 사용할…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 사이드바의 ‘내가 물어본 것’: 이번 대화에서 주인이 입력한 모든 문장을 클릭 한 번으로 전체 보기, 복사 및 입력창으로 되돌리기.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 사이드바의 타임라인: 이번 라운드의 시간이 어디에 사용되었는지 표시합니다.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 사이드바의 토큰 왕래: 주 대화에서 매번 Anthropic에 몇 개의 토큰을 보내고, 얼마나 기다렸으며, 몇 개를 받았는지 표시하고 맨 위에…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code의 솔직한 속마음: 매 라운드의 답변이 끝나면 Claude이(가) 속마음을 한마디 조용히 말합니다.
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 새 슬래시 명령 및 사이드 패널과 같은 Claude Code용 작은 모드.
- [juro-mont/claude-ev-charging](https://github.com/juro-mont/claude-ev-charging) - An EV-charging progress bar and session panel for Claude Code helper agents.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd는 Claude Code 프롬프트 위의 밴드에 삽니다: 세션을 연기하고, 실행 중인 항목, context 및 usage limits를…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code의 응답과 알림을 VOICEVOX / Irodori-TTS 등으로 읽어주는 mod.
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Code 세션 간의 대화를 읽고 참여하는 Claude Mod (/crosstalk).
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Claude Code 모드. PixBar: 프롬프트 위에서 턴, 컨텍스트, 5시간 창 및 git에 따라 움직이는 픽셀 생물.
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude 모드.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Claude Code 모드(usage-meter 등).
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - 프롬프트 캐시 모닥불 옆에 모델별 픽셀 생물을 표시하고 프롬프트 위에 배치하는 Claude Code 모드.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 두 가지 Claude Code 모드: 채팅 옆의 파일 패널인 folio와 상태 줄이 포함된 터미널 세션 재스타일링인 tint.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: Claude Code가 알고 있는 내용을 실시간 그래프로 표시.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Claude Code의 답변을 기다리는 동안 주의가 흐트러지지 않게 합니다.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Sanmu의 Claude Code 모드 — 플러그인 marketplace(할 일 사이드 창).
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Angel(Vremia)의 프로젝트를 위한 Claude Code 모드.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 사용 사례, 원본 데모, 호환성 근거 및 안전 참고 사항을 담은 커뮤니티 큐레이션 Claude Code Mods 가이드: 영어 / 中文.
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Mod Box의 개별 Claude Code 모드로, 각각 따로 설치할 수 있습니다.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - 하나의 플러그인에 Claude Code 모드 14개가 포함되어 있으며, 각각 켜고 끌 수 있고 창에서 모드를 관리, 구성 및 가져올 수…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - iTerm2 탭 부제목에 Claude이(가) 무엇을 하고 있는지 표시하여, 탭 표시줄을 한눈에 보고 어느 세션에 사용자의 주의가 필요한지 알…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Claude Code mod: answer Claude point by point, right on the text.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 전환 가능한 권한 프로필을 제공하는 Claude Code 모드: 안전한 기본 프로필, 켜고 끌 수 있는 이름 지정 프로필, 그리고 그 외 모든…
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Claude Code용 소형 모드: 프롬프트 위에서 달리는 작은 아바타인 runner-avatar.
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - 관련 아티팩트와 참조를 추적하는 Claude Code 모드.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of what your AI coding agent is aiming for…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code를 위한 커뮤니티 모드: Claude Code 내부에서 실행되는 가드, 패널 및 명령. 마켓플레이스: modhub.
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Claude Code용 사이드 패널: Claude이(가) 작성한 파일, 터미널 분할, pull 기능이 포함된 git 저장소 상태, 사용량 바…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code를 위한 조용한 사이드 패널: 이 세션이 수행 중인 작업, 계획, 에이전트 및 다른 모든 세션.
- [mmedum/nuet](https://github.com/mmedum/nuet) - Claude Code 트랜스크립트에서 각 프롬프트와 각 답변 위에 희미한 시간이 표시되며, 사용 중인 시계 설정의 형식으로 작성됩니다.
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Code가 접어 숨기는 내용을 다시 표시합니다: Claude이(가) 읽은 파일, 실행한 명령, 각 턴에서 수행한 작업.
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod: warns when a session.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - 세션 시작 시 CLAUDE_CODE_ENABLE_TODO_TOOLS를 설정하여 todo 도구를 제외하는 모델에서도 다시 활성화하는 Claude…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - 안전하게 일시 중지할 수 있을 때까지 기다린 다음 세션을 넘기거나 압축하는 Claude Code 모드.
- [muellerei/task-line](https://github.com/muellerei/task-line) - 프롬프트 위 작업 목록에 현재 작업, 진행률 막대 및 개수를 작업당 한 줄로 표시하는 Claude Code 모드.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 내부에서 AI를 상대로 Connect Four 플레이 (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - 다른 코딩 에이전트가 저장소에 커밋하면 Claude이(가) 이를 감지하고 해당 보고서를 신뢰하는 대신 diff와 테스트로 감사하는 Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 여러 AI 에이전트가 공유하는 저장소를 위한 Claude Code 모드: 비밀 값이 .env 밖으로 나가거나 공개 원격 저장소로 푸시되는 것과…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande.
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod: flashes the terminal tab while Claude waits on you.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Claude Code 모드 마켓플레이스.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - 토큰을 전혀 사용하지 않는 Claude Code용 재미있고 무료인 모드. 첫 번째는 D&amp;D DM 화면인 Dungeon Master입니다.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code에서 SQL을 위한 가드레일: DB CLI를 통해 Claude이 DELETE, WHERE 없는 UPDATE, DROP…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows 및 CJK를 우선하는 하나의 모드: 모든 터미널에서 붙여넣은 이미지 및 텍스트 미리보기, CJK에 맞는…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Claude Code mods made by the OrbitMap team.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 무엇을 해 주는지에 따라 정렬한 최고의 Claude Code Mods. 직접 확인하여 각 항목을 한 줄로 정리했습니다.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code용 Claude Mods 두 가지: garde-du-corps.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 데스크톱 앱의 Code 탭을 위한 실시간 세션 통계 사이드 패널: 컨텍스트, 비용, git 변경 사항, 턴 통계, 하위 에이전트…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - Various mods and skills for my Claude Desktop setup.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code용 모드: safety-guard는 파괴적인 명령과 비밀 파일 접근을 차단하고, notify-router는 규칙 기반…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod: session timer and one-click handoff to a fresh context window.
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod: 실시간 주식 티커, /quote 패널, 가격 알림, 시장 밴드, 모델이 호출할 수 있는 quote 도구.
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Claude Code 모드: 사용된 context와 프롬프트 캐시가 만료될 때까지의 카운트다운을 프롬프트 위에 표시하는 band.
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Claude Code 모드: Claude이(가) 그리는 모든 다이어그램을 고정하고 작업의 실시간 지도를 유지하는 사이드 창.
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Claude Code 모드: Claude의 메모리 폴더를 병합, 다시 작성 및 정리하는 dreaming pass와 백업 및 실행 취소 기능.
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Claude Code 모드: Claude이(가) 보기 전에 모호한 프롬프트를 제거하고 프로젝트 고유의 용어를 제안.
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod: 프롬프트 위 한 줄에 SSH 호스트, RAM 및 5h/7d 사용량 제한 표시.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 모드: Claude이(가) 작업하는 동안 할 팔굽혀펴기. 토큰 없음.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline as a Claude Code mod: paces your usage limits in a line above the…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - claude code용 모드.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 모드: plan mode에서 승인한 계획을 프롬프트 위의 라이브 체크리스트로 바꾸고, Claude이 완료할 때마다 각…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 엄선한 Claude Code 모음입니다. 모든 항목을 복제하고 claude plugin validate로 확인했으며, 건드릴 수 있는 항목을…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 비용 없는 모드: 도우미 에이전트는 Haiku에서 실행되고, 큰 파일과 로그는 Claude의 컨텍스트를 채우는 대신 무료 Gemini 모델이…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 세션을 따라가는 로파이 사운드트랙: 차분함, 집중, 몰입과 테스트 통과 및 실패를 알리는 신호음. 오리지널 음악입니다.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude이(가) 코딩하는 동안 학습하세요: 코드를 변경한 턴이 끝나면 해당 변경 사항에 관한 질문 하나가 프롬프트 위에 나타납니다.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude이(가) 수행하는 모든 편집을 기록한 테이프: 각 변경 사항이 직접 입력되는 모습을 재생하고, 단계별로 살펴보며, 모든 파일을…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: Claude Code를 위한 비공식 Avengers 팬 모드.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - 프롬프트 위에 컨텍스트, 증가량, 할당량, 캐시, 네이티브 비용 및 에이전트 활동과 세션 세부 정보를 표시하는 Claude Code…
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods, installable as a plugin marketplace: deviation-kernel guards…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - 설치할 것이 전혀 필요 없는 Claude Code 패널의 오리지널 DOOM: 엔진은 모드 내부에서 실행되며, 셰어웨어 에피소드와…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [stelmach-systems/claude-mods](https://github.com/stelmach-systems/claude-mods) - Mody Claude Code (function hooks): panel agentów, pasek budżetu, flota sesji.
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Keep Claude.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 춤추는 pixel-art Malenia와 함께 Claude Code용 원클릭 commit messages.
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — Claude 플랜 사용량(세션 및 주간 한도, 재설정 카운트다운, 컨텍스트)을 프롬프트 바로 위에 표시하는…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Claude Code의 모양과 소리를 바꾸는 작은 모드.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 현재 세션을 창에 표시하는 Claude Code 모드입니다. 각 프롬프트, 해당 프롬프트에 대해 Claude이(가) 단계별로 수행한 작업…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - mods용 Claude Code plugin marketplace: Claude Code 내부에 bands, panes 및 기타 UI를 그리는…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - 읽고 있는 문장이 강조 표시된 상태로 Claude Code의 답변을 들어 보세요. 로컬 음성 및 여러 언어 지원.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code 모드: 프롬프트 위 한 줄에 5h/7d 할당량, 컨텍스트 창, 프롬프트 캐시 잔여 시간 및 세션 비용을 표시하고…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 모드: 장시간 실행되는 작업을 위한 애니메이션 진행 밴드와 완료 요약.
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 작은 Claude Code 모드 세 가지입니다. 하위 에이전트가 언제 완료되는지 확인하고, Claude이(가) 완료된 후 보낼 메시지를…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Claude이(가) 읽기 전에 큰 스크린샷을 축소하여 긴 세션을 더 오래 유지하고, 클릭이 여전히 올바른 위치에 도달하도록 Claude에게…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;I.
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - 프롬프트 입력창 위에 다음 프롬프트 추천을 표시합니다. /auto를 입력하면 10초 카운트다운 후 첫 번째 추천을 대신 전송합니다.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 작업 옆의 패널에서 Claude에게 별도 질문을 하세요. 기본 대화에는 표시되지 않습니다. 데스크톱 앱의 /btw처럼 작동합니다.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - 내 Claude Code 모드.
- [wellavelino/mystique](https://github.com/wellavelino/mystique) - A Claude Code mod: a highlighter pen for replies, a side panel for query…
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Claude Code용 모드: 사용량 제한 표시줄(5시간/주간) 및 작업/보류 항목 패널.
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
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — Xiaohongshu 캐러셀 및 WeChat 21:9+1:1 커버 쌍을 생성합니다.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code를 위한 아름다운 vim 스타일 powerline.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 터미널 창에서 코딩 에이전트의 diff를 검토하고 줄 단위 주석을 Claude Code, Codex, OpenCode 또는 Pi로 보냅니다.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - herdr용 브라우저 및 휴대폰 클라이언트: 모든 에이전트 창을 위한 채팅 및 라이브 터미널, SSH를 통한 원격 PC, 웹 푸시 알림.
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 컨텍스트 사용량, API 속도 제한 및 비용 추적을 포함한 Claude Code용 종합 상태 표시줄 플러그인.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code용 모드를 구축하세요. 모든 요청을 후킹하고, 모든 응답을 수정하며, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code를 위한 종합 상태 표시줄 대시보드 — 세션 정보, 할당량 막대, 에이전트 추적, MCP 상태, 메시지 기록 등을…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code 세션의 탄소 발자국을 추적합니다.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejun이 만든 Claude Code용 미적 상태 표시줄.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 공개 Claude Code 스킬 및 모드.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code용 Skills, 모드, 서브에이전트, 훅, 슬래시 명령 및 가이드 — 에이전트가 설치할 수 있습니다.
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 합법적인 무료 LLM APIs 및 코딩 에이전트 — 자체 업데이트되며 주 2회 프로브 검증.
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern Plugin - 캐릭터 카드 역할극, 월드북 관리, 프리셋 전환, 다크 테마, 메모리 요약, 관계…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Claude Code를 위한 빠르고 종속성 없는 비용 계산기 및 사용자 지정 가능한 상태 표시줄입니다.
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code 세션용 터미널 상태 표시줄.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 팔로우하는 대회(World Cup, Premier League, LALIGA, Champions League 및 11개 더)의 실시간 축구…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Claude Code를 Windows 및 macOS에서 사용하기 위한 로컬 제어 플레인: 고정 엔드포인트 뒤에서 한 번의 클릭으로 LLM…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 코딩 에이전트를 키보드 펌웨어 전문가로 바꾸는 Agent Skill입니다.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code 안에서 기도 시간, 히즈리 날짜, 아즈카르, 오늘의 아야, 순나 단식, 라마단, 주무아 및 타스비흐를 제공하며, 하나의…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 내부에서 버전 관리되는 개인 Claude Code 구성 — 에이전트, 스킬, 훅, 설정, statusline.
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Claude Code용 2줄 truecolor 상태줄(bash + 네이티브 Windows PowerShell): 모델, effort, 컨텍스트…
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - DeepSeek Harness를 위한 피크/비피크 시간 부동 조수 카드: i18n(en/zh/ru), 현지 시간 기준 시간대, 세션 비용을…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi 및 DeepSeek Harness용 플러그인 모음: 상태 표시줄 HUD, 작업 진행률 표시줄, Tailscale…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture를 위한 휴대용 Claude Code 툴킷: 엄격한 TDD 에이전트, 계층 규칙, hooks…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 이식 가능한 Claude Code 전역 구성: 사용자 지정 스킬, PreToolUse 후크 및 사용자 지정 상태 표시줄.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 매일 사용하는 Claude Code 플러그인: 어떤 컴퓨터에서든 작동하도록 정리한 skills와 mods입니다.
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop의 Code 탭을 위한 비공식 모드 — usage-pet: Clawd가 표시되는 사용량 밴드와 애니메이션 픽셀 펫.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) 브리지, 자체 개발(포크 아님): 스트리밍 답변 카드 / 하나의 인스턴스에서 여러 봇.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - 게임 Hytale 모드를 지원하는 Claude Code 플러그인 및 스킬 마켓플레이스.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code를 위한 토큰 거버넌스: 상위 모델이 지시하고, 실행은 충분히 적합한 가장 저렴한 수단으로 전달됩니다.
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code를 위한 실시간 워크플로 단계 상태 표시줄(Plan → Exec → Verify → Done)이며 모델이 자동으로…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media 모드용 저장소.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Claude Code를 위한 간단하고 유용한 상태 표시줄 설정.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Claude Code용 플러그인 마켓플레이스: 모드, skills, 에이전트, hooks, 출력 스타일 및 테마를 하나씩 설치할 수 있습니다.
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - 속도 제한, 현재 디렉터리 및 Git 브랜치 정보를 포함한 Claude Code 상태 표시줄을 표시하여 워크스페이스 인식을 향상합니다.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linux, WSL, Windows 및 macOS용으로 구성 가능한 Claude Code 상태줄, 프롬프트 타이밍, 서브에이전트 행, 터미널…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Claude Code를 위한 빠른 Rust 상태 줄 — payload 우선, 캐시된 git, 약 10ms 렌더링.
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Catppuccin 캡슐 스타일 사이드 패널에 컨텍스트 분석, 캐시 적중, 속도 제한 예측, 비용 및 활동을 표시하는 Claude Code용…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Claude Code용 상태 줄 및 토큰 줄: 컨텍스트, 속도 표시가 포함된 5시간 및 주간 사용량, 활동, git 및 비용을 표시합니다.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - macOS, Linux, Windows 전반에서 모델, 컨텍스트, 제한, git 정보, 세션 시간을 포함한 Claude Code의 주요 상태…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - 다중 행 Claude Code 상태 줄: 비용, 컨텍스트 %, git 및 활성 계정 — 가격과 컨텍스트 창이 자동으로 업데이트됩니다.
- [QingqiShi/claude](https://github.com/QingqiShi/claude) - Personal ~/.claude for Claude Code: settings, global CLAUDE.md, hooks, status…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - claude code를 위한 유용한 정보가 있는 Statusline.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - 네이티브 에이전트 팀. 통제된 방식으로. Claude Code를 위한 엄격한 작업자 한도, 실시간 팀 가시성 및 이식 가능한 구성.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code 추가 기능: 탭 상태 색상 점 감시기 + 내장 GSD 상태 표시줄.
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr에서 Claude Code용으로 정의 가능한 software factory: xstate station 그래프, manager 모드…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - herdr 설치 프로그램 플러그인으로 패키징된 macOS 및 Linux용 Claude Code 사용량 상태 줄입니다.
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code용 사용자 지정 상태 표시줄 — 사용률, 컨텍스트 크기, 비용 및 타이머가 표시되는 컨텍스트 막대.
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Claude Code를 위한 깔끔하고 유용한 상태 표시줄 — 프로젝트, git 상태, 모델, 세션 시간, 컨텍스트 사용량 및 속도 제한을…
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - baloo가 포함된 Claude Code 플러그인 마켓플레이스: 스킬, 프로젝트의 결정 사항·지침·검사를 기준으로 변경 사항을 검증하는…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 전문가급 Claude Code statusline: 세션 시간, ECB FX를 적용한 다중 통화 비용, MTok당 요금 및 지출 한도를…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code용 구독 인식 상태 표시줄.
- [d3r3nic/claude-live-sessions](https://github.com/d3r3nic/claude-live-sessions) - A Claude Code plugin: a pane of the live Claude Code and Codex sessions on your…
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code용 풍부한 터미널 상태 줄 — Bun + TypeScript, 런타임 의존성 없음.
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude Code용 도구, 스킬 및 에이전트 — 모델, 브랜치, PR, 컨텍스트 크기, 프롬프트 캐시 잔여 시간 및 비용을 표시하는 상태…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Claude Code 사용자 지정 상태줄 (모델, effort, 컨텍스트, 캐시, 사용량 한도).
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code의 실제 DeepSeek API 지출: DeepSeek 피크/오프피크 요금으로 세션 트랜스크립트의 가격을 다시 계산하고…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Claude Code 내부에서 이미지를 미리 봅니다: 답변 아래 칩 위에 마우스를 올려 그림을 띄우거나, /img &lt;path&gt;로 창에서…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Claude의 할 일을 Fizzy.do에 동기화하여 팀이 실시간으로 확인할 수 있게 하고, 작업을 영구 카드로 전환해 협업을 강화하고 진행…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - 컨텍스트, 비용, 기간, git 브랜치, 속도 제한 및 실시간 사용량을 표시하는 간결한 대시보드로 Claude Code 상태 추적.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 환경 설치 프로그램: skills, statusline, hooks, permissions 및 선택적…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Claude Code용 HUD 스타일 상태 줄 — 네트워크 상태, TPS, 컨텍스트, 할당량, 비용을 한 줄에 모두 표시.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [primelogiclabio/claude-tools](https://github.com/primelogiclabio/claude-tools) - Skills and mods for Claude Code and Cowork — project-tracker, reference-doc…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - 휴대용 Claude Code 구성(statusline + 설치 프로그램).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code용 소형 대시보드: 컨텍스트 %, 캐시 카운트다운, 5시간 및 주간 사용량, 새 채팅으로의 원클릭 Handoff, 그리고…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Claude Code용 사용자 지정 터미널 상태 표시줄: 모델, 디렉터리, git 상태, 컨텍스트 사용량 및 속도 제한.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 포터블 Claude Code 설정: CLAUDE.md, settings, statusline, skills.
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code용 실시간 비용 추적 및 세션 모니터링 상태 줄.
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code 스킬(VS Code, Windows): 채팅의 파일 경로 아래 이미지 미리보기 및 열기 버튼, 클릭 가능한 로컬 링크…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - 폴더, git 브랜치, 모델, 컨텍스트 창 사용량 및 플랜 사용량 제한을 표시하는 Claude Code 상태 줄.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code 에이전트를 위한 사전 대응형 AI 메모리 및 속도 제한 모니터.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code 훅, 서브에이전트 및 상태줄: 유형별 오픈 소스 컬렉션과 도구, 각각 보안 등급 제공. English / 中文.
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code 상태 표시줄을 위한 시각적 빌더입니다. 브라우저에서 터미널 하단의 막대를 디자인한 다음 명령 하나를 붙여 넣어 설치하세요.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 실시간 토큰 사용량과 예상 에너지 소비량을 표시하는 Claude Code 상태 표시줄.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Claude Code용 모드: 함수 훅을 기반으로 구축된 창, 밴드 및 동반자.
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code 스타일 UI 번들로, Pi 코딩 에이전트를 위한 도구 렌더링, 스피너, 상태 표시줄, 테마 및 설정 마법사를 제공합니다.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code 세션 간에 작업을 전달하세요. 저장소를 담당하는 세션에 변경 사항을 넘기세요.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablabs용 모듈식 크로스 플랫폼 도구 MODS를 제어하기 위한 MCP 서버입니다. CAD/CAM 및 기계 제어 도구가 포함되어 있습니다.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 로컬 LLM을(를) 사용하여 CK3 모드를 번역하는 Codex 및 Claude Code 스킬.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code용 오픈 소스 모드 및 기타 확장 기능.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Claude Code 상태 표시줄: CCometixLine의 미관 + Claude HUD 기능.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code에 반복해서 요청하는 작업을 찾아 모드로 변환하세요. 예제 모드 8개와 가상 사무실도 포함됩니다.
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Claude Code용 prompt-bar 모드: 사용량 제한, 캐시 타이머 및 알림, 모델/작업량 선택기, 사이드 패널.

</details>

<a id="dsh-cordis"></a>

## DSH 및 Cordis 플러그인 생태계

DeepSeek Harness와 Cordis는 서로 다른 방향에서 같은 지점에 도달합니다. 이들에게 플러그인은 모드 메커니즘이므로, 그쪽의 플러그인은 이곳의 모드에 해당합니다.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74358 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **74358**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐100891 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **100891** |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100557 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **100557** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82028 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **82028**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35768 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **35768**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25499 · Python · 🔎 inferred · 19 天</summary>

##### 📝 요약

Distilly — 어떤 Agent 또는 Bot에서든 재사용 가능한 Skills로 그들의 사고방식을 추출하세요. 이전 이름은 Colleague Skill（原同事 Skill）입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **25499**  |
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
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4493 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **4493**   |
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
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

세계 최초의 AI 에이전트용 가상 터미널

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3682**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3093 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **3093**   |
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
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

컨텍스트 인사이트 및 관리를 위한 최고의 DeepSeek Harness 플러그인으로, 컨텍스트 대시보드 / 브라우저 / 사이드바와 컨텍스트 명령을 제공하여 컨텍스트 통계, 구성, 분석, 발전 세부 정보와 컨텍스트가 어떻게 구성되고 발전하는지 확인할 수 있습니다. 하나의 도구로 제공되는 DeepSeek Harness 컨텍스트 시각화 플러그인으로, Context 패널과 브라우저 및 사이드바, Context 명령을 통해 컨텍스트 구성, 발전, 압축, 가지치기 등의 이벤트와 작업을 파악합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1995**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1841 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **1841**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kenryu42/cc-safety-net">kenryu42/cc-safety-net</a></b> · ⭐1591 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

AI 코딩 에이전트를 위한 실행 전 보호 장치입니다. 도구 호출이 실행되기 전에 파괴적인 Git 및 파일 시스템 명령과 민감한 파일에 접근하려는 일반적인 시도를 차단합니다. Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build, Hermes Agent, Kimi Code, OpenClaw, OpenCode 및 Pi를 지원합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1591**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `antigravity` · `claude` · `claude-code` · `claude-code-plugin` · `cli` · `codex`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1578 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

크로스 디바이스 오픈 소스 Agent 워크벤치

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **1578**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **1410**   |
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
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1173 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **1173**   |
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
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **705**    |
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
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness Desktop App: DSH Sessions, 프로젝트, 파일, 웹 리서치, 플러그인 및 Office 아티팩트를 위한 로컬 AI 데스크톱 작업 공간입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **592**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
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
| 최초 등록   | 2026-10-12 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness용 무료 웹 검색 제공자 - DuckDuckGo 백엔드, API 키 불필요

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **369**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
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
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 스킨 / 배경화면 / 테마 패키지 플러그인 (dsh-plugin) — 8개의 Mirage 테마, 사용자별 강조 색상, 배경화면 2.0, 테마 패키지 가져오기·내보내기/공유 링크, 즐겨찾기 및 무작위 선택을 지원하며 순수 네이티브 토큰 시스템으로 구현되었습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **225**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐204 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **204**    |
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
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 애니메이션 검색 플러그인: 대화 내에서 여러 소스를 검색하고, Bangumi 평점 및 상세 정보를 카드로 표시하며, 마그넷 링크 복사를 지원합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **176**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness (DSH) 백업 및 복원 플러그인 — 전체 DSH 구성, 플러그인, MCP 서버, 스킬 및 작업 공간을 내보내고 가져오고 마이그레이션하고 동기화합니다. 한 번의 클릭으로 다른 머신으로 마이그레이션할 수 있습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **176**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **172**    |
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
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness (DSH)에서 ChatGPT Plus / Pro(Codex) 구독을 사용하세요: ChatGPT 로그인으로 GPT-6 및 Codex 모델, 이미지, 웹 검색 및 할당량을 이용할 수 있습니다 — OpenAI API 키가 필요하지 않습니다. 베타: ChatGPT 모바일 앱에서 DSH를 제어합니다. DSH에서 ChatGPT 구독을 사용하고 ChatGPT 모바일 App으로 원격 제어할 수 있습니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **160**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐143 · Python · 🔎 inferred · 0 天</summary>

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
| 스타        | **143**    |
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
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐135 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

설치만 하면 mattpocock/skills v1.3.1의 27개 엔지니어링 및 생산성 스킬이 함께 제공되므로 수동으로 스킬을 설치할 필요가 없습니다. 400억 토큰으로 제작된 이 플러그인은 원본 스킬을 기반으로 개발 효율을 10배 높이고 초보자가 이 스킬 모음을 더 빠르게 익히도록 돕습니다. GitHub issue를 전력 지원하며, Markdown은 미리보기 버전이고 GitLab은 현재 지원하지 않습니다. 사용과 지원에 감사드립니다💗

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **135**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/flymysql/dsh-remote">flymysql/dsh-remote</a></b> · ⭐133 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, operate with rw_* tools, and SFTP-mirror it into a real local DSH workspace.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **133**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `remote` · `sftp` · `ssh` · `tunnel` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/flymysql--dsh-remote/714d273f27c6d75b.png" width="100%" alt="flymysql/dsh-remote screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **133**    |
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
<summary>🧵 <b><a href="https://github.com/Noob-stupid/dsh-plugin-gating-hub">Noob-stupid/dsh-plugin-gating-hub</a></b> · ⭐100 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH plugin - framework upgrade safety & plugin gating: contract pre-check, rollback point, auto-rollback on failure, evidence-based auto-disable; plus a multi-source plugin market. Unofficial. | DSH 插件：框架升级安全 + 插件门控——升级前契约预检、回滚点、失败自动回滚、有确证证据才自动禁用；另带多源插件市场。非官方社区项目。

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **100**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `ai-empower` · `cli` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins` · `framework-upgrade` · `marketplace`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/noob-stupid--dsh-plugin-gating-hub/0b18270cf916dc1c.png" width="100%" alt="Noob-stupid/dsh-plugin-gating-hub screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐90 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

StudyHub: 자신의 자료를 문제와 간격 반복 학습으로 바꾸는 DeepSeek Harness (DSH) 플러그인 · 자신의 자료를 문제와 간격 반복 학습으로 바꾸는 DSH 학습 플러그인

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **90**     |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-12 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 72</sub></summary>

- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30초 만에 자신에게 맞는 DeepSeek Harness 플러그인을 찾아보세요.
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - DSH 플러그인 — DeepSeek Harness(DSH)에서 사용할 수 있는 무료 OpenCode Zen 모델입니다.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 플러그인 마켓 / DSH Plugin Marketplace: DeepSeek Harness Web GUI에서 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 스스로 반복 개선하는 소프트웨어를 위한 플러그인 런타임 — 에이전트가 Rust, TypeScript, Python 및 Go에서 프로세스와…
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 4 小时自动维护 | Oh-My-DSH…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - Best Roblox Luau Bug Checker and API Verifier 2026 DevForum MCP Tool.
- [ZASENJC/dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) - 自动分类、收录和验证 DeepSeek-Harness 社区插件的市场。 Automatically categorize, curate, and…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Deepseek-Harness 핵심 기반으로 제작된 데스크톱 버전 Agent입니다.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 살아 있는 DeepSeek Harness 플러그인 디렉터리 — 매시간 갱신, 매일 호환성 테스트, 앱 내 플러그인 스토어와 스캐폴더 포함.
- [1475505/miliastra-beyond-simulator](https://github.com/1475505/miliastra-beyond-simulator) - 千星沙箱模拟器：Lua 驱动的 2D 奇域外置沙箱 ，支持 DeepSeek Harness、Web 和 MCP.
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - AI Coding Agent를 위한 작업 인식형 워크스페이스 컨텍스트 검색 및 수명 주기 추적: 현재 작업과 가장 관련성 높은 문서, 코드 및…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent는 AI 코딩 에이전트를 위한 오픈 소스 FDE Harness입니다 — 진입 시 비즈니스 판단을 파일.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 플러그인 엄선 디렉터리 — MCP / Skill / TUI / 멀티 Agent / 컨텍스트 메모리 /…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - 시각적 Agent 오케스트레이션 플랫폼｜DeepSeek Harness 기반으로 Workflow, Multi-Agent, 메타 오케스트레이션…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh 게임 소재 마스터 플러그인입니다. seedream 이미지 생성 모델과 minimax 동영상 생성 모델을 연동하여 다양한 게임 소재를…
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 플러그인: 모델 컨텍스트 창을 한 번에 매칭하고 용량 출처를 표시하며, 선택을 통한 일괄 구성, 기존 창 관리…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness（DSH）기반 멀티 플랫폼 그룹 채팅 지능형 에이전트 시스템｜DSH 기반 멀티 플랫폼 그룹 채팅…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - DSH(DeepSeek Harness) 웹 GUI 플러그인 모음 — 작업 알림, 공급자 사용량, LAN 프록시, MCP 관리자…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 커뮤니티가 엄선한 DeepSeek Harness(dsh) 플러그인, 도구, 스킬 및 학습 자료입니다.
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeek Harness를 기반으로 구축된 오픈 소스 GrokBot 대안.
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - DeepSeek Harness용 MCP 서버 관리자 플러그인: 설정 → MCP 페이지, OAuth(PKCE + 동적 클라이언트 등록) 또는…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - A2A 상거래 협상 런타임 + DeepSeek Harness(dsh) 플러그인입니다.
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - DeepSeek Harness Web용 도구 상자 패널: MCP 관리자(도구 및 JSON Schema, 마켓, 가져오기, 워크스페이스 복사)와…
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - DeepSeek Harness 플러그인 · 전송栏에서 한 번의 클릭으로 프롬프트 초안 「최적화」: 5차원 진단 + SSE 스트리밍으로 표시되는…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - 검증된 DeepSeek Harness 플러그인 마켓플레이스 및 자율 레지스트리.
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML이 아닌 진짜 PowerPoint입니다. AI에게 다룰 내용을 말하면 pptwise가 자신의 컴퓨터에서 편집 가능한 덱을 만듭니다.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - 코딩 에이전트를 위한 로컬 우선 코드 지식 그래프 및 컨텍스트 harness입니다.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - 스팸이 필터링된 DeepSeek Harness (dsh) 플러그인, 번들 및 스킬의 오픈 데이터 레지스트리입니다.
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - 임베디드 C/C++ AI 엔지니어링 플러그인 — 펌웨어 스킬(FreeRTOS, Keil, HardFault, 상태 머신) + 1% Rule /…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 로컬 WorkBuddy 데스크톱 앱에 로그인된 모델(DeepSeek / GLM / Kimi / MiniMax 등)을 로컬 OpenAI 및…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - dsh plugin teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 플러그인을 위한 상시 호환성 테스트: 정확한 릴리스, 격리된 러너, 수정 가능한 업스트림 이슈.
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - 로컬 우선 에이전트를 위한 공격적인 컨텍스트 압축입니다. 자체 호스팅 llama.cpp에서 Qwen3.8‑27B를 낮은 컨텍스트로 실행하고…
- [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) - OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - DeepSeek Harness (dsh)를 위한 보호형 컨텍스트 압축: LLM가 제안하고 결정론적 보호 장치가 폐기합니다 — 원자별 즉시…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web 및 Desktop 버전으로, Plugins, Skills 및 Interfaces를…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - 프로젝트 문서와 장기 메모리를 전용 Obsidian vault에 일반 Markdown으로 보관하는 DeepSeek Harness 호스트…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - 엄선된 근거 기반 DeepSeek Harness (DSH) 플러그인 디렉터리: 검증된 로드 가능한 확장 기능과 스킬, 권한을 고려한 설치…
- [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) - DSH 纯净桌面壳：双击像普通软件一样一键启动，后端活性实时监测 + 托盘快捷启停，零视觉改造.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 플러그인을 위한 X-ray: 선언된 기능과 실제 동작을 비교합니다. 레지스트리 + 정적 스캐너 + 배지.
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 플러그인 마켓 — DeepSeek Harness 설정에서 커뮤니티 플러그인을 한 번에 설치하고 공개 디렉터리 사이트.
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - DeepSeek Harness용 Mixture of Agents (MoA) 플러그인으로, /moa 슬래시 명령, 파일 작업 공간 및 Live…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH 플러그인: 네이티브 dsh-better-sidebar 탭으로 제공되는 IDE급 Git 도구 창 — 브랜치 트리, 커밋 그래프, 변경…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) 플러그인 리더보드 및 디렉터리｜DeepSeek Harness (DSH) 플러그인 순위 / 플러그인…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 다중 폴더 workspace: DSH(DeepSeek Harness)의 Agent가 기본 디렉터리뿐 아니라 추가한 다른 폴더도 동시에 읽고 쓸…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - 엄선된 목록과 매니페스트로 검증된 GitHub 검색 기능을 제공하는 검색 가능한 DeepSeek Harness 플러그인 레지스트리입니다.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness(dsh) 플러그인을 위한 종속성 없는 검증 표준 — 정적 구조 게이트(R), cordis 계약 검사(K)…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - DeepSeek Harness (DSH) 플러그인: 설정 패널에서 한 번의 클릭으로 OpenCode Go 모델 동기화 - 모든 서버 모델…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness 플러그인 마켓 - dsh-plugin 토픽 플러그인 찾아보기, 검색 및 설치.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness의 OpenCode — OpenCode Zen + Go 무료 티어 모델을 계속 작동하게 하는 DSH 플러그인…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness를 위한 서드파티 플러그인 마켓플레이스 및 보호된 수명 주기 관리자.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx는 사람을 중심으로 설계된 확장 가능한 데스크톱 작업 공간입니다.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - DeepSeek Harness를 위한 모든 기능이 포함된 코딩 에이전트 — Claude Code 스타일 워크플로, 원하는 모델, TUI…
- [GooDAnDReaDY/dsh-live-canvas](https://github.com/GooDAnDReaDY/dsh-live-canvas) - Interactive Visual Frontend Studio, Retool-Style CRUD Engine, Time-Travel…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - DeepSeek Harness Agent가 GitHub을(를) 조작할 수 있는 네이티브 손발을 갖게 하세요! gh CLI의 보안 자격 증명을…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — DeepSeek Harness (dsh)를 위한 커뮤니티 버전 로컬 배포·운영 도구 모음: 설치 / 시작 / 모니터링…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - 보관된 DeepSeek Harness 세션을 디스크에 저장된 기록 및 로그 디렉터리와 함께 영구적으로 삭제합니다.
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness(DSH) 웹 플러그인: 시장 대시보드 사이드바 탭을 모니터링합니다 — 마우스를 올리면 장중 차트가 표시되는…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - 원격 서버에서 기존 DSH 플러그인을 사용해 작업을 실행하고, 원하는 수의 머신에 걸쳐 운영합니다.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 출처가 표시되지 않은 빈 모델 시도를 재시도 가능하게 만듭니다. 이를 판별할 수 있는 하나의 접점.
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - 스스로 정리하는 플러그인: iOS 및 macOS용 cordis 플러그인 프레임워크의 Swift 6 포트.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness 에이전트 프리셋: Codex 및 Claude Code를 위임 하위 에이전트로 사용하며, 각각 읽기 전용 및 전체…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus-verified 라이프사이클 커널과 Cordis 호환성 어댑터를 갖춘 Rust 플러그인 런타임입니다.
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - 인라인 Antigravity 대시보드: tok/s, DSH 스타일 캐시 적중률, 5시간 및 주간 할당량.
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness용 Paseo Provider Plugin (Direct Provider).
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [HaydenSmith1121/dsh-plugins](https://github.com/HaydenSmith1121/dsh-plugins) - DeepSeek Harness (dsh) 插件市场 —— 目录（一个插件一个配置文件）+ 可视化面板 + 一键安装；插件本体在…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - GitHub을(를) 기반으로 한 dsh 플러그인 마켓플레이스 - topic:dsh-plugin을 자동으로 검색하고 매시간 동기화.

</details>

<a id="writing"></a>

## 작성, 토론 및 동영상

모드 기능에 관한 글, 토론 및 동영상입니다.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
| TypeScript | 377  | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 90   | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 38   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 17   | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Rust       | 6    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| Go         | 5    | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| PowerShell | 2    | `GoSlowPoke168/claude-statusline`, `YangShen-SWE/dsh-plugin-simple-pet`                                       |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1    | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1    | `eovidiu/cordis-ios`                                                                                          |

<sub>언어를 명시한 항목만 집계됩니다. 문서 및 토론 항목은 이 표에서 제외됩니다.</sub>

## 기여

수정 사항을 제보해 주시면 이 목록을 가장 빠르게 개선할 수 있습니다. 항목이 잘못 분류되었거나, 등급이 잘못 매겨졌거나, 이름 충돌로 인해 프로젝트가 잘못 제외되었다면 이슈 또는 풀 리퀘스트를 열어 주세요. 마지막 유형은 자동 필터가 가장 자주 잘못 판단하는 경우입니다.

---

<sub>독립적인 커뮤니티 프로젝트입니다. Anthropic와(과) 제휴, 승인 또는 검토를 거치지 않았습니다. Claude Code, Claude 및 Anthropic은(는) Anthropic의 상표입니다. 제품 동작은 예고 없이 변경될 수 있으므로, 중요한 내용은 공식 문서에서 확인하세요. 에셋은 원 프로젝트의 자산으로 남으며, 라이선스가 허용하는 경우에만 재현됩니다.</sub>

<sub>마지막 업데이트 · 2026-10-12T06:04:10+08:00</sub>
