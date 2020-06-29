{
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\nIKkbY7z3KfkAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2213c95e5c0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "d=xtest[25]\n",
    "d.shape=(28,28)\n",
    "pt.imshow(255-d)\n",
    "\n",
    "print(clf.predict([xtest[25]]))\n",
    "pt.show()\n",
    "         "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy= 10.104761904761904\n"
     ]
    }
   ],
   "source": [
    "p=clf.predict(xtest)\n",
    "count=0\n",
    "for i in range(0,21000):\n",
    "    count+=1 if p[i]==actual_label[i] else 0\n",
    "print (\"Accuracy=\", (count/21000)*100)"
   ]
  },