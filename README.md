# Checky Board 출제 원리 스킬

학습 목표와 근거에 맞는 문항을 만들고, 정답·해설·채점 기준·인지 부하·인쇄 결과를 함께 검토하는 공개 교육용 스킬입니다. 특정 프로그램에 연결하지 않아도 문항 초안과 자료에 적용할 수 있습니다.

**[스킬 본문](skills/checkyboard-authoring/SKILL.md)** · **[AGPL-3.0](LICENSE)** · 기준일: 2026-11-11

## 사용

`skills/checkyboard-authoring` 폴더를 Codex의 사용자 스킬 폴더에 복사합니다. 기본 위치는 `~/.codex/skills/checkyboard-authoring`입니다. 다른 에이전트에서도 본문과 필요한 참고 자료를 읽어 적용할 수 있습니다.

```text
$checkyboard-authoring 4학년 아이가 이 시험을 처음 푸는 입장에서
문항마다 찾을 정보와 할 판단, 남길 답을 짚어 줘.
번호순으로 부담이 쌓이는 구간과 다음 출제에 반영할 점도 알려 줘.
```

## 담은 원리

| 주제 | 자료 |
|---|---|
| 목표 → 자료 → 판단 → 정답 → 채점 증거 | [출제 원리와 전체 검수](skills/checkyboard-authoring/references/authoring-principles.md) |
| 문항별 첫 풀이와 시험 전체에서 부담이 쌓이는 구간 | [인지 부하와 첫 풀이 검수](skills/checkyboard-authoring/references/cognitive-load.md) |
| 모두/한 가지, 타당한 대안, 부분점수 | [정답과 채점](skills/checkyboard-authoring/references/review-and-rubrics.md) |
| 그림·표·답란·학생용과 교사용 출력 | [자료와 인쇄](skills/checkyboard-authoring/references/materials-and-print.md) |
| 과학·수학·수업 범위·견본 문체 | [과목별 범위](skills/checkyboard-authoring/references/subject-profiles.md) |
| 연구 근거와 적용 한계 | [출처와 범위](skills/checkyboard-authoring/references/sources-and-scope.md) |

상황은 확인할 수 있게 보여 주고, 학생이 해야 할 중심 판단은 남깁니다. 요구 사고(알기·적용·추론), 예상 난도, 인지 부하는 구분합니다. 실제 학생 측정 없이 효과·정답률·풀이 시간을 검증했다고 주장하지 않습니다.

## 합성 먹이그물 보조 도구

Python 3.10 이상, 표준 라이브러리만 사용합니다.

```bash
python skills/checkyboard-authoring/scripts/foodweb.py skills/checkyboard-authoring/references/synthetic-foodweb.json --remove plant-a
python -m unittest discover -s tests -v
```

생산자가 사라졌을 때 직접 먹이를 모두 잃는 동물과 남은 생산자에서 먹이 경로가 이어지는 동물을 구분합니다. 이 도구는 실제 생존이나 개체 수를 예측하지 않습니다. 예제는 실제 시험과 무관한 합성 그래프입니다.

## 공개 범위

공개 대상은 출제 원리·교육적 검토 절차·합성 예제입니다. 별도 프로그램의 연동 규격·구현·설치 안내, 실제 시험지·교과서 사진·학교 자료·학생 기록·개인 코멘트는 포함하지 않습니다. 이 저장소는 별도 프로그램의 소스나 이용 권한을 제공하지 않습니다.

[검증 범위](VALIDATION.md)와 [고지](NOTICE)를 참고하세요. 연구·교육과정 문서는 출처 링크로 안내하며 원문을 재배포하지 않습니다.
