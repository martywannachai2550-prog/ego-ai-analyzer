def generate_plan(type_name, language="EN"):

    if type_name == "Independent Explorer":

        if language == "TH":
            strategy = "การเรียนรู้ผ่านการทำโครงงาน"
            schedule = [
                "ดูบทเรียนหรือวิดีโอสอน",
                "สร้างโครงงานขนาดเล็ก",
                "แก้โจทย์หรือความท้าทาย",
                "ปรับปรุงโครงงานของคุณ",
                "เผยแพร่ผลงานของคุณ"
            ]
        else:
            strategy = "Project-based learning"
            schedule = [
                "Watch tutorial",
                "Build mini project",
                "Solve challenge problem",
                "Improve your project",
                "Publish your work"
            ]

    elif type_name == "Focused Achiever":

        if language == "TH":
            strategy = "การฝึกฝนอย่างเป็นระบบ"
            schedule = [
                "ศึกษาเนื้อหาทฤษฎี",
                "จดบันทึก",
                "ฝึกทำแบบฝึกหัด",
                "แก้โจทย์ระดับสูง",
                "ทำแบบทดสอบสั้น ๆ"
            ]
        else:
            strategy = "Structured training"
            schedule = [
                "Study theory",
                "Take notes",
                "Practice exercises",
                "Solve advanced problems",
                "Take a mini test"
            ]

    elif type_name == "Adaptive Collaborator":

        if language == "TH":
            strategy = "การเรียนรู้ผ่านการสำรวจ"
            schedule = [
                "สำรวจแนวคิดใหม่",
                "เชื่อมโยงแนวคิดต่าง ๆ",
                "สร้างสิ่งใหม่ในแบบของคุณ",
                "ทดลองแนวทางที่แตกต่าง",
                "แบ่งปันแนวคิดของคุณ"
            ]
        else:
            strategy = "Exploratory learning"
            schedule = [
                "Explore new concept",
                "Connect ideas",
                "Create something original",
                "Experiment with variation",
                "Share your idea"
            ]

    else:

        if language == "TH":
            strategy = "การเรียนรู้เชิงวิเคราะห์อย่างลึกซึ้ง"
            schedule = [
                "ศึกษาเนื้อหาเชิงทฤษฎีอย่างละเอียด",
                "วิเคราะห์ระบบ",
                "อ่านกรณีศึกษา",
                "นำความรู้ไปใช้กับโครงงาน",
                "ประเมินผลลัพธ์"
            ]
        else:
            strategy = "Deep analytical learning"
            schedule = [
                "Deep theory study",
                "Analyze system",
                "Read case studies",
                "Apply to project",
                "Evaluate results"
            ]

    return strategy, schedule