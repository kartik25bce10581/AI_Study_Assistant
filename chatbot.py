def chatbot_response(q):
    q = q.lower()

    responses = {
        "revise": "Use active recall and spaced repetition.",
        "focus": "Study in a distraction-free environment.",
        "exam": "Practice previous year papers and manage time.",
        "motivation": "Start small. Discipline builds motivation.",
        "memory": "Use mnemonics and revise repeatedly.",
        "practice": "Solve questions daily and review mistakes.",
        "plan": "Make a realistic timetable and follow it.",
        "stress": "Take breaks and practice deep breathing.",
        "sleep": "Sleep 7–8 hours for better retention.",
        "notes": "Prepare short and visual notes.",
        "backlog": "Break backlog into small daily targets.",
        "consistency": "Small daily effort gives big results."
    }

    for key, value in responses.items():
        if key in q:
            return value

    return "Ask about study, revision, focus, exams, or planning."