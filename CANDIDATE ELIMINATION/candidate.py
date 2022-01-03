{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c69048ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The concepts to be learned\n",
      "[['green' 'hard' 'no' 'wrinkled']\n",
      " ['green' 'hard' 'yes' 'smooth']\n",
      " ['brown' 'soft' 'no' 'wrinkled']\n",
      " ['orange' 'hard' 'no' 'wrinkled']\n",
      " ['green' 'soft' 'yes' 'smooth']\n",
      " ['green' 'hard' 'yes' 'wrinkled']\n",
      " ['orange' 'hard' 'no' 'wrinkled']]\n",
      "\n",
      "Labels specific to the concepts\n",
      "\n",
      "['Yes' 'no' 'no' 'Yes' 'Yes' 'Yes' 'Yes']\n",
      "\n",
      "\n",
      "Final S:  ['?' '?' '?' '?']\n",
      "Final G:  []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "data = pd.read_csv('data.csv')\n",
    "concept = np.array(data)[:,:-1]\n",
    "print(\"The concepts to be learned\")\n",
    "print(concept)\n",
    "target = np.array(data)[:,-1]\n",
    "print(\"\\nLabels specific to the concepts\\n\")\n",
    "print(target)\n",
    "print(\"\\n\")\n",
    "def learn(concept,target):\n",
    "    specific_h = concept[0].copy()\n",
    "    general_h = [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]\n",
    "    for i,h in enumerate(concept):\n",
    "        if target[i]=='Yes':\n",
    "            for j in range(len(specific_h)):\n",
    "                if h[j]!=specific_h[j]:\n",
    "                    specific_h[j]='?'\n",
    "                    general_h[j][j]='?'\n",
    "        elif target[i]=='No':\n",
    "            for j in range(len(specific_h)):\n",
    "                if h[j]!=specific_h[j]:\n",
    "                    general_h[j][j]=specific_h[j]\n",
    "                else:\n",
    "                    general_h[j][j]='?'\n",
    "    indices = [i for i,val in enumerate(general_h) if val==['?' for i in range(len(specific_h))]]\n",
    "    for i in indices:\n",
    "        general_h.remove(['?' for i in range(len(specific_h))])\n",
    "    return specific_h,general_h\n",
    "s_final, g_final = learn(concept,target)\n",
    "print(\"Final S: \", s_final)\n",
    "print(\"Final G: \", g_final)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50f134e4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b74ee62",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
