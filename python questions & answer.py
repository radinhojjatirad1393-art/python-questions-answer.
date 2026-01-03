import tkinter as tk
from tkinter import messagebox
import random

class PythonQuiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("بازی سوال و جواب پایتون")
        self.root.geometry("800x500")
        
        # متغیرهای بازی
        self.score = 0
        self.current_question = 0
        self.total_points = 0
        
        # 40 سوال با امتیازهای مختلف
        self.questions = [
            {"question": "برای چاپ در پایتون چه تابعی است؟", "answer": "print", "points": 1},
            {"question": "برای معکوس کردن شرط چه کلمه‌ای است؟", "answer": "not", "points": 1},
            {"question": "برای شرط 'و' چه کلمه‌ای است؟", "answer": "and", "points": 1},
            {"question": "برای جدا کردن مقادیر در print از چه چیزی استفاده می‌کنیم؟", "answer": ",", "points": 1},
            {"question": "اولویت کدام از or بیشتر است؟", "answer": "and", "points": 2},
            {"question": "برای تعریف تابع چه کلمه‌ای است؟", "answer": "def", "points": 2},
            {"question": "برای حلقه while چه کلمه‌ای است؟", "answer": "while", "points": 2},
            {"question": "برای مدیریت خطا چه بلوکی است؟", "answer": "try", "points": 2},
            {"question": "برای وارد کردن کتابخانه چه کلمه‌ای است؟", "answer": "import", "points": 1},
            {"question": "برای ایجاد کلاس چه کلمه‌ای است؟", "answer": "class", "points": 2},
            {"question": "برای ایجاد لیست خالی چه علامتی است؟", "answer": "[]", "points": 1},
            {"question": "تابع length چیست؟", "answer": "len", "points": 2},
            {"question": "برای خواندن ورودی کاربر چه تابعی است؟", "answer": "input", "points": 1},
            {"question": "کدام نوع داده تغییرناپذیر است؟", "answer": "tuple", "points": 3},
            {"question": "برای تبدیل رشته به عدد چه تابعی است؟", "answer": "int", "points": 2},
            {"question": "برای ایجاد دیکشنری خالی چه علامتی است؟", "answer": "{}", "points": 1},
            {"question": "برای برگشت از تابع چه کلمه‌ای است؟", "answer": "return", "points": 2},
            {"question": "برای حلقه روی دنباله چه کلمه‌ای است؟", "answer": "for", "points": 2},
            {"question": "برای کامنت چه علامتی است؟", "answer": "#", "points": 1},
            {"question": "برای مقدار None چه کلمه‌ای است؟", "answer": "None", "points": 2},
            {"question": "برای تبدیل عدد به رشته چه تابعی است؟", "answer": "str", "points": 2},
            {"question": "برای اضافه کردن به لیست چه متدی است؟", "answer": "append", "points": 2},
            {"question": "برای گرد کردن عدد چه تابعی است؟", "answer": "round", "points": 3},
            {"question": "برای بررسی نوع متغیر چه تابعی است؟", "answer": "type", "points": 2},
            {"question": "برای شرط if چه کلمه‌ای است؟", "answer": "if", "points": 1},
            {"question": "برای else چه کلمه‌ای است؟", "answer": "else", "points": 1},
            {"question": "برای ادامه حلقه چه کلمه‌ای است؟", "answer": "continue", "points": 3},
            {"question": "برای خروج از حلقه چه کلمه‌ای است؟", "answer": "break", "points": 3},
            {"question": "برای ایجاد set خالی چه تابعی است؟", "answer": "set()", "points": 2},
            {"question": "برای کوچک کردن حروف چه متدی است؟", "answer": "lower", "points": 2},
            {"question": "برای جستجوی زیررشته چه متدی است؟", "answer": "find", "points": 3},
            {"question": "برای ایجاد شیء چه متدی است؟", "answer": "__init__", "points": 4},
            {"question": "برای حذف از لیست چه متدی است？", "answer": "remove", "points": 2},
            {"question": "برای باز کردن فایل چه تابعی است؟", "answer": "open", "points": 2},
            {"question": "برای بستن فایل چه متدی است؟", "answer": "close", "points": 1},
            {"question": "برای خواندن خطوط فایل چه متدی است؟", "answer": "readlines", "points": 3},
            {"question": "برای بزرگترین عدد چه تابعی است؟", "answer": "max", "points": 2},
            {"question": "برای کوچکترین عدد چه تابعی است؟", "answer": "min", "points": 2},
            {"question": "پسوند فایل پایتون چیست？", "answer": ".py", "points": 2},
            {"question": "برای ایجاد دنباله اعداد چه تابعی است؟", "answer": "range", "points": 3},
        ]
        
        # محاسبه کل امتیازها
        self.total_points = sum(q["points"] for q in self.questions)
        
        # ایجاد رابط
        self.setup_ui()
        
        # نمایش اولین سوال
        self.show_question()
        
        self.root.mainloop()
    
    def setup_ui(self):
        # عنوان
        self.title_label = tk.Label(self.root, text="بازی سوال و جواب پایتون", 
                                   font=("Arial", 20))
        self.title_label.pack(pady=10)
        
        # امتیاز
        self.score_label = tk.Label(self.root, text=f"امتیاز: 0/{self.total_points}", 
                                   font=("Arial", 14))
        self.score_label.pack()
        
        # شماره سوال
        self.question_number_label = tk.Label(self.root, text="سوال: 1/40", 
                                             font=("Arial", 12))
        self.question_number_label.pack(pady=5)
        
        # سوال
        self.question_label = tk.Label(self.root, text="", 
                                      font=("Arial", 14), 
                                      wraplength=700,
                                      justify="center")
        self.question_label.pack(pady=20, padx=20)
        
        # امتیاز سوال
        self.points_label = tk.Label(self.root, text="", 
                                    font=("Arial", 12))
        self.points_label.pack()
        
        # ورودی پاسخ
        self.answer_label = tk.Label(self.root, text="پاسخ:", font=("Arial", 12))
        self.answer_label.pack()
        
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14), width=40)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # دکمه‌ها
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.check_button = tk.Button(button_frame, text="بررسی", 
                                     font=("Arial", 12), width=10,
                                     command=self.check_answer)
        self.check_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = tk.Button(button_frame, text="بعدی", 
                                    font=("Arial", 12), width=10,
                                    command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.hint_button = tk.Button(button_frame, text="راهنما", 
                                    font=("Arial", 12), width=10,
                                    command=self.show_hint)
        self.hint_button.pack(side=tk.LEFT, padx=5)
        
        # پیشرفت
        self.progress_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.progress_label.pack(pady=5)
        
        # تمرکز روی ورودی
        self.answer_entry.focus()
    
    def show_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            
            # نمایش سوال
            self.question_label.config(text=q["question"])
            
            # نمایش شماره سوال
            self.question_number_label.config(text=f"سوال: {self.current_question + 1}/40")
            
            # نمایش امتیاز سوال
            self.points_label.config(text=f"امتیاز این سوال: {q['points']}")
            
            # پاک کردن ورودی
            self.answer_entry.delete(0, tk.END)
            
            # فعال/غیرفعال کردن دکمه‌ها
            self.check_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
            
            # نمایش پیشرفت
            progress = int((self.current_question / len(self.questions)) * 50)
            bar = "█" * progress + "░" * (50 - progress)
            self.progress_label.config(text=f"[{bar}]")
            
            # به‌روزرسانی عنوان پنجره
            self.root.title(f"سوال {self.current_question + 1}/40 - بازی پایتون")
        else:
            self.end_game()
    
    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.current_question]["answer"].lower()
        
        if not user_answer:
            messagebox.showwarning("خطا", "لطفاً پاسخ را وارد کنید")
            return
        
        if user_answer == correct_answer:
            self.score += self.questions[self.current_question]["points"]
            self.score_label.config(text=f"امتیاز: {self.score}/{self.total_points}")
            messagebox.showinfo("درست", "✅ پاسخ درست است!")
        else:
            messagebox.showwarning("اشتباه", f"❌ پاسخ اشتباه!\nپاسخ صحیح: {correct_answer}")
        
        # فعال کردن دکمه بعدی
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        
        # تمرکز روی دکمه بعدی
        self.next_button.focus()
    
    def next_question(self):
        self.current_question += 1
        self.show_question()
        self.answer_entry.focus()
    
    def show_hint(self):
        q = self.questions[self.current_question]
        answer = q["answer"]
        length = len(answer)
        
        if length > 2:
            hint = answer[0] + "*" * (length - 2) + answer[-1]
        else:
            hint = answer[0] + "*" * (length - 1)
        
        messagebox.showinfo("راهنما", 
                          f"طول پاسخ: {length} حرف\n"
                          f"راهنما: {hint}\n"
                          f"امتیاز: {q['points']}")
    
    def end_game(self):
        percentage = (self.score / self.total_points) * 100
        
        if percentage >= 80:
            grade = "عالی 🎯"
        elif percentage >= 60:
            grade = "خوب 👍"
        elif percentage >= 40:
            grade = "متوسط ⚖️"
        else:
            grade = "نیاز به تلاش بیشتر 📚"
        
        result = f"""🎮 بازی تمام شد!

امتیاز شما: {self.score} از {self.total_points}
درصد: {percentage:.1f}%
سطح: {grade}

"""
        messagebox.showinfo("پایان بازی", result)
        
        # پرسش برای شروع مجدد
        if messagebox.askyesno("شروع مجدد", "آیا می‌خواهید دوباره بازی کنید؟"):
            self.score = 0
            self.current_question = 0
            self.score_label.config(text=f"امتیاز: 0/{self.total_points}")
            self.show_question()
        else:
            self.root.destroy()

# اجرای بازی
if __name__ == "__main__":
    game = PythonQuiz()
