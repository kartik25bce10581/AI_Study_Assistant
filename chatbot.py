def chatbot_response(q):
    q = q.lower()

    if "revise" in q:
        return "Use active recall + spaced repetition."
    elif "focus" in q:
        return "Study in distraction-free environment."
    elif "exam" in q:
        return "Practice PYQs + time management."
    elif "motivation" in q:
        return "Discipline > Motivation. Start small."
    elif "memory" in q:
        return "Use mnemonics + repeated revision."
    elif "practice" in q:
        return "Solve problems daily and analyze mistakes."
    elif "plan" in q:
        return "Make a realistic daily timetable."
    elif "stress" in q:
        return "Take breaks + deep breathing."
    elif "sleep" in q:
        return "7-8 hours sleep improves learning."
    elif "notes" in q:
        return "Keep notes short, clear, and visual."
    elif "backlog" in q:
        return "Divide backlog into small chunks."
    elif "consistency" in q:
        return "Daily small progress is key."
    else:
        return "Ask about study, revision, exams, focus, etc."
    
    