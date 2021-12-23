import time
import threading
class SasorizaChallenge():
    def __init__(self,zodiac="さそり座",sex="女") -> None:
        self.intro_sec = 15
        self.question_result = False
        self.zodiac = zodiac
        self.sex = sex
        self.list_zodiac = ["おひつじ座","おうし座","ふたご座","かに座","しし座",
                            "おとめ座","てんびん座","さそり座","いて座","やぎ座","みずがめ座","うお座"]
        self.list_sex = ["男","女"]
        self.player = input(f"■{zodiac}の{sex}チャレンジ\n\n名前を入力してください:")
        if self.player == "" :self.player = "ともしげ"
        print(f"\n{self.player}さん。イントロ{self.intro_sec}秒以内に正しい星座と性別を入力して下さい。\n")
        time.sleep(2)
        print(f"★ ★ ★ チャレンジスタートです ★ ★ ★\n")
        Thread = threading.Thread(target=self.__question)
        Thread.start()
        self.__count_intro()
        
    def __count_intro(self) -> None:
        for i in range(self.intro_sec):
            if self.question_result is True:
                print(f"\n\n芝&{self.player}:そうよ私は～♪{self.zodiac}の{self.sex}～♪\n\n")
                print(f"{self.zodiac}の{self.sex}チャレンジ成功")
                return
            if i + 1 == self.intro_sec:
                print(f"\n\n芝:いいえ私は～♪{self.zodiac}の{self.sex}～♪\n\n")
                print(f"時間切れ！{self.zodiac}の{self.sex}チャレンジ失敗")
                self.question_result = True
                return
            time.sleep(1)

    def __question(self) -> bool:
        self.question_result = False
        while True:
            anser_zodiac = input("星座を入力して下さい:")
            if anser_zodiac in self.list_zodiac:
                print(f"{self.player}:{anser_zodiac}ですか？")
                if anser_zodiac == self.zodiac:
                    print("(芝:そうよ…)")
                    break
                else:
                    if self.question_result is True:
                        return
                    print("(芝:いいえ…)")
            else:
                if self.question_result is True:
                    return
                print("星座が認識できません。以下のいずれかを入力して下さい。\nおひつじ座 おうし座 ふたご座 かに座 しし座 おとめ座\nてんびん座 さそり座 いて座 やぎ座 みずがめ座 うお座\n")
        while True:
            anser_sex = input("性別を入力してください:")
            if anser_sex in self.list_sex:
                print(f"{self.player}:{anser_sex}ですか？")
                if anser_sex == self.sex:
                    print("(芝:そうよ…)")
                    self.question_result = True
                    break
                else:
                    if self.question_result is True:
                        return
                    print("(芝:いいえ…)")
            else:
                if self.question_result is True:
                    return
                print("性別が認識できません。以下のどちらかを入力して下さい。\n男  女\n")

if __name__ == "__main__":      
    sasori = SasorizaChallenge()
