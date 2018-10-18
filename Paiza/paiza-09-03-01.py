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
      "hello python\n"
     ]
    }
   ],
   "source": [
    "class Greeting:\n",
    "    def __init__(self):\n",
    "        self.msg = \"hello\"\n",
    "        self.target = \"paiza\"\n",
    "\n",
    "    def say_hello(self):\n",
    "        print(self.msg + \" \" + self.target)\n",
    "\n",
    "class Hello(Greeting):\n",
    "    # ここにオーバライドするメソッドを記述する\n",
    "        def say_hello(self,target):\n",
    "            print(self.msg+\" \"+target)\n",
    "\n",
    "\n",
    "\n",
    "player = Hello()\n",
    "player.say_hello(\"python\")"
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
