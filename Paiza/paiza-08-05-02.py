{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "合計は113点です\n"
     ]
    }
   ],
   "source": [
    "# coding: utf-8\n",
    "# 学生メソッドを作る\n",
    "\n",
    "class Gakusei:\n",
    "    def __init__(self, kokugo, sansu):\n",
    "        self.kokugo = kokugo\n",
    "        self.sansu  = sansu\n",
    "\n",
    "    # この下に、合計得点を戻り値として返すsumメソッドを記述する\n",
    "    def sum(self):\n",
    "        return(self.kokugo+self.sansu)\n",
    "\n",
    "yamada = Gakusei(70, 43)\n",
    "print(\"合計は\" + str(yamada.sum()) + \"点です\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
