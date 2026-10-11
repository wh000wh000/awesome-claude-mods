<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="멋진 Claude 모드">
</p>

<h1 align="center">멋진 Claude 모드</h1>

<p align="center"><b>Claude Code 모드와 플러그인, 그리고 이들이 변경하는 더 심층적인 동작을 근거에 따라 등급화한 색인입니다.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-624-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **실시간 색인** · 마지막 동기화: `2026-10-11T10:13:26+08:00` (UTC+8)
> · 항목: **624** · 최신 업데이트에 추가됨: **0** · 구현 언어: **12**

<sub>아래의 모든 항목은 자동으로 수집, 필터링 및 재검증되었습니다. 유료 게재 항목은 없습니다.</sub>

<a id="featured"></a>

## 지금 주목할 항목

<sub>카테고리별 항목 하나를 근거 등급과 별점에 따라 순위를 매겨 선택하며, 업데이트할 때마다 다시 계산합니다. 추천이 아닌 순위이며, 모든 항목은 아래의 전체 카드로 연결됩니다. 스크린샷이나 녹화본을 게시한 프로젝트를 우선하므로 목록이 시각적으로 유지됩니다.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9467 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2533 · Python · 👁️ observed</sub>
<sub>유령 토큰을 찾으세요. 수정하세요. 압축을 견디세요. 컨텍스트 품질 저하를 피하세요.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74290 · TypeScript · 👁️ observed</sub>
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
- [공식: Anthropic 자체 저장소 및 릴리스 노트](#공식-anthropic-자체-저장소-및-릴리스-노트) — **18**
- [모드: 모드 기능으로 구축됨](#모드-모드-기능으로-구축됨) — **484**
- [DSH 및 Cordis 플러그인 생태계](#dsh-및-cordis-플러그인-생태계) — **111**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150075 · TypeScript · ✅ official · 0 天</summary>

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
| 스타        | **150075** |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9467 · TypeScript · ✅ official · 1 天</summary>

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
| 스타        | **9467**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8245 · Python · ✅ official · 1 天</summary>

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
| 스타        | **8245**   |
| 마지막 푸시 | 2026-10-09 |
| 최초 등록   | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6336 · Python · ✅ official · 241 天</summary>

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
| 스타        | **6336**   |
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
<summary>🏛️ <b><a href="https://github.com/PerryLink/dsh-mcp-panel">PerryLink/dsh-mcp-panel</a></b> · ⭐74 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

공식 DeepSeek Harness MCP 클라이언트를 위한 MCP 관리 콘솔입니다. 상태 진단 및 파이프라인 시험 호출을 지원하는 /mcp 명령, 서버 CRUD를 관리하는 Settings MCP 탭(승인 게이트가 적용된 쓰기 및 자동 백업), 공식 도구 파이프라인(Apache-2.0, dsh-plugin)을 통한 도구 시험 콘솔을 제공합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `공식: Anthropic 자체 저장소 및 릴리스 노트`                                    |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **74**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/f435adadbab44c9f.png" width="100%" alt="PerryLink/dsh-mcp-panel screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-mcp-panel/79405ad96d2dc69e.gif" width="100%" alt="PerryLink/dsh-mcp-panel animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/Enc-hanted/dsh-pulse">Enc-hanted/dsh-pulse</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Cross-session usage & cost observatory for the DeepSeek Harness web profile — trend/heatmap dashboards, per-model peak-hour pricing (CNY/USD), official DeepSeek balance with spend reconciliation.

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
<summary>🏛️ <b><a href="https://github.com/MIHassan3/DSH-Launcher">MIHassan3/DSH-Launcher</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

이것은 공식 DeepSeek Harness용 런처입니다. 수정은 없으며 DeepSeek가 개발한 것을 실행하기만 합니다.

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
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `ai-agent` · `ai-agents` · `ai-tools` · `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mihassan3--dsh-launcher/2d777b77102fa60f.png" width="100%" alt="MIHassan3/DSH-Launcher screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 3</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - 모드에 `$.ui.notify`를 추가했습니다. 자체 알림 설정을 통해 네이티브 알림을 표시하고 어떤 채널에서 전송했는지 알려줍니다.
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - `UserPromptSubmit` 훅 또는 모드의 `prompt.submit` 훅 실행 중 Esc 또는 인터럽트로 인해 헤드리스 세션이…
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - A curated directory of source-verified DeepSeek Harness (DSH) plugins, tools…

</details>

<a id="mods"></a>

## 모드: 모드 기능으로 구축됨

여기의 모든 항목은 2.1.287에서 Claude Code가 얻은 기능을 사용한다는 증거를 보여 줍니다. `ui.render`을 통해 그리거나, 창·밴드·카드를 소유하거나, `$.ui.selection()`을 읽거나, `agent.spawn`로 팀원을 생성하거나, 명시적으로 모드라고 밝힙니다.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2533 · Python · 👁️ observed · 0 天</summary>

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
| 스타        | **2533**   |
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
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐470 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 요약

GitHub에서 스캔한 공개 Claude Code mods(function hooks)의 커뮤니티 카탈로그로, 각 mod가 네트워크를 통해 읽기, 쓰기, 실행 또는 전송할 수 있는 항목을 표시합니다. https://mods.aidojo.si/ 찾아보기

<sub>🔧 코드에서 사용된 항목: `data/seeds.txt`, `data/duplicates.txt`, `data/repos.txt`</sub>

##### 📌 기본 정보

| 필드     | 값                                                             |
| -------- | -------------------------------------------------------------- |
| 카테고리 | `모드: 모드 기능으로 구축됨`                                   |
| 근거     | `자체 텍스트에서 모드 API을(를) 언급하거나 모드 기능을 선언함` |
| 언어     | JavaScript                                                     |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **470**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐182 · TypeScript · 👁️ observed · 1 天</summary>

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
| 스타        | **182**    |
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
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐117 · TypeScript · 👁️ observed · 6 天</summary>

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
| 스타        | **117**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐109 · HTML · 👁️ observed · 0 天</summary>

##### 📝 요약

모든 프롬프트의 추론 강도를 선택하고, 프롬프트 캐시와 컨텍스트를 표시하며, 한 번의 클릭으로 넘기거나 압축하는 Claude Code 모드

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
| 스타        | **109**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>애니메이션 녹화</sub></td>
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐88 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **88**     |
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
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐62 · TypeScript · 👁️ observed · 8 天</summary>

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
| 스타        | **62**     |
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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐57 · Shell · 👁️ observed · 3 天</summary>

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
| 스타        | **57**     |
| 마지막 푸시 | 2026-10-07 |
| 최초 등록   | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/markneonin/paneline">markneonin/paneline</a></b> · ⭐6 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 요약

Activity, Files, Agents, Context 및 MCP 탭이 있는 사이드 패널, 프롬프트 위의 상태 줄, 새롭게 스타일링된 채팅, 터미널의 Mermaid 다이어그램, 표, 코드 및 diff 패널을 추가하는 Claude Code mod(플러그인). 색상은 /color와 /theme(dark, light 및 기타)를 모두 따릅니다.

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
| 마지막 푸시 | 2026-10-06 |
| 최초 등록   | 2026-10-10 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/markneonin--paneline/e7976a2ea941fd17.png" width="100%" alt="markneonin/paneline screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 450</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Claude Code에서 사용할 수 있는 100개 이상의 모드 모음입니다.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Claude Mods 및 이를 빌드하기 위한 도구: 먼저 builder skill을 제공한 다음 mods를 제공합니다.
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - 제가 매일 실행하는 Claude Code harness로, 첫날부터 이 이름으로 공개되었으며 현재 ucsandman/Agnostic-AI와…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Claude Mods로 Claude Code에 지붕을 씌우세요. 바이너리를 수정하지 않고 시스템 프롬프트와 영어 알림을 원하는 문구로…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - 네 가지 Claude Code 모드: Cache Keeper, Recording Mode, Goal Meter 및 Collision Guard.
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Learning Hacker의 Claude Code Mods: 에이전트의 작동을 이해하기 쉬운 방식으로 시각화합니다.
- [kakha13/claude](https://github.com/kakha13/claude) - Claude가 읽기 전에 프롬프트를 수정하고 번역하는 Claude Code 모드.
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Claude Code용 사이드 패널: 세션에서 실행하는 서브에이전트, 각 에이전트가 하는 일, 토큰 및 대화를 클릭 한 번으로 확인할 수…
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - Claude Code를 위한 cockpit: 프롬프트 바로 위에서 실시간 계획 바, subagent 스트립, 재설정 카운트다운이 포함된 사용량…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Claude Code Mods에 관한 출처 인용 Obsidian 지식 베이스: 작동 방식, 구축 방법 및 설치 전에 확인하는 방법.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Claude Code 에이전트에게 Claude Mods(함수 훅 플러그인)를 구축하는 방법을 가르치는 스킬과 시작 예제.
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Claude Desktop(Code 탭) 사이드바 패널: 모든 Claude Code session의 미완료 및 진행 중인 할 일을 나열하고…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Nekyia Labs의 Claude Code mods 및 스킬, 지속적인 홈에 사는 AI들이 매일 구축하고 사용.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Claude Code용 Claude Mods(function-hooks 플러그인).
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Claude Desktop(Code 탭) 입력 상자 위의 사용량 막대: 5h / 7d 할당량, token 사용량, 비용.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - 하나의 마켓플레이스에서 설치할 수 있는 커뮤니티 Claude 모드, 플러그인 및 스킬.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - Baselane mods 갤러리: 검토 및 고정된 Claude Code mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - 대화형 에이전트와 협업하는 사람을 위한 의사 결정 큐 CLI/TUI. 에이전트가 질문을 올리면 사람은 하나의 받은 편지함에서 답합니다.
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Claude Code IDE 패널 모드: 에이전트 보드, 파일 트리 및 HWP/PDF 뷰어, 시스템 상태…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Claude Code용 플로팅 상태 카드 — 모델, 컨텍스트, 속도 제한, 비용, 브랜치 — 그리고 모든 스크립트나 mod가 값을 전달할 수…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Claude Code 모드: 화면 공유 중 screen-guard가 이름과 비밀 정보를 가리고, cache-panel이 프롬프트 캐시가…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Claude Code Extensions. Claude의 모든 기능을 잠금 해제하세요.
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
- [HMarzban/claude-mod](https://github.com/HMarzban/claude-mod) - 다음 Claude Code 메시지에 드는 비용을 확인하세요. 프롬프트 위의 라이브 밴드에서 프롬프트 캐시 카운트다운, 재워밍 비용, 세션…
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
- [noash-xrc/claude-tools](https://github.com/noash-xrc/claude-tools) - Claude Code mod that lets Claude log unfinished work to Docs/todos.md, with a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Claude Code용 모드: Claude이 수행하는 작업을 연기하는 작은 픽셀 마스코트 Clawd.
- [reporails/arcade](https://github.com/reporails/arcade) - Claude Code mods로 제공되는 클래식 데스크톱 게임으로, Claude가 작업하는 동안 pane에서 플레이합니다.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - 플러그인 마켓플레이스로 설치할 수 있는 엄선된 Claude Code 모음: 테마, 창, 상태 표시줄, 초상화.
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - 에이전트가 정직하게 작업하도록 하는 Claude Code 모드 — 범위를 보호하고 배포를 검증하며 프롬프트 위에 세션을 표시하는 함수 훅.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - 내 Claude Code 모음으로, 디렉터리마다 모드 하나씩 포함.
- [Ankitrai97/rai-claude-mods](https://github.com/Ankitrai97/rai-claude-mods) - 무료 Claude Code 모드 5개: Simple Mode, Usage Tally, Context Handoff, Inbox Alerts 및…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Claude Code 모드: 컨텍스트 바, 에이전트 패널, PDPA 블러.
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - 공장에서 갓 나온 제품입니다. Claude Code 모드: 밈을 요청하고 계속 작업하세요.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Claude Code용 모드: 프롬프트 캐시 표시줄, 다음 단계, 빠른 버튼 및 변경 사항 재생 — 마켓플레이스에서 설치 가능.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - 프롬프트 위 표시줄에 사용량 한도와 지출을 그려 주는 Claude Code 모드.
- [gecm0/skill-router-mod](https://github.com/gecm0/skill-router-mod) - skill-router mod: Jev이 각 프롬프트에 필요한 skills를 선택하고 로드합니다.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Claude Code 내부의 Claude Code mods용 앱 스토어: /mods로 2,700개의 mod를 탐색, 검색 및 설치하거나…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Herman의 Claude Code 모드 (마켓플레이스 herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Claude Code 모드: 계획을 위한 진행률 표시줄, Claude가 실행 중인 작업의 원장, 도구 출력용 토큰 마스킹.
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - 일상적인 UX를 위한 Claude Code 모드: 계획 한도, 컨텍스트 및 에이전트가 수행 중인 작업.
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - MacLeod Labs의 Claude Code 모드: streams는 세션의 뒤섞인 작업을 색상 코드가 적용된 스트림으로 풀어냅니다.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Windows에서의 Claude Code 모드에 대한 첫날 현장 노트: 컨텍스트/할당량 연료 표시줄, Thai UI 모드, Matrix 부팅…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - 내가 만들고 개인적으로 사용하는 Claude Code 모드.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Claude Code 모드: 프롬프트 위에 실시간 비용, 컨텍스트 및 플랜 할당량 미터를 표시합니다. 아이콘에는 Nerd Font가 필요합니다.
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - 하위 에이전트 확장, 대규모 컨텍스트 프롬프트 및 재시도 루프가 사용량 창을 소모하기 전에 보류하는 Claude Code 모드입니다.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - claude용 code-mods.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - 명명된 프로필을 사용해 저장소별로 전역 스킬, 에이전트, 규칙 및 도구를 켜거나 끄는 Claude Code 모드입니다.
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Claude Code용 모드: 함수 훅을 기반으로 구축된 플러그인.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - 코딩 세션을 위한 영화 스타일 크레딧. 모델 호출이나 텔레메트리가 없는 네이티브 Claude Mod입니다.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - 내가 만든 여러 claude code 모드.
- [Unayung/cc-mods-youtube](https://github.com/Unayung/cc-mods-youtube) - Claude Code 안에 cliamp를 기반으로 제공되는 YouTube 플레이어(Claude Code 모드).
- [VladLeus/claude-mods](https://github.com/VladLeus/claude-mods) - Claude Code 모드: 에이전트 플릿 대시보드 및 오토파일럿(local-mods 마켓플레이스).
- [vynnlee/mods](https://github.com/vynnlee/mods) - vynnlee의 Claude Code mods. mod마다 하나의 폴더, 하나의 마켓플레이스에서 설치 가능.
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Claude Code로 작업하면서 외국어를 익히세요.
- [20alexl/windvane](https://github.com/20alexl/windvane) - 긴 Claude Code 세션을 대신 돌봐줍니다: 컨텍스트가 차는 것을 감시하고, 체크포인트 초안을 만들고, 적절한 시점에 압축한 뒤 작업을…
- [akerskuuug/claude-mods](https://github.com/akerskuuug/claude-mods) - Claude Code 모드: 프롬프트 주변의 사용량, 한도, 브랜치 및 모델.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Claude Code Desktop에서 테마가 적용된 답변, 전체 너비 다이어그램, 컨텍스트와 한도를 한눈에 확인.
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - 에이전트가 Java을 작성할 때 Alibaba Java 규정(p3c)을 위반한 코드는 디스크에 저장되지 않습니다.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Claude Code용 실시간 비용, 토큰, 컨텍스트 사용량 사이드바: 세션 내에서 턴별 비용, 캐시 적중률, burn rate, 30일…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Claude Code mod: a backlog of the follow-ups Claude suggests across every…
- [ben-rogerson/claude-counter-strike](https://github.com/ben-rogerson/claude-counter-strike) - Claude Code용 Counter-Strike 1.6 무전 호출 - 배포 시 &quot;Fire in the hole&quot;, 긴 턴이 끝나면.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Internet radio inside Claude Code: a cliamp sidebar, mini player, favorites…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: 에이전트 그래프(소프트웨어 팩토리)를 설계하고 실행하기 위한 Claude Code 모드.
- [cephalofoil/kitt](https://github.com/cephalofoil/kitt) - 제품 개발 작업을 위한 Herdr 설정 + Claude Code 모드.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Claude Code용 macOS notch 대시보드: 사용량 제한, 열린 세션, 작업 진행률, 프롬프트 캐시 카운트다운 및 할 일 — 다섯…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude가 요리 중입니다. 팀과 채팅하세요. 친구들이 온라인에서 Claude Code 세션 바로 옆에 있습니다.
- [danielpg95/modster-hunter](https://github.com/danielpg95/modster-hunter) - Claude Code 모드: Claude이 작업하는 동안 유휴 게임에서 픽셀 아트 Modsters를 잡습니다.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Claude Code가 작업하는 동안 프롬프트 위에서 벌어지는 우주 전투.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - 각 Claude Code 에이전트가 컨텍스트에 어떤 파일을 가지고 있는지, 그리고 각각 얼마나 있는지 확인하세요.
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods for Claude Code: panes, commands and hooks built with the plugin…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - 냉정함을 유지하세요. Claude Code 사용일을 위한 온도계입니다.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Claude Code mod: a live pane of the GitHub PRs a session opens or pushes to…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - 터미널 및 데스크톱 앱용 소형 Claude Code 모드.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - 에이전트 응답에 스페인어 단어를 추가하는 Claude CLI skill + mod.
- [Fazzani/claude-mods](https://github.com/Fazzani/claude-mods) - Claude Mods.
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - 이를 Person of Interest의 The Machine처럼 재스타일링하는 Claude Code 모드입니다.
- [hellosverre/smart-compact](https://github.com/hellosverre/smart-compact) - 적절한 순간(커밋 후, 테스트가 통과된 후, 프롬프트 캐시가 만료되기 전)에 compact하거나 Claude이(가) 요청할 때…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: 라이브 DAG 패널이 있는, 필수 및 검증된 subagents의 DAG workflows를 위한 Claude Code…
- [i-harsha-reddy/naruto-mod](https://github.com/i-harsha-reddy/naruto-mod) - Claude Code를 위한 픽셀 아트 Naruto 동반자: Claude이(가) 작업하는 동안 20명의 닌자와 60개의 인술이 실행됩니다.
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Claude Code를 위한 오픈 소스 모드: 창, 상태 줄, 토스트, 도구 가드 및 슬래시 명령.
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - 각 서브에이전트와 해당 에이전트가 건드리는 파일, 그리고 세션의 사용량과 비용을 위한 패널을 제공하는 Claude Code 모드입니다.
- [joeVenner/claude-code-mods](https://github.com/joeVenner/claude-code-mods) - Claude Code mods, plugins, skills, agents, hooks 및 MCP servers의 커뮤니티 디렉터리.
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Claude Code mod: 세션 상태, 실시간 Spec Kit 진행 상황 및 사용량 창 거버넌스.
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - 프롬프트 위에 한 줄로 표시되는 컨텍스트 창으로, Claude Code가 자체 미터를 그리는 방식으로 표현됩니다.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Claude Code 터미널 UI를 Claude 데스크톱 앱처럼 보이게 하는 Claude Code plugin (mod): 프롬프트 버블…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Claude Code가 백그라운드에서 실행하는 항목을 확인하세요: 서브에이전트, Codex 작업, 셸, 모니터, cron 작업 및…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - A free, open-source plugin for Claude Code.
- [manuacl/claude-mods](https://github.com/manuacl/claude-mods) - 개인용 Claude Code 모드: 프롬프트 위에 컨텍스트 날씨와 계정 한도를 표시하는 otto-hud, Otto the octopus.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - 세션의 GitHub개 풀 리퀘스트를 트랜스크립트 옆 창에 표시하는 Claude 모드: 설명을 프롬프트 상자에 인용하고 검사 및 리뷰 상태를…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude Code 도구 호출용 디버거인 Claude DevTools.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Claude Code 스킬: 문서 팩트체커, 코드 감사기, 버그 메모리 로그, 모드 등.
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Claude Code 버디 플러그인: 프롬프트 위에서 규칙을 기억하고 Claude의 단축키를 알려 주는 ASCII 동반자.
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - 에이전트별 도구 가시성을 위한 Claude Code 플러그인 — 각 루프마다 서브에이전트, 스킬, MCP 및 내장 도구를 숨기고 거부합니다.
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code 모드: Jev에 기반한 모델/작업량 라우팅, 원문 그대로의 컨텍스트 압축 및 더 저렴한 장시간 세션을 위한 출력 다듬기.
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Code 모드: Claude Code를 위한 보안 계층 — 비밀 정보 삭제, 신뢰할 수 없는 콘텐츠 알림, MCP 도구 포이즈닝…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - Claude Code mods 모음.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Claude Code 플러그인 및 모드: 훅으로 강제되는 인간 승인 게이트와 프롬프트 위 상태 표시줄을 갖춘 AI 네이티브…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Awesome Claude Code mods 컬렉션 | 클로드 코드 모드 모음집.
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Claude Code 플러그인(모드): 여러 Claude 계정 간 전환, 상태 밴드에서 사용량 제한 확인, 터미널 패널에서 에이전트…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 테스트 완료, 한 번의 명령으로 설치 가능한 Claude Code 모드: YOLO 모드용 가드레일, 실시간 비용 및 컨텍스트, 패널, 펫…
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: 로컬 오픈 소스 Kokoro TTS 음성으로 요청 시 Claude의 답변과 사용자의 프롬프트를 소리 내어 읽어주는…
- [tommy5dollar/effort-router](https://github.com/tommy5dollar/effort-router) - Claude Code 사용량을 최대 두 배까지 늘리세요. 각 프롬프트와 서브에이전트에 적절한 추론 작업량을 선택하는 플러그인입니다.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - 실시간 창, 비용을 고려한 모델 라우팅 및 안전 가드를 위한 Claude Code 모드: 한 번의 명령으로 마켓플레이스에서 설치하세요.
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Claude Code 모드 및 플러그인: 사용량 모니터, 토큰 추적기 및 상태 줄.
- [Verinoda-Labs/verinoda-symbiosis](https://github.com/Verinoda-Labs/verinoda-symbiosis) - Verinoda + Claude Code, 함께: Verinoda와 verinoda-live, 코드 인덱스를 최신 상태로 유지하고, 에이전트가…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - 간단한 결정을 저렴한 decision model에 맡기는 Claude Code 모드: 라우팅, 스킬, 인젝션 검사, /compact-jev.
- [vumichien/claude-code-mods-kit](https://github.com/vumichien/claude-code-mods-kit) - Three free Claude Code mods: hide .env values from tool results, watch a remote…
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Claude Code mods. touch-map: Claude가 나열, 읽기, 편집 또는 생성한 파일을 트리와 activity map으로…
- [Yanir-R/catchup](https://github.com/Yanir-R/catchup) - 읽지 않은 에이전트 메시지를 쉬운 영어로 요약하는 Claude Code mod.
- [Yuvalz19500/claude-mods](https://github.com/Yuvalz19500/claude-mods) - Mods for Claude Code: live panes, bands and hooks. A plugin marketplace.
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [0xnicholasy/claude-mod-collapse-tools](https://github.com/0xnicholasy/claude-mod-collapse-tools) - Claude Code mod: collapses every tool-call row in the transcript to one line;
- [0xnicholasy/claude-mods](https://github.com/0xnicholasy/claude-mods) - Claude Code plugin marketplace for 0xnicholasy.
- [AbyssCN/claude-lead-harness](https://github.com/AbyssCN/claude-lead-harness) - Claude Code 모드 + cheap-executor 드라이버: 하나의 Claude 세션을 리드로 사용하고, MiniMax Code를…
- [AdamCaviness/cache-magic](https://github.com/AdamCaviness/cache-magic) - Claude Code mod that auto writes a handoff before a large session.
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - afterever의 Claude Code 모드(플러그인 마켓플레이스).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [akixi-maison/usage-mods](https://github.com/akixi-maison/usage-mods) - Claude Code mod: usage progress bars (context, 5h, 7d) and a compact button…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Claude Code 프롬프트 위에 표시되는 애니메이션 점자 고양이.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Claude Code 모드: 저렴한 작업은 하위 Claude Code를 통해 GLM/Kimi로 라우팅하고, 중요한 작업은 구독에서 유지합니다.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - OmniDimension 음성 에이전트 테스트 호출을 실행하는 Claude Code 프롬프트 위의 픽셀 고양이. Claude Code mod.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - 컨텍스트 창을 작게 유지할 수 있도록 압축하기 좋은 시점을 선택하는 Claude Code 모드.
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Claude Code용 Claude Mods: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - anderson-spider의 Claude Code 플러그인 마켓플레이스.
- [angomedia/claude-mods](https://github.com/angomedia/claude-mods) - Mods for Claude Code.
- [ankits3a/cache-keeper](https://github.com/ankits3a/cache-keeper) - Claude Code 모드: prompt-cache 밴드, keep-warm, handoff judge trial.
- [antonisPanos/claude-mods](https://github.com/antonisPanos/claude-mods)
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - 코드가 변경될 때마다 LGTM Lines 우주선이 지나갑니다 — Claude Code 모드.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - 애니메이션 주민 체력 카드로 표시되는 Claude 사용 한도 — Claude Code 모드.
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - S2 팀용 Claude Code 모드(the ather marketplace).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - Claude이(가) 평이한 영어를 사용하도록 만들고 일반적인 글쓰기 습관을 표시하는 Claude Code 모드입니다.
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Claude이 작업하는 동안 하는 짧은 운동: 일일 목표, 연속 기록, 배지 및 선택적 리더보드. Claude Code 모드.
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Claude Code용 사용량 보드: 모델별 지출(오늘, 이번 주, 이번 달, 전체 기간) 및 주간 한도 예측.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - A Claude Code mod: live context-window breakdown above the prompt.
- [bastianfuchs/claude-code-cache-warm](https://github.com/bastianfuchs/claude-code-cache-warm) - 푸터에 prompt-cache 카운트다운을 표시하고 자리를 비운 동안 5분 캐시를 따뜻하게 유지하는 Claude Code 모드입니다.
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Claude Code용 Now Playing mod: 프롬프트 위에 앨범 아트, 컨트롤 및 Up next 창과 함께 표시되는 Apple…
- [bennewton999/claude-code-mods](https://github.com/bennewton999/claude-code-mods) - 여러 세션을 동시에 실행하기 위한 Claude Code 모드 5개: 플릿 보드, PR-to-production 추적기, 규칙 트립와이어…
- [berkayburakk/berko-mods](https://github.com/berkayburakk/berko-mods) - Claude Code mod pack from the Berko video: Mask, View, Guard, Saving, Chime +…
- [bhargava-gumpula/claude-mods](https://github.com/bhargava-gumpula/claude-mods) - Claude Code mods: 사용량 밴드, 채팅 참가자 목록, /cube, /handoff, 프롬프트 정리.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Claude Code용 모드: 캐시 시계, Blast Radius, 제안, 작업 목록, Grill.
- [C-M-Jones/suggestion-spotlight](https://github.com/C-M-Jones/suggestion-spotlight) - Claude Code mods: Suggestion Spotlight가 Claude이(가) 제안한 다음 프롬프트가 무엇을 가리키는지 보여줍니다.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - 당신의 Claude Code를 위한 그냥 올빼미.
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - 한 줄짜리 Claude Code 밴드(캐시 카운트다운, 컨텍스트, 제한, 다음 작업)와 7개의 커뮤니티 모드를 하나의 플러그인으로 설치하며…
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - Freedoom이 포함된 오리지널 Doom 엔진으로, Claude Code 안에서 플레이 가능. Mac Apple Silicon 알파 버전.
- [cmorss/claude-mods](https://github.com/cmorss/claude-mods) - git worktree를 위한 Claude Code mods: /terminal과 /worktree-files가 대화가 작업 중인…
- [Dandeppert/Claude-mods](https://github.com/Dandeppert/Claude-mods)
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Claude Code 안에 사는 Tamagotchi: 부화하고, Claude이(가) 작성한 코드를 먹고, 버그를 남기며, 여덟 종류의 성체 중…
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Claude Code 터미널 대화 내 북마크 및 vim 스타일 마크: 줄을 강조 표시하고, 표시한 뒤, 다시 이동합니다.
- [degterev/swiftui-preview-mod](https://github.com/degterev/swiftui-preview-mod) - Claude Code 모드: Xcode가 렌더링한 SwiftUI 프리뷰를 터미널 창에 표시.
- [delexw/codyssey](https://github.com/delexw/codyssey) - 모든 Claude Code 세션을 작은 모험으로 바꿉니다. 에이전트의 기분을 따라가는 생성 음악, 편집과 명령마다 몬스터와 싸우는 픽셀 기사…
- [derekwden-droid/message-timestamps](https://github.com/derekwden-droid/message-timestamps) - 터미널과 데스크톱 앱에서 각 프롬프트와 답변의 시간을 표시하는 Claude Code 모드.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - 함수 훅으로 작성된 Claude Code 모드와 이를 제공하는 마켓플레이스. dash: 한 패널에 있는 세션의 대시보드.
- [DiegoCarrillo32/claude-plugins](https://github.com/DiegoCarrillo32/claude-plugins) - Claude Code 모드 및 디자인 시스템: crab-crew와 Crab Crew 디자인 시스템.
- [DiegoHeer/claude-mods](https://github.com/DiegoHeer/claude-mods) - My Claude Code mods, shared as a plugin marketplace.
- [divramod/divramod-claude-code-mods](https://github.com/divramod/divramod-claude-code-mods) - divramod의 Claude Code 모드: Claude Code 인터페이스를 위한 실시간 패널 및 조정 기능.
- [DominikSch004/claude-mods](https://github.com/DominikSch004/claude-mods) - 모든 컴퓨터에서 사용하는 Claude Code mods: savvy-progress, filetree, skins, blast-radius.
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Claude Code mod: after a guard blocks a tool call, it stops recognized detours…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Claude Code mod: one inbox for messages from teammates, named subagents and…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Claude Code mod: explains sandbox blocks and turns repeated blocks into…
- [drprofi114-star/claude-mods](https://github.com/drprofi114-star/claude-mods)
- [duylinhdang1998/my-claude-mods](https://github.com/duylinhdang1998/my-claude-mods)
- [EggmanPDX/claude-mods](https://github.com/EggmanPDX/claude-mods) - mods.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - 이봐요, 음소거했어요! diff를 버리고 장단을 끊으세요. 더 이상 편집도, 크레딧 차감도 없습니다.
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Desktop 앱과 터미널에서 프롬프트 위 밴드로 구독 사용량(5h / 7d)을 표시하는 Claude Code mod.
- [fanoisme/claude-mods](https://github.com/fanoisme/claude-mods) - Claude Code를 위한 모션 디자인 mods: 모델, effort, context, 사용량 제한, 작업 진행률, subagents 및…
- [Flo0806/fh-claude-mods](https://github.com/Flo0806/fh-claude-mods) - Claude Mod Marketplace.
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - 프롬프트 위에서 병렬 브랜치와 worktree를 실시간으로 보여 주는 레이더: 어떤 항목이 깔끔하게 병합되는지, 어떤 항목이 충돌하는지, 어떤…
- [Gabrielmtvp/claude-code-mods](https://github.com/Gabrielmtvp/claude-code-mods) - 내 Claude Code 모드.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Claude Code를 위한 모드 및 스킨: Claude의 작업을 위한 실시간 진행률 표시줄, 이에 맞는 Windows Terminal…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [gauravruhela07/claude-mods](https://github.com/gauravruhela07/claude-mods) - Seven Claude Code mods: savvy-progress, skins, filetree, cache-tax…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Claude Code 답변의 모든 코드 블록에서 Ctrl+클릭으로 링크 복사.
- [gecm0/jev-mod](https://github.com/gecm0/jev-mod) - jev mod: Claude Code용 $.jev, TypeSafe Jev의 형식이 지정된 판단.
- [Gersom/claude-mod-cache-watch](https://github.com/Gersom/claude-mod-cache-watch) - Claude Code 모드: 프롬프트 캐시가 따뜻한지 차가운지 표시하는 패널.
- [Gersom/gersom-claude-mods](https://github.com/Gersom/gersom-claude-mods) - Claude Code용 Mods: usage-meter 같은 hook 플러그인.
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - 하나의 마켓플레이스를 통해 설치하는 Claude Code mods(function-hook plugins).
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Claude Code용 Evangelion 스타일 사이드바: 컨텍스트, 할당량, 활동, PR, 하드웨어, 세션 및 forge 패널.
- [gsporto226/claude-mods](https://github.com/gsporto226/claude-mods) - 유용한 claude code 모드.
- [Gxrco/Screen-peek](https://github.com/Gxrco/Screen-peek) - Claude-Code Plugin(Mod)을 사용하면 모델이 작업하는 동안 무엇을 하고 있는지 볼 수 있습니다.
- [hamTotk/better-rewind](https://github.com/hamTotk/better-rewind) - Claude Code mod: rewind or summarize from any prompt or AskUserQuestion answer.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [hellosverre/redgreen](https://github.com/hellosverre/redgreen) - Claude Code 패널의 테스트 결과: Claude 자체 테스트 실행의 실패, 세부 정보 및 실행 기록.
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Claude Code 모드: 각 답변에 걸린 시간, Claude이(가) 생각한 시간, tok/s를 Claude desktop app의 답변…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - 작은 Claude Code 모드: 컨텍스트 및 plan 사용량 게이지, prompt-cache 미터 및 살펴볼 항목을 표시하는 패널.
- [Jang-seungminn/usage-hud](https://github.com/Jang-seungminn/usage-hud) - Claude Code mod: usage HUD above the prompt with two animated ASCII dogs.
- [jeffyfung/claude-mods](https://github.com/jeffyfung/claude-mods) - 내 claude 모드를 보관하는 곳입니다.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - 사이드바의 context 사용량 패널: 총량, 분류, 라운드별 증가량, 가장 많은 공간을 차지하는 항목, 캐시, Claude이(가) 현재 하는…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - 사이드바의 파일 목록: 이번 대화에서 어떤 파일을 새로 만들고, 수정하고, 삭제했는지와 각각 몇 줄을 변경했는지 표시합니다.
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 입력창 위를 뛰어다니는 8비트 스타일의 毛毛(흑백 네덜란드 드워프 롭 토끼): 대기 중에는 납작 엎드리고, 작업 중에는 달리며, 도구를 사용할…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - 사이드바의 ‘내가 물어본 것’: 이번 대화에서 주인이 입력한 모든 문장을 클릭 한 번으로 전체 보기, 복사 및 입력창으로 되돌리기.
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - 사이드바의 타임라인: 이번 라운드의 시간이 어디에 사용되었는지 표시합니다.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - 사이드바의 토큰 왕래: 주 대화에서 매번 Anthropic에 몇 개의 토큰을 보내고, 얼마나 기다렸으며, 몇 개를 받았는지 표시하고 맨 위에…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - claude code의 솔직한 속마음: 매 라운드의 답변이 끝나면 Claude이(가) 속마음을 한마디 조용히 말합니다.
- [jgilb17/claude-mods](https://github.com/jgilb17/claude-mods)
- [Jh-jaehyuk/plan-checklist](https://github.com/Jh-jaehyuk/plan-checklist) - Claude Code용 증거 기반 계획 체크리스트: 승인된 계획은 Claude이(가) 검증 증거가 있을 때만 체크할 수 있는 체크리스트가…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - 새 슬래시 명령 및 사이드 패널과 같은 Claude Code용 작은 모드.
- [jkf87/mod-guide](https://github.com/jkf87/mod-guide) - Unofficial community guide to Claude Code mods (function hooks) in 6 languages…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Claude Code용 모드 카탈로그.
- [jpo-oss/claude-games](https://github.com/jpo-oss/claude-games) - Claude Code가 작업하는 동안 내부에서 플레이할 수 있는 멀티플레이어 게임.
- [juliomyitbrain/claude-code-git-graph](https://github.com/juliomyitbrain/claude-code-git-graph) - Claude Code 모드: 저장소의 커밋 그래프와 클릭한 커밋의 세부 정보를 그리는 패널.
- [justmytwospence/claude-cache-guard](https://github.com/justmytwospence/claude-cache-guard) - Claude Code 모드: 자리를 비운 동안 프롬프트 캐시를 따뜻하게 유지하고, 대규모 대화를 다시 캐시하게 될 프롬프트 전에 확인.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd는 Claude Code 프롬프트 위의 밴드에 삽니다: 세션을 연기하고, 실행 중인 항목, context 및 usage limits를…
- [kaicodedocument/claude-code-usage-bar](https://github.com/kaicodedocument/claude-code-usage-bar) - 프롬프트 위에 속도 제한 허용량, 세션 토큰 및 비용을 표시하는 Claude Code 모드.
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Claude Code의 응답과 알림을 VOICEVOX / Irodori-TTS 등으로 읽어주는 mod.
- [Kareem1809/chat-cigarette](https://github.com/Kareem1809/chat-cigarette) - 🚬 A Claude Code mod: a cigarette burns down with every message — when it.
- [KashifManzer/clear-caption](https://github.com/KashifManzer/clear-caption) - A Claude Code mod that adds plain-language captions and state markers to tool…
- [kba977/claude-code-pomodoro](https://github.com/kba977/claude-code-pomodoro) - A pomodoro timer above the Claude Code prompt (Claude Code mod).
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Claude Code 세션 간의 대화를 읽고 참여하는 Claude Mod (/crosstalk).
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - 편의성/사용성 개선 Claude 모드.
- [kjhq/haiku-compact](https://github.com/kjhq/haiku-compact) - haiku로 차가운 claude code 세션을 압축하세요 — 절약한 내용을 보여주는 한 줄 캐시 밴드.
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - 두 가지 Claude Code 모드: 채팅 옆의 파일 패널인 folio와 상태 줄이 포함된 터미널 세션 재스타일링인 tint.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Claude Code Desktop용 실시간 작업 HUD: Claude이(가) 작업하는 동안 프롬프트 위에 표시되는 스트립과, 한 번 클릭하면…
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [loucimj/turn-chime](https://github.com/loucimj/turn-chime) - Claude Code mod: chime after 40s turns, spoken announcement after 5-minute turns.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - 사용 사례, 원본 데모, 호환성 근거 및 안전 참고 사항을 담은 커뮤니티 큐레이션 Claude Code Mods 가이드: 영어 / 中文.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - iTerm2 탭 부제목에 Claude이(가) 무엇을 하고 있는지 표시하여, 탭 표시줄을 한눈에 보고 어느 세션에 사용자의 주의가 필요한지 알…
- [m-tababi/delegation-guard](https://github.com/m-tababi/delegation-guard) - 주 세션이 subagents에 위임하도록 유도하고 프롬프트 위에 주 컨텍스트 토큰과 위임된 토큰을 비교해 보여주는 Claude Code mod.
- [MahadSalim/claude-mods](https://github.com/MahadSalim/claude-mods) - 개인 claude 모드 플러그인 모음.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [marcelmatula/claude-mods](https://github.com/marcelmatula/claude-mods) - 하나의 플러그인 마켓플레이스(marcel-mods)에 모은 Marcel의 Claude Code 모드.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - 전환 가능한 권한 프로필을 제공하는 Claude Code 모드: 안전한 기본 프로필, 켜고 끌 수 있는 이름 지정 프로필, 그리고 그 외 모든…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Claude Code를 위한 커뮤니티 모드: Claude Code 내부에서 실행되는 가드, 패널 및 명령. 마켓플레이스: modhub.
- [mina-asham/claude-usage-stats](https://github.com/mina-asham/claude-usage-stats) - A Claude Code mod that shows your plan usage.
- [mmedum/glimt](https://github.com/mmedum/glimt) - Claude Code를 위한 조용한 사이드 패널: 이 세션이 수행 중인 작업, 계획, 에이전트 및 다른 모든 세션.
- [mmedum/spor](https://github.com/mmedum/spor) - Claude Code가 접어 숨기는 내용을 다시 표시합니다: Claude이(가) 읽은 파일, 실행한 명령, 각 턴에서 수행한 작업.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - 세션 시작 시 CLAUDE_CODE_ENABLE_TODO_TOOLS를 설정하여 todo 도구를 제외하는 모델에서도 다시 활성화하는 Claude…
- [muellerei/task-line](https://github.com/muellerei/task-line) - 프롬프트 위 작업 목록에 현재 작업, 진행률 막대 및 개수를 작업당 한 줄로 표시하는 Claude Code 모드.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Claude Code 내부에서 AI를 상대로 Connect Four 플레이 (/connect-four).
- [Nachx639/context-canary](https://github.com/Nachx639/context-canary) - Claude Code용 픽셀 아트 카나리아: Claude이(가) 사용자의 지시를 따르지 않으면 죽었다가 자동으로 압축된 후 되살아납니다.
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - 다른 코딩 에이전트가 저장소에 커밋하면 Claude이(가) 이를 감지하고 해당 보고서를 신뢰하는 대신 diff와 테스트로 감사하는 Claude…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - 여러 AI 에이전트가 공유하는 저장소를 위한 Claude Code 모드: 비밀 값이 .env 밖으로 나가거나 공개 원격 저장소로 푸시되는 것과…
- [Nexus-nimdA/null-radio](https://github.com/Nexus-nimdA/null-radio) - Claude Code를 위한 사이버 네온 인터넷 라디오 창 - synthwave 다이얼, 현재 재생 중, VU, 로컬 ffplay.
- [niksavis/handily](https://github.com/niksavis/handily) - 모든 트래커에서 작업 항목, 태스크 및 세션을 표시하는 Claude Code Mods입니다. Mods는 표시하고 질문할 뿐, 강제하지 않습니다.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Claude Code에서 SQL을 위한 가드레일: DB CLI를 통해 Claude이 DELETE, WHERE 없는 UPDATE, DROP…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Claude Code, Windows 및 CJK를 우선하는 하나의 모드: 모든 터미널에서 붙여넣은 이미지 및 텍스트 미리보기, CJK에 맞는…
- [oguz-hd/claude-code-chime](https://github.com/oguz-hd/claude-code-chime) - Claude Code용 Chime: Claude이(가) 완료하거나, 사용자의 입력을 필요로 하거나, 오류가 발생할 때 소리를 냅니다.
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: 이미지 썸네일 및 상태 표시줄.
- [onk3sh/fix-on-edit](https://github.com/onk3sh/fix-on-edit)
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - 무엇을 해 주는지에 따라 정렬한 최고의 Claude Code Mods. 직접 확인하여 각 항목을 한 줄로 정리했습니다.
- [oscarcosmedev/claude-mods](https://github.com/oscarcosmedev/claude-mods)
- [ozdeger/claude-looked-at-mod](https://github.com/ozdeger/claude-looked-at-mod) - Claude Code 모드: 에이전트가 확인한 모든 이미지와 파일(스크린샷, 렌더링 결과, 읽은 파일)을 Claude 데스크톱 앱의 패널에서…
- [pablodiazjorge/impact-radius](https://github.com/pablodiazjorge/impact-radius) - 위험한 셸 명령(rm -rf, git reset --hard, 강제 push, 마이그레이션, 전역 설치, curl | sh…)을 보류하고…
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Claude Code용 Claude Mods 두 가지: garde-du-corps.
- [paragpandyareal/lazy-panda-panel](https://github.com/paragpandyareal/lazy-panda-panel) - Claude Code용 Lazy Panda Panel: 발 하나 들지 않고 문서를 검토하세요.
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Swear at Claude Code and a cartoon hand slaps back.
- [paulpc2/claude-code-mods](https://github.com/paulpc2/claude-code-mods) - Claude Code mods: usage-both shows 5-hour and weekly usage above the prompt.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Claude 데스크톱 앱의 Code 탭을 위한 실시간 세션 통계 사이드 패널: 컨텍스트, 비용, git 변경 사항, 턴 통계, 하위 에이전트…
- [pkkid/claude-mods](https://github.com/pkkid/claude-mods) - 내 Claude Desktop 설정을 위한 다양한 모드와 스킬.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Claude Code용 모드: safety-guard는 파괴적인 명령과 비밀 파일 접근을 차단하고, notify-router는 규칙 기반…
- [prompteafacil-hub/mods-claude-code](https://github.com/prompteafacil-hub/mods-claude-code) - prompteafacil 커뮤니티의 Claude Code 모드.
- [ptpmediabr/ideas-shelf](https://github.com/ptpmediabr/ideas-shelf) - 프로젝트별 아이디어 선반: 패널에 아이디어를 적고 완료된 것으로 표시하세요. 프로젝트 루트의 IDEAS.md에 저장됩니다.
- [ptpmediabr/mods-manager](https://github.com/ptpmediabr/mods-manager) - 모드와 플러그인을 확인하고, 켜고, 끄고, 설치하고, 프로필로 그룹화하는 패널.
- [ptpmediabr/side-chat](https://github.com/ptpmediabr/side-chat) - 세션 내부의 사이드 채팅 패널로, 선택한 모델에서 질문에 답하거나 요청을 실행.
- [ptpmediabr/usage-weather](https://github.com/ptpmediabr/usage-weather) - 프롬프트 위에 표시되는 조용한 한 줄: 컨텍스트, 5시간 및 주간 사용량, 프롬프트 캐시가 준비되었는지 여부, 그리고 지우고 계속하기 버튼.
- [qarge/claude-mods](https://github.com/qarge/claude-mods)
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Claude Code mod: 실시간 주식 티커, /quote 패널, 가격 알림, 시장 밴드, 모델이 호출할 수 있는 quote 도구.
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Claude Code mod: 프롬프트 위 한 줄에 SSH 호스트, RAM 및 5h/7d 사용량 제한 표시.
- [Rinze-Smits/ifc-viewer-claude-mod](https://github.com/Rinze-Smits/ifc-viewer-claude-mod) - IFC Viewer mod for Claude Code.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Claude Code 모드: Claude이(가) 작업하는 동안 할 팔굽혀펴기. 토큰 없음.
- [Rsclub22/claude-mods](https://github.com/Rsclub22/claude-mods)
- [RyanWeera/ai-router](https://github.com/RyanWeera/ai-router) - A Claude Code mod that routes tasks to other AI models.
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - Claude Code용 모드 상점: GitHub에서 모드를 스크랩하고, 미리 보고, 마켓플레이스를 호스팅합니다.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Claude Code 모드: plan mode에서 승인한 계획을 프롬프트 위의 라이브 체크리스트로 바꾸고, Claude이 완료할 때마다 각…
- [sadhirr1/claude-mods](https://github.com/sadhirr1/claude-mods) - 다양한 claude 모드가 있는 저장소일 뿐입니다.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - 엄선한 Claude Code 모음입니다. 모든 항목을 복제하고 claude plugin validate로 확인했으며, 건드릴 수 있는 항목을…
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - 비용 없는 모드: 도우미 에이전트는 Haiku에서 실행되고, 큰 파일과 로그는 Claude의 컨텍스트를 채우는 대신 무료 Gemini 모델이…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - 세션을 따라가는 로파이 사운드트랙: 차분함, 집중, 몰입과 테스트 통과 및 실패를 알리는 신호음. 오리지널 음악입니다.
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Claude이(가) 코딩하는 동안 학습하세요: 코드를 변경한 턴이 끝나면 해당 변경 사항에 관한 질문 하나가 프롬프트 위에 나타납니다.
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Claude이(가) 수행하는 모든 편집을 기록한 테이프: 각 변경 사항이 직접 입력되는 모습을 재생하고, 단계별로 살펴보며, 모든 파일을…
- [samaphp/session-links](https://github.com/samaphp/session-links) - 세션에서 언급한 모든 링크를 프롬프트 위 한 줄에 표시합니다. Claude Code 모드.
- [SanjayPG/claude-code-usage-tracker](https://github.com/SanjayPG/claude-code-usage-tracker) - Claude Code 모드: 프롬프트 위에 실시간 사용량 할당량 진행률 표시줄을 표시합니다.
- [sawzhang/hello-mod](https://github.com/sawzhang/hello-mod) - Claude Code 함수 훅 최소 데모: prompt 위의 실시간 token/비용 패널, 클릭 가능한 버튼, 독립적으로 그리는 스레드…
- [shelltime/claude-code-mods](https://github.com/shelltime/claude-code-mods) - ShellTime의 Claude Code 모드(function-hook 플러그인).
- [siller/supermod](https://github.com/siller/supermod) - Claude Code 모드: 프롬프트 위에 Superpowers 진행률, 컨텍스트 창 및 에이전트를 표시합니다.
- [skryvets/claude-status-bar-mod](https://github.com/skryvets/claude-status-bar-mod) - Claude Code 모드: 프롬프트 아래에 세션 정보를 색상으로 표시합니다.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Claude Code용 아늑한 RPG HUD 모드.
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 개인 Claude Code 모드 마켓플레이스: clean-view, where-am-i, next-steps…
- [Steady-Matter/spotter-pals](https://github.com/Steady-Matter/spotter-pals) - Spotter: a Claude Code mod with pixel Pals that hatch and grow as your helper…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - 춤추는 pixel-art Malenia와 함께 Claude Code용 원클릭 commit messages.
- [stillgbx/still-mods](https://github.com/stillgbx/still-mods) - Claude Code 모드.
- [stylusnexus/claude-mods](https://github.com/stylusnexus/claude-mods)
- [su-record/claude-mods](https://github.com/su-record/claude-mods) - Personal Claude Code mods.
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code 모드 — marketplace sunkanxx-mods.
- [Suyeo2025/claude-mods](https://github.com/Suyeo2025/claude-mods) - Claude Code 모드: 미니 바 HUD.
- [SyntacticFlow/claude-mods](https://github.com/SyntacticFlow/claude-mods) - Claude Code용 플러그인.
- [systemNEO/claude-code-mods](https://github.com/systemNEO/claude-code-mods) - Claude Code용 모드: delete-guard (프로젝트 폴더 외부에서 삭제하려면 승인이 필요함).
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Claude Code 모드: 프롬프트 바로 위에서 Claude 요금제 사용량(세션 + 주간 한도, 재설정 카운트다운, 컨텍스트)을 확인합니다.
- [tanwar-harsh/luff-crew-monitor](https://github.com/tanwar-harsh/luff-crew-monitor) - Claude Code 모드: 모든 서브에이전트를 위한 실시간 크루 패널(모델, 작업량, 단계, 컨텍스트, 비용, 시간), 프롬프트 위의 작업…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [teambrilliant/claude-code-mods](https://github.com/teambrilliant/claude-code-mods)
- [TFoxik/claude-model-router](https://github.com/TFoxik/claude-model-router) - 작업 종류별로 모델과 작업 강도를 선택하고 해당 선택에 드는 비용을 보여주는 Claude Code 모드입니다.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - 현재 세션을 창에 표시하는 Claude Code 모드입니다. 각 프롬프트, 해당 프롬프트에 대해 Claude이(가) 단계별로 수행한 작업…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - mods용 Claude Code plugin marketplace: Claude Code 내부에 bands, panes 및 기타 UI를 그리는…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Claude Code mods on demand — a skill that reads your conversation and builds…
- [tjanuki/claude-mod-agent-board](https://github.com/tjanuki/claude-mod-agent-board) - Claude Code 모드: 세션의 하위 에이전트와 상태를 보여주는 도킹된 창.
- [tksunw/usage-reporter](https://github.com/tksunw/usage-reporter) - Claude Code mod that writes your Claude usage limits to a file other tools can…
- [Tum4s/sprout](https://github.com/Tum4s/sprout) - Claude Code 모드: 서브에이전트와 해당 에이전트가 사용하는 파일을 추적하는 밴드 및 패널.
- [tusharck/mods-for-claude](https://github.com/tusharck/mods-for-claude) - 엄선된 Claude Code 모드 카탈로그로, 각 모드에는 직접 빌드할 수 있는 복사-붙여넣기 프롬프트가 포함되어 있습니다.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Tempered Works의 Claude Code 모드: ship-state, timeline, limit-resume — 그리고 Codex…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Claude Code mod: 5h/7d quota, context window, prompt-cache time left and…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Claude Code 모드: 장시간 실행되는 작업을 위한 애니메이션 진행 밴드와 완료 요약.
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - 작은 Claude Code 모드 세 가지입니다. 하위 에이전트가 언제 완료되는지 확인하고, Claude이(가) 완료된 후 보낼 메시지를…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - &quot;I.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - 작업 옆의 패널에서 Claude에게 별도 질문을 하세요. 기본 대화에는 표시되지 않습니다. 데스크톱 앱의 /btw처럼 작동합니다.
- [Victormartinsilva/MODS-CLAUDECODE](https://github.com/Victormartinsilva/MODS-CLAUDECODE) - 한 단계 설치와 포르투갈어 동영상 가이드를 제공하는 Claude Code 모드 마켓플레이스.
- [vihrea1337/headroom](https://github.com/vihrea1337/headroom) - Claude Code의 속도 제한 카운트다운 및 소모 속도 예측.
- [vinkdc/roclaude](https://github.com/vinkdc/roclaude) - Claude Code용 Roblox Studio 안전 레이어: RemoteEvent 감사, 실행 취소, Team Create 보호 및…
- [wipeer/claude-mods](https://github.com/wipeer/claude-mods) - Claude Code용 작지만 편리한 모드.
- [wmaq/wmaq-claude-mods](https://github.com/wmaq/wmaq-claude-mods) - Claude Code 모드: stage-toons, 픽셀 아트 Clawd 만화와 함께 프롬프트 위에 워크플로 진행률 표시줄을 표시합니다.
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Claude Code용 모드. agent-crew: 역할, 모델, 현재 도구, 진행률, 토큰 및 시간을 표시하는 실시간 픽셀 크루로…
- [YeonwooSung/my-claude-code-mods](https://github.com/YeonwooSung/my-claude-code-mods)
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - A live task board for Claude Code: plan before building, follow every task…
- [youngOman/pill-mods](https://github.com/youngOman/pill-mods) - Claude Code 모드: 繁中 다음 단계 캡슐, 블록 복사, 스티커 썸네일.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - 데스크톱과 터미널에서 Claude Code 프롬프트 위에 항상 표시되는 밴드: 컨텍스트 사용량 및 속도 제한 창.
- [zh10only1/claude-code-mods](https://github.com/zh10only1/claude-code-mods) - 개인용 Claude Code 모드(플러그인 마켓플레이스).
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - 최고의 에이전트를 위한 최고의 리소스를 엄선한 컬렉션입니다. 코딩 동반자의 논란의 여지 없는 챔피언인 Claude Code를 비롯해, 막강한…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - 컨텍스트 사용량, 활성 도구, 실행 중인 에이전트 및 할 일 진행 상황 등 현재 상황을 보여주는 Claude Code 플러그인입니다.
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 powerline 지원, 테마 등을 제공하는 Claude Code CLI용 아름답고 높은 사용자 지정성을 갖춘 상태 표시줄입니다.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Claude Code 시스템 프롬프트의 모든 부분, 기본 제공 도구 설명 27개, 하위 에이전트 프롬프트(Plan/Explore/Task)…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 기초부터 고급까지 Claude Code를 최대한 활용하기 위한 45개 이상의 팁을 제공합니다.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — Xiaohongshu 캐러셀 및 WeChat 21:9+1:1 커버 쌍 생성.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Claude Code를 위한 아름다운 vim 스타일 powerline.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - 터미널 창에서 코딩 에이전트의 diff를 검토하고 줄 단위 주석을 Claude Code, Codex, OpenCode 또는 Pi로 보냅니다.
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - 컨텍스트 사용량, API 속도 제한 및 비용 추적을 포함한 Claude Code용 종합 상태 표시줄 플러그인.
- [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) - Claude Code 및 Codex 로컬 token 추적 — 상태 표시줄(Codex 업계 최초의 가짜 statusline), GitHub…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Claude Code용 mods 빌드: 모든 요청을 hook하고, 모든 응답을 수정하며, /model…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Claude Code용 종합 statusline 대시보드 — 세션 정보, quota bars, 에이전트 추적기, MCP 상태, 메시지 기록 등.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: Claude Code 세션의 탄소 발자국 추적.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - awesomejun이 만든 Claude Code용 미적인 statusline.
- [amirfish1/claude-command-center](https://github.com/amirfish1/claude-command-center) - One local board for Claude Code, Codex, Cursor and 5 more coding agents.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - 공개 Claude Code 스킬 및 모드.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Claude Code용 Skills, mods, subagents, hooks, slash commands 및 guides — 에이전트가…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 법적으로 무료인 LLM APIs 및 코딩 에이전트 — 주 2회 자동 업데이트 및 프로브 검증.
- [398894496-arch/DSH-KRouter](https://github.com/398894496-arch/DSH-KRouter) - Second brain for coding agents. Seal the day, distill into Obsidian, merge…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Claude Code 세션용 터미널 상태 표시줄.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ 팔로우하는 대회(World Cup, Premier League, LALIGA, Champions League 및 11개 더)의 실시간 축구…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Local control plane for Claude Code on Windows and macOS: switch LLM gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - 코딩 에이전트를 키보드 펌웨어 전문가로 바꾸는 Agent Skill입니다.
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - ~/.claude 내부에서 버전 관리되는 개인 Claude Code 구성 — 에이전트, 스킬, 훅, 설정, statusline.
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Claude Code 안에서 기도 시간, 히즈리 날짜, 아즈카르, 오늘의 아야, 순나 단식, 라마단, 주무아 및 타스비흐를 제공하며, 하나의…
- [livlign/ccbit](https://github.com/livlign/ccbit) - Claude Code용 세션 인식 상태 표시줄입니다. kaomoji 얼굴이 대화 기록을 읽고 세션 전반의 상태를 설명합니다.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — 연구 주제, 추적 가능한 지식 카드, 재사용 가능한 AI 토론을 위한 DeepSeek…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - .NET DDD/Clean Architecture를 위한 휴대용 Claude Code 툴킷: 엄격한 TDD 에이전트, 계층 규칙, hooks…
- [saadnvd1/agent-os](https://github.com/saadnvd1/agent-os) - Mobile-first web UI for managing AI coding sessions.
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Claude Code, pi 및 DeepSeek Harness용 플러그인 모음: 상태 표시줄 HUD, 작업 진행률 표시줄, Tailscale…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - 이식 가능한 Claude Code 전역 구성: 사용자 지정 스킬, PreToolUse 후크 및 사용자 지정 상태 표시줄.
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - 매일 사용하는 Claude Code 플러그인: 어떤 컴퓨터에서든 작동하도록 정리한 skills와 mods입니다.
- [34823/tg-pane](https://github.com/34823/tg-pane) - Claude Code 안의 Telegram: 패널에서 채팅과 채널을 읽고, 읽지 않은 게시물의 AI 요약을 받습니다.
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) 브리지, 자체 개발(fork 아님): 스트리밍 답장 카드 / 하나의 인스턴스에 여러 bot.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Hytale Mods를 지원하기 위한 Claude Code 플러그인 및 스킬 마켓플레이스.
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Claude Code를 위한 토큰 거버넌스: 상위 모델이 지시하고, 실행은 충분히 적합한 가장 저렴한 수단으로 전달됩니다.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Windows Terminal 및 tmux에서 Claude Code를 위한 분할 패널 뷰어: subagents, 실시간 git diffs…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Claude Code를 위한 실시간 워크플로 단계 상태 표시줄(Plan → Exec → Verify → Done)이며 모델이 자동으로…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Claude Desktop의 Code 탭을 위한 비공식 모드 — usage-pet: Clawd와 애니메이션 픽셀 펫이 있는 사용량 밴드.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Claude Code Awesome Media 모드용 저장소.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Claude Code 및 Codex 토큰 비용 절감: 조회와 테스트 실행을 더 저렴한 모델로 라우팅하고, 문서를 간결한 Markdown으로…
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Simple and useful status line setup for Claude Code.
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
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - herdr에서 Claude Code를 위한 정의 가능한 소프트웨어 팩토리: xstate 스테이션 그래프, manager 모드, rigs…
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Claude Code용 사용자 지정 상태 표시줄 — 사용률, 컨텍스트 크기, 비용 및 타이머가 표시되는 컨텍스트 막대.
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - A clean, informative status line for Claude Code — shows project, git status…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - baloo가 포함된 Claude Code 플러그인 마켓플레이스: 스킬, 프로젝트의 결정 사항·지침·검사를 기준으로 변경 사항을 검증하는…
- [ChristianVerghis/claude-statusline](https://github.com/ChristianVerghis/claude-statusline) - Claude Code 상태 표시줄: 컨텍스트 사용량, 5시간/7일 할당량 막대, 재설정 시간, git 브랜치.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - 전문가급 Claude Code statusline: 세션 시간, ECB FX를 적용한 다중 통화 비용, MTok당 요금 및 지출 한도를…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Claude Code용 구독 인식 상태 표시줄.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Claude Code용 풍부한 터미널 상태 줄 — Bun + TypeScript, 런타임 의존성 없음.
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Claude Code용 2행 상태 표시줄: 컨텍스트, 페이스 마커가 포함된 속도 제한, 비용 및 캐시.
- [eddywong888/claude-castle-mod](https://github.com/eddywong888/claude-castle-mod) - A Castlevania-style usage HUD mod for Claude Code: context blood meter…
- [ejklock/claude-mermaid-render](https://github.com/ejklock/claude-mermaid-render) - 트랜스크립트에 Mermaid 다이어그램을 아름답게 렌더링하는 Claude Code 플러그인: 모든 터미널에서 색상이 적용된 Unicode…
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Claude Code용 도구, 스킬 및 에이전트 — 모델, 브랜치, PR, 컨텍스트 크기, 프롬프트 캐시 잔여 시간 및 비용을 표시하는 상태…
- [Furkan-rgb/claude-config](https://github.com/Furkan-rgb/claude-config) - Claude Code 전역 설정: 에이전트, 스킬, 모드, 설정.
- [Guidin9/claude-usage-footer](https://github.com/Guidin9/claude-usage-footer) - Claude Code 플러그인: 푸터 오른쪽 아래에서 남은 Claude 5시간 사용 한도를 항상 확인 — 더 이상 /usage를 사용할 필요…
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Claude Code의 실제 DeepSeek API 지출: DeepSeek 피크/오프피크 요금으로 세션 트랜스크립트의 가격을 다시 계산하고…
- [HiramAA/claude-desktop-mods](https://github.com/HiramAA/claude-desktop-mods) - Mods para Claude Code y Claude Desktop en Windows con WSL: Docker y rendimiento…
- [ihororlovskyi/claude-statusline](https://github.com/ihororlovskyi/claude-statusline) - 에이전트 패널 행이 있는 Claude Code 상태 표시줄.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Claude의 할 일을 Fizzy.do에 동기화하여 팀이 실시간으로 확인할 수 있게 하고, 작업을 영구 카드로 전환해 협업을 강화하고 진행…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - 컨텍스트, git 상태, 비용 및 속도 제한을 보여주는 상세한 색상 코드 상태 표시줄을 Claude Code에 표시합니다.
- [konnichiwab/claude-code-config](https://github.com/konnichiwab/claude-code-config) - Claude Code 설정 메뉴, 상태 표시줄 및 config.
- [Larg0Winch/claude-label](https://github.com/Larg0Winch/claude-label) - Claude Code 상태 표시줄에서 창별 라벨을 편집할 수 있습니다. Pacto(pacto.global) 제공.
- [ldk00315-jpg/claude-code-voice-mod](https://github.com/ldk00315-jpg/claude-code-voice-mod) - codex app-server realtime(ChatGPT 로그인)을 사용하는 모드 + helper로 Windows에서 음성으로 Claude…
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - 컨텍스트 창, API 사용량 추적, git 상태 및 세션 비용을 표시하는 사용자 지정 Claude Code 상태 표시줄.
- [melderan/claude-statusline-rust](https://github.com/melderan/claude-statusline-rust) - 빠른 Rust 상태줄(Claude Code용, 훅 JSON을 읽고 지표를 SQLite에 기록).
- [mgstegmaier/claude-plugins](https://github.com/mgstegmaier/claude-plugins) - 직접 만든, 케이지 프리 claude 플러그인, 스킬, 모드 등.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code 환경 설치 프로그램: skills, statusline, hooks, permissions 및 선택적…
- [oshnilia/claude-plugins](https://github.com/oshnilia/claude-plugins) - Claude이(가) 수행하는 작업을 이해하기 위한 Claude Code 플러그인 및 모드: 읽기 쉬운 답변 형식과 실시간 세션…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - 활성 작업, 대기 중인 권한 및 경과 시간에 대한 실시간 표시기로 macOS 메뉴 막대에서 Claude Code 상태를 모니터링합니다.
- [pirncedark/afu-claude-statusline](https://github.com/pirncedark/afu-claude-statusline) - Claude Code용 다채로운 다중 행 상태 표시줄(할당량 막대, 컨텍스트, 서브에이전트 패널).
- [rainyfei/claude-statusline-win](https://github.com/rainyfei/claude-statusline-win) - Windows용 Claude Code 상태줄(PowerShell): 사용량 막대, 속도 경고가 포함된 5시간/7일 재설정 카운트다운, 자동 줄…
- [realkewal/claude-kit](https://github.com/realkewal/claude-kit) - Claude Code 플러그인. Usage Bars는 세 개의 정렬된 막대로 컨텍스트 창 사용량과 함께 세션 및 주간 속도 제한을 보여줍니다.
- [roy651/cc-plugins](https://github.com/roy651/cc-plugins) - Claude Code용 Bearings and Glossary 모드.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - 사용자 지정 Claude Code 상태 표시줄(업스트림: kamranahmedse/claude-statusline).
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - 공유 컴포넌트 키트, 플레이그라운드 및 Storybook이 포함된 Claude Code 설정 및 모드.
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Claude Code를 위한 작은 대시보드: 컨텍스트 %, 캐시 카운트다운, 5시간 및 주간 사용량, 새 채팅으로 이동하는 원클릭…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - 포터블 Claude Code 설정: CLAUDE.md, settings, statusline, skills.
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Claude Code용 모드: 컨텍스트, 제한, 비용, 프롬프트 캐시 상태 및 하위 에이전트를 보여주는 프롬프트 위 패널입니다.
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - 터미널용 경량 종속성 없는 상태줄 대시보드로 Claude Code 컨텍스트 사용량, 세션 비용 및 속도 제한 재설정을 추적합니다.
- [UtakataKyosui/utakata-cc-mod](https://github.com/UtakataKyosui/utakata-cc-mod) - Claude Code용 모드 모음(goal-orchestrator: /goal을 작업으로 분해하여 SubAgent에 위임).
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Claude Code용 실시간 비용 추적 및 세션 모니터링 상태 줄.
- [xinvxueyuan/cordis-plugin-secret](https://github.com/xinvxueyuan/cordis-plugin-secret) - Cordis / DeepSeek Harness 플러그인 — 에이전트는 인라인 대화 카드에서 사람에게 비밀을 요청하며, 값 자체는 절대 받지…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - 컨텍스트 깊이, 세션 간 속도 제한, 저장소별 git 상태 및 worktree를 표시하는 3행 Claude Code 상태 표시줄.
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Context Rot Detector 2026 - Claude Code 에이전트를 위한 사전 대응형 AI 메모리 및 속도 제한 모니터.
- [zerofaultlabs/claude-statusline](https://github.com/zerofaultlabs/claude-statusline) - Claude Code 상태줄: 컨텍스트 사용량, 속도 제한, 비용 및 캐시 적중을 한눈에 표시.
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Claude Code 훅, 서브에이전트 및 상태줄: 유형별 오픈 소스 컬렉션과 도구, 각각 보안 등급 제공. English / 中文.
- [zoo3323/claude-statusline](https://github.com/zoo3323/claude-statusline) - Claude Code 상태 표시줄 — 유휴 상태에서도 계속 실시간으로 유지되는 Claude/Codex 사용량 게이지, 컨텍스트 %, 진행 중인…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Claude Code 상태 표시줄을 위한 시각적 빌더입니다. 브라우저에서 터미널 하단의 막대를 디자인한 다음 명령 하나를 붙여 넣어 설치하세요.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - 실시간 토큰 사용량과 예상 에너지 소비량을 표시하는 Claude Code 상태 표시줄.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - 함수 후크를 기반으로 창, 밴드 및 버디를 구축한 Claude Code용 Mods.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Claude Code 세션 간에 작업 전달. 리포지토리를 담당하는 세션에 변경 사항을 넘김.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Fablab용 모듈식 크로스 플랫폼 도구인 MODS를 제어하기 위한 MCP 서버의 기능입니다.
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - 로컬 LLM을(를) 사용하여 CK3 Mods를 번역하기 위한 Codex 및 Claude Code 스킬.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Claude Code를 위한 오픈 소스 모드 및 기타 확장 기능.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: Claude Code에 반복해서 요청하는 작업을 찾아 모드로 변환. 예제 모드 8개와 가상 사무실도 포함.

</details>

<a id="dsh-cordis"></a>

## DSH 및 Cordis 플러그인 생태계

DeepSeek Harness와 Cordis는 서로 다른 방향에서 같은 지점에 도달합니다. 이들에게 플러그인은 모드 메커니즘이므로, 그쪽의 플러그인은 이곳의 모드에 해당합니다.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74290 · TypeScript · 👁️ observed · 0 天</summary>

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
| 스타        | **74290**  |
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
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100412 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **100412** |
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
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐81684 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **81684**  |
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
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐73982 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **73982**  |
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
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35761 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **35761**  |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30367 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **30367**  |
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
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25472 · Python · 🔎 inferred · 18 天</summary>

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
| 스타        | **25472**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9113 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

시공간 조합 가능성을 위한 메타 프레임워크

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **9113**   |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-09 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8596 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **8596**   |
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
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4268 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **4268**   |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

The World's First Virtual Terminal for AI Agents

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
| 최초 등록   | 2026-10-11 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3409 · Python · 🔎 inferred · 0 天</summary>

##### 📝 요약

本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | Python                                                                          |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **3409**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AdamPlatin123/dsh-plugin-radar">AdamPlatin123/dsh-plugin-radar</a></b> · ⭐1462 · Python · 🔎 inferred · 0 天</summary>

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
| 스타        | **1462**   |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-plugins` · `continuous-validation` · `deepseek-harness` · `dsh` · `dsh-plugin` · `ecosystem-radar` · `plugin-registry`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/adamplatin123--dsh-plugin-radar/fb6ad7eb8891212c.jpg" width="100%" alt="AdamPlatin123/dsh-plugin-radar screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1168 · Go · 🔎 inferred · 0 天</summary>

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
| 스타        | **1168**   |
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

가장 종합적인 DeepSeek Harness 플러그인 마켓입니다 — 매일 갱신되며, 인터넷 전반에서 수집하고 게시 전에 검토합니다.

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
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `agent` · `deepseek` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/livxue--dsh-plugin-shop/0cd59c71bcc6f86e.png" width="100%" alt="LivXue/dsh-plugin-shop screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐702 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **702**    |
| 마지막 푸시 | 2026-10-10 |
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

Your Intelligence, Orchestrated. Every builder. Every team. Every agent. For Everyone.

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
<summary>🧵 <b><a href="https://github.com/xing-shuyin/pi-web-ui">xing-shuyin/pi-web-ui</a></b> · ⭐282 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Just open your browser — get all your work done.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **282**    |
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

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

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
<summary>🧵 <b><a href="https://github.com/cv-superding/dsh-deepseek-web-login">cv-superding/dsh-deepseek-web-login</a></b> · ⭐248 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

비공식 DSH (DeepSeek Harness) 플러그인: chat.deepseek.com 웹 모델을 LLM provider로 사용합니다. 브라우저 로그인 캡처, PoW 해결, SSE 스트리밍, 프롬프트 기반 도구 호출을 지원합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **248**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-09 |

🏷 `browser-automation` · `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `dsh` · `llm-provider`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cv-superding--dsh-deepseek-web-login/b95392c45786ce03.png" width="100%" alt="cv-superding/dsh-deepseek-web-login screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-trading">zhu1090093659/dsh-trading</a></b> · ⭐238 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

Agent-native trading terminal built on DeepSeek Harness. Crypto, US, CN and HK in one three-column GUI, 19+ hot-swappable connectors, dry-run by default with human approval on every live order. BYOK, no data redistribution.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **238**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `agent-native` · `ai-agent` · `cryptocurrency` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop` · `trading-terminal`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhu1090093659/dsh-trading/main/docs/banners/banner-en.jpg" width="100%" alt="zhu1090093659/dsh-trading screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

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
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>애니메이션 녹화</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/2BingLing/dsh-market">2BingLing/dsh-market</a></b> · ⭐138 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek Harness 插件市场 · 持续收录 6000+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 6000+ plugins, Chinese search, 5-dim scoring, one-click install.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **138**    |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-11 |

🏷 `deepseek-harness` · `deepseek-harness-plugin` · `deepseek-harness-plugins` · `dsh` · `dsh-bundle` · `dsh-market` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/2BingLing/dsh-market/master/assets/readme/banner.webp" width="100%" alt="2BingLing/dsh-market screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

<sub>재배포에 적합한 라이선스가 명시되지 않아 업스트림 저장소에서 에셋을 핫링크했습니다.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mexiaosqwq/dsh-web-mobile">mexiaosqwq/dsh-web-mobile</a></b> · ⭐130 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **130**    |
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
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐127 · TypeScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **127**    |
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
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐119 · Python · 🔎 inferred · 0 天</summary>

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
| 스타        | **119**    |
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
<summary>🧵 <b><a href="https://github.com/dickpy/dsh-imagegen">dickpy/dsh-imagegen</a></b> · ⭐103 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DSH (DeepSeek Harness) Web GUI AI image generation plugin: text-to-image & image-to-image via OpenAI-compatible endpoints (gpt-image-2), with shared cross-device history.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **103**    |
| 마지막 푸시 | 2026-10-11 |
| 최초 등록   | 2026-10-11 |

🏷 `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dickpy--dsh-imagegen/5859c3cebcc07298.png" width="100%" alt="dickpy/dsh-imagegen screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EricWang1358/dsh-web-studyhub">EricWang1358/dsh-web-studyhub</a></b> · ⭐85 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

StudyHub: 자신의 자료를 문제와 간격 반복 학습으로 바꿔 주는 DeepSeek Harness (DSH) 플러그인 · 자신의 자료를 문제와 간격 반복 학습으로 바꾸는 DSH 학습 플러그인

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | JavaScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **85**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `dsh` · `dsh-plugin` · `education` · `flashcards` · `spaced-repetition` · `study`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ericwang1358--dsh-web-studyhub/1e4a97948bc59f9d.jpg" width="100%" alt="EricWang1358/dsh-web-studyhub screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/mrRisega/dsh-remote">mrRisega/dsh-remote</a></b> · ⭐75 · JavaScript · 🔎 inferred · 0 天</summary>

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
| 스타        | **75**     |
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
<summary>🧵 <b><a href="https://github.com/Sev7eEn7/dsh-sieve">Sev7eEn7/dsh-sieve</a></b> · ⭐73 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

dsh-sieve: DeepSeek Harness (DSH)용 context engineering 및 token 최적화 플러그인 — 도구 출력 필터링, 컨텍스트 정리, 점진적 스킬 공개를 지원합니다. 오프라인 재생에서 payload를 36% 줄입니다. DSH 컨텍스트 관리 및 token 최적화 절약 플러그인입니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **73**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `agent-tools` · `ai-agent` · `ai-coding` · `coding-agent` · `context-engineering` · `context-management` · `context-pruning` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sev7een7--dsh-sieve/eab2b3c8b1588637.webp" width="100%" alt="Sev7eEn7/dsh-sieve screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ZASENJC/dsh-plugins-store">ZASENJC/dsh-plugins-store</a></b> · ⭐69 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

DeepSeek-Harness 커뮤니티 플러그인을 자동으로 분류, 수록 및 검증하는 마켓. DeepSeek-Harness 커뮤니티 플러그인 마켓플레이스를 자동으로 분류, 선별 및 검증합니다.

##### 📌 기본 정보

| 필드     | 값                                                                              |
| -------- | ------------------------------------------------------------------------------- |
| 카테고리 | `DSH 및 Cordis 플러그인 생태계`                                                 |
| 근거     | `모드, 플러그인 또는 훅이라고 선언했지만 모드 표면에 관한 구체적인 내용은 없음` |
| 언어     | TypeScript                                                                      |

##### 📊 데이터

| 지표        | 값         |
| ----------- | ---------- |
| 스타        | **69**     |
| 마지막 푸시 | 2026-10-10 |
| 최초 등록   | 2026-10-10 |

🏷 `agent-tools` · `awesome-list` · `community-project` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 이미지</th><th align="center" width="50%">🎬 동영상</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zasenjc--dsh-plugins-store/e83b24d43eca5912.png" width="100%" alt="ZASENJC/dsh-plugins-store screenshot"></td>
<td align="center" valign="top"><sub>게시된 미디어 없음</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐57 · HTML · 🔎 inferred · 0 天</summary>

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
| 스타        | **57**     |
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
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐53 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 요약

面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体。纯本地、零模型调用、零网络。  Task-aware workspace context retrieval and lifecycle tracking for AI coding agents. Find, organize, and track the workspace context most relevant to the task at hand — locally, deterministically, zero model calls, zero network.

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
<summary><b>이 카테고리의 더 많은 항목</b> <sub>· 77</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - AI 코딩 에이전트를 위한 실행 전 보호 장치입니다. 도구 호출이 실행되기 전에 파괴적인 Git 및 파일 시스템 명령과 민감한 파일에…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30초 만에 나에게 정말 적합한 DeepSeek Harness 플러그인을 찾으세요.
- [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) - A curated list of plugins, skills, MCP servers, patch/profile layers…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH 플러그인 마켓 / DSH Plugin Marketplace: DeepSeek Harness Web GUI에서 GitHub…
- [arcships/rutis](https://github.com/arcships/rutis) - 계속 실행되는 프로그램을 위한 플러그인 런타임 — 프로세스와 머신 전반의 Rust 코어, TypeScript 및 Python 플러그인.
- [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) - 🐳 DeepSeek Harness 플러그인 커뮤니티 집계 — dsh-plugin 생태계 자동 동기화 · 엄선 디렉터리 · 4시간마다 자동 관리…
- [adamkhalile/luau-docs-oracle](https://github.com/adamkhalile/luau-docs-oracle) - 최고의 Roblox Luau 버그 검사기 및 API 검증기 2026 DevForum MCP 도구.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - DeepSeek Harness (DSH) 플러그인 엄선 디렉터리 — MCP / Skill / TUI / 멀티 Agent / 컨텍스트 메모리 /…
- [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) - 【求⭐】🐋DSH Web UI…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) - DeepSeek harness용 Zotero toolkit입니다. Zotero 라이브러리를 에이전트를 위한 증거 저장소로 바꿔 줍니다.
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Windows의 모든 에이전트 모드를 위한 DSH 플러그인: Git Bash 셸(pwsh 실행기 대체).
- [jingyi0605/Codingns4DSH](https://github.com/jingyi0605/Codingns4DSH) - 把外部 Agent CLI、持久终端、工作区调试和远程访问，装进 DSH 原生界面.
- [ZhangFengshun/dsh-remote-ssh](https://github.com/ZhangFengshun/dsh-remote-ssh) - DSH web plugin: VSCode Remote-SSH-like remote development.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: DeepSeek Harness（DSH）기반 멀티 플랫폼 그룹 채팅 지능형 에이전트 시스템｜DSH 기반 멀티 플랫폼 그룹 채팅…
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [HaoyueQin/dsh-usage-statistics-panel](https://github.com/HaoyueQin/dsh-usage-statistics-panel) - DSH web plugin: per-day token usage statistics with a GitHub-style activity…
- [JustGenius-s/DSH-Desktop](https://github.com/JustGenius-s/DSH-Desktop) - DSH-Desktop.
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 중국어 웹소설 작가를 위한 로컬 집필 워크벤치(도구 19개): 집필 전에 이전 장의 연결 부분/개요/인물 카드/회수할 복선/용어 규칙을 모두…
- [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) - Appearance customization plugin for DeepSeek Harness: theme color palette…
- [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) - DSH 플러그인 생태계 투명 순위 및 추천: 매일 dsh-plugin 토픽 자동 수집 + 공개 점수 모델 + 순위/추천 플러그인 및 정적 사이트.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - 커뮤니티가 엄선한 DeepSeek Harness (dsh) 플러그인, 도구, 스킬 및 학습 리소스입니다.
- [Wenaixi/dsh-superpower](https://github.com/Wenaixi/dsh-superpower) - DeepSeek Harness 플러그인: 15개의 obra/superpowers 엔지니어링 스킬, 이중 언어 설명, 스킬별 토글 |…
- [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) - DeepSeek Harness Web용 MCP 서버 관리 UI — 플로팅 패널, JSON 가져오기 및 프로필 기반 영속성을 제공합니다.
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - 검증된 DeepSeek Harness 플러그인 마켓플레이스 및 자동 레지스트리.
- [liustack/pptwise](https://github.com/liustack/pptwise) - HTML이 아닌 진짜 PowerPoint입니다. AI에게 다룰 내용을 말하면 pptwise가 자신의 컴퓨터에서 편집 가능한 덱을 만듭니다.
- [Wenaixi/dsh-ponytail](https://github.com/Wenaixi/dsh-ponytail) - DeepSeek Harness 플러그인: DietrichGebert/ponytail lazy senior 모드 및 7단계 사다리 포트, 이중…
- [daha1216/dsh-plugin-collection](https://github.com/daha1216/dsh-plugin-collection) - DeepSeek Harness（DSH）第三方插件精选目录：一键安装，条目均指向插件作者原仓库.
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - 스팸이 필터링된 DeepSeek Harness(dsh) 플러그인, 번들 및 스킬의 오픈 데이터 레지스트리입니다.
- [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) - A curated list of plugins for DeepSeek Harness (dsh) — 精选 DeepSeek Harness 插件列表.
- [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) - DSH 手机/外网远程访问插件：免配置公网隧道 + 局域网 HTTPS 直连 + 自定义公网链接/端口 + 微信机器人.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 로컬 컴퓨터의 WorkBuddy 데스크톱 버전에 로그인된 모델(DeepSeek / GLM / Kimi / MiniMax 등)을 로컬…
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) - DeepSeek Harness 플러그인을 위한 격리된 설치 및 스모크 테스트 실행기: 저장소 또는 npm 패키지를 임시 DSH_HOME…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DeepSeek Harness 플러그인을 위한 상시 호환성 테스트: 정확한 릴리스, 격리된 러너, 수정 가능한 업스트림 이슈.
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - DeepSeekBot: DeepSeek Harness (DSH) 기반으로 구축된 오픈 소스 GrokBot 대안.
- [klarkxy/dsh-plugins](https://github.com/klarkxy/dsh-plugins) - Small, independently installable plugins for DeepSeek Harness.
- [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) - DSH Web UI 会话进度插件：输入框停靠区常驻进度条.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - DeepSeek Harness 플러그인을 위한 X-ray: 선언된 기능과 실제 동작을 비교합니다. 레지스트리 + 정적 스캐너 + 배지.
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - 프로젝트 문서와 장기 메모리를 전용 Obsidian vault에 일반 Markdown으로 보관하는 DeepSeek Harness 호스트…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 플러그인 마켓 — DeepSeek Harness 설정에서 커뮤니티 플러그인을 한 번에 설치하고, 공개 디렉터리 사이트.
- [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) - 에이전트 우선 DeepSeek Harness 플러그인 인텔리전스: 기존 플러그인을 검증하고, 누락된 기능을 식별하며, 빌드 준비가 완료된…
- [omdsh-dev/dsh-minigames](https://github.com/omdsh-dev/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) - DSH를 위한 로컬 우선 음성 대화입니다. 선택적 외부 공급자와 함께 음성 인식 및 음성 합성을 자체 컴퓨터에서 실행합니다.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH 플러그인: 네이티브 dsh-better-sidebar 탭으로 제공되는 IDE급 Git 도구 창 — 브랜치 트리, 커밋 그래프, 변경…
- [KannaKuron/dsh-ptc-cordis-preset](https://github.com/KannaKuron/dsh-ptc-cordis-preset) - PTC 모드 기반의 창작 모드: DSH 플러그인이 Code Mode 도구 오케스트레이션과 자기 참조 Cordis 도구 및 preset 창작…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness(DSH) 플러그인 리더보드 및 디렉터리｜DeepSeek Harness(DSH) 플러그인 순위 / 플러그인…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - 다중 폴더 workspace: DSH(DeepSeek Harness)의 Agent가 기본 디렉터리뿐 아니라 추가한 다른 폴더도 동시에 읽고 쓸…
- [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) - DeepSeek Harness용 엔지니어링 워크플로 플러그인: 작업 단계, 검증 기록, 커밋 확인, 스킬 및 규칙 관리.
- [liceses/dsh-cosplay](https://github.com/liceses/dsh-cosplay) - DSH 롤플레잉 플러그인: 캐릭터 카드(시스템 프롬프트 주입 + 사용자 프롬프트 재작성), 공유 가능한 단일 파일 카드 패키지, 원본 UI를…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - 엄선된 목록과 매니페스트로 검증된 GitHub 검색 기능을 제공하는 검색 가능한 DeepSeek Harness 플러그인 레지스트리입니다.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - DeepSeek Harness(dsh) 플러그인을 위한 종속성 없는 검증 표준 — 정적 구조 게이트(R), cordis 계약 검사(K)…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness 플러그인 마켓 — dsh-plugin topic 플러그인 탐색, 검색 및 설치.
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - DeepSeek Harness의 OpenCode — OpenCode Zen + Go 무료 티어 모델을 계속 작동하게 하는 DSH 플러그인…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — DeepSeek Harness를 위한 서드파티 플러그인 마켓플레이스 및 보호된 수명 주기 관리자.
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx는 사람을 중심으로 설계된 확장 가능한 데스크톱 작업 공간입니다.
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon: DeepSeek Harness 웹 서버(dsh web)를 자동 시작, 자가 복구 백그라운드 서비스.
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 입력 경험 플러그인: 보내기/줄바꿈 키 전환, 우클릭 메뉴, 패널 스크롤 및 크기 기억, OpenCode 요청 헤더 자동 주입.
- [HarcoChen/dsh-intellij-integration](https://github.com/HarcoChen/dsh-intellij-integration) - DeepSeek Harness (DSH) for JetBrains IDEs — AI coding with native diffs, tool…
- [InterPSS-Project/ipss-agent](https://github.com/InterPSS-Project/ipss-agent) - InterPSS Agentic Power System Simulation Agent for AC load flow, DC-based…
- [lhh010/dsh-input-history](https://github.com/lhh010/dsh-input-history) - DSH Web 输入历史插件：Ctrl+Up / Ctrl+Down 像终端一样召回与切换已发送消息，零核心改动.
- [momasiku/dsh-pilot](https://github.com/momasiku/dsh-pilot) - Desktop automation for DeepSeek Harness: hands and eyes on the whole Windows…
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - DeepSeek Harness 데스크톱 버전에 &quot;네트워크 대역 제한 + 선택적 숫자 비밀번호&quot;가 있는 원격 액세스 진입점을 제공합니다.
- [omdsh-dev/dsh-file-trace](https://github.com/omdsh-dev/dsh-file-trace) - DSH Web UI 文件追踪插件：记录并查看模型读取/写入/编辑的每个文件，带行号内容、终端风逐行 diff（红删绿增蓝改）与 hunk 上下文折叠；支持…
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - DeepSeek Harness(DSH) 웹 플러그인: 시장 대시보드 사이드바 탭을 모니터링합니다 — 마우스를 올리면 장중 차트가 표시되는…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - DeepSeek Harness 플러그인: Windows 샌드박스 ACL 프로비저닝 실패.
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - 출처가 표시되지 않은 빈 모델 시도를 재시도 가능하게 만듭니다. 이를 판별할 수 있는 하나의 접점.
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - DeepSeek Harness agent preset: Codex and Claude Code as delegation subagents…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Verus-verified 라이프사이클 커널과 Cordis 호환성 어댑터를 갖춘 Rust 플러그인 런타임입니다.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 플러그인 집계 사이트: 전체 DeepSeek Harness 플러그인 통합 검색, 다중 소스 자동 중복 제거 및 분류, 매시간 갱신 |…
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 플러그인 스토어 - GitHub topic:dsh-plugin 기반 자동 발견 및 매시간 정기 동기화.

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 2 天</summary>

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
| TypeScript | 402  | `anthropics/claude-code`, `anthropics/claude-code-action`, `PerryLink/dsh-mcp-panel`                          |
| JavaScript | 85   | `Enc-hanted/dsh-pulse`, `MIHassan3/DSH-Launcher`, `karanb192/awesome-claude-code-mods`                        |
| Python     | 45   | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 29   | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 16   | `HeyCubit/effortless`, `awss1i/assay`, `darrell-tw/darrelltw-mods`                                            |
| Go         | 7    | `cephalofoil/kitt`, `kylesnowschwartz/tail-claude-hud`, `livlign/ccbit`                                       |
| Rust       | 5    | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `melderan/claude-statusline-rust`            |
| PowerShell | 2    | `rainyfei/claude-statusline-win`, `daha1216/dsh-plugin-collection`                                            |
| Swift      | 2    | `bhargava-gumpula/claude-mods`, `peaceinitiativemenhadenoil263/claude-status-bar`                             |
| C          | 1    | `reporails/arcade`                                                                                            |
| C#         | 1    | `sakanamaru/dsh-minato`                                                                                       |
| MDX        | 1    | `jkf87/mod-guide`                                                                                             |

<sub>언어를 명시한 항목만 집계됩니다. 문서 및 토론 항목은 이 표에서 제외됩니다.</sub>

## 기여

수정 사항을 제보해 주시면 이 목록을 가장 빠르게 개선할 수 있습니다. 항목이 잘못 분류되었거나, 등급이 잘못 매겨졌거나, 이름 충돌로 인해 프로젝트가 잘못 제외되었다면 이슈 또는 풀 리퀘스트를 열어 주세요. 마지막 유형은 자동 필터가 가장 자주 잘못 판단하는 경우입니다.

---

<sub>독립적인 커뮤니티 프로젝트입니다. Anthropic와(과) 제휴, 승인 또는 검토를 거치지 않았습니다. Claude Code, Claude 및 Anthropic은(는) Anthropic의 상표입니다. 제품 동작은 예고 없이 변경될 수 있으므로, 중요한 내용은 공식 문서에서 확인하세요. 에셋은 원 프로젝트의 자산으로 남으며, 라이선스가 허용하는 경우에만 재현됩니다.</sub>

<sub>마지막 업데이트 · 2026-10-11T10:13:26+08:00</sub>
