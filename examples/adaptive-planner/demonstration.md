# Illustrative disruption

**This authored schedule demonstrates a constraint calculation. It is not a calendar export or a model-run result.**

Fictional Wednesday before the change: sleep 23:00–07:00; flexible study 09:00–11:00; laundry 11:30–12:30; travel to class 12:30–13:00; class 13:00–15:00. Free usable time includes 07:30–08:30 and 15:30–18:00. Study is two hours due Thursday; laundry takes one hour and is due Wednesday evening. The exam now occupies 09:00–11:00, with preparation/travel 08:30–09:00 and return travel 11:00–11:30.

| Time | Revised Wednesday | Reason |
| --- | --- | --- |
| 07:30–08:30 | Available | No need to fill every opening |
| 08:30–09:00 | Exam preparation/travel | Fixed transition |
| 09:00–11:00 | Exam | New fixed commitment |
| 11:00–11:30 | Return travel | Fixed transition |
| 11:30–12:30 | Laundry | Still fits before class travel |
| 12:30–13:00 | Travel to class | Preserved |
| 13:00–15:00 | Class | Preserved |
| 15:30–17:30 | Study, moved from 09:00 | Full two hours retained |
| 17:30–18:00 | Available slack | Flexibility retained |
| 23:00–07:00 | Sleep | Preserved |

If the two-hour study task instead had to finish before the 09:00 exam and only 07:30–08:30 remained, Wednesday would be one hour short. The planner should identify that shortfall, seek an earlier feasible slot if supplied, or ask the user to change scope or deadline. It should not make up Tuesday capacity or schedule 06:30 study during protected sleep.

Sample invocation: “Revise this week around a new Wednesday exam. Keep sleep, classes, and travel fixed; report anything that no longer fits.”

Limitations: This example does not establish optimized scheduling, live calendar synchronization, or the user's actual preferences. Conflicts involving missing travel times or uncertain durations remain assumptions until resolved.
