{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d5c6ae16",
   "metadata": {},
   "outputs": [],
   "source": [
    "import PyPDF2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c895f968",
   "metadata": {},
   "outputs": [],
   "source": [
    "myfile=open('US_Declaration.pdf',mode='rb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "81163952",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdf_reader=PyPDF2.PdfReader(myfile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "32839ff6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(pdf_reader.pages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "91dae40e",
   "metadata": {},
   "outputs": [],
   "source": [
    "page_one=pdf_reader.pages[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f4c36984",
   "metadata": {},
   "outputs": [],
   "source": [
    "mytest=page_one.extract_text()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a9b27261",
   "metadata": {},
   "outputs": [],
   "source": [
    "myfile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1370c4bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "f=open(\"US_Declaration.pdf\",mode='rb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6cc89f2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdf_reader=PyPDF2.PdfReader(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cc14c9d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "first_page=pdf_reader.pages[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8a350b7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdf_writer=PyPDF2.PdfWriter()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "930649ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'/Type': '/Page',\n",
       " '/Contents': {},\n",
       " '/MediaBox': [0, 0, 612, 792],\n",
       " '/Resources': {'/Font': {'/F9': {'/Type': '/Font',\n",
       "    '/Subtype': '/Type1',\n",
       "    '/Name': '/F9',\n",
       "    '/Encoding': '/WinAnsiEncoding',\n",
       "    '/FirstChar': 31,\n",
       "    '/LastChar': 255,\n",
       "    '/Widths': [778,\n",
       "     250,\n",
       "     333,\n",
       "     555,\n",
       "     500,\n",
       "     500,\n",
       "     1000,\n",
       "     833,\n",
       "     278,\n",
       "     333,\n",
       "     333,\n",
       "     500,\n",
       "     570,\n",
       "     250,\n",
       "     333,\n",
       "     250,\n",
       "     278,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     333,\n",
       "     333,\n",
       "     570,\n",
       "     570,\n",
       "     570,\n",
       "     500,\n",
       "     930,\n",
       "     722,\n",
       "     667,\n",
       "     722,\n",
       "     722,\n",
       "     667,\n",
       "     611,\n",
       "     778,\n",
       "     778,\n",
       "     389,\n",
       "     500,\n",
       "     778,\n",
       "     667,\n",
       "     944,\n",
       "     722,\n",
       "     778,\n",
       "     611,\n",
       "     778,\n",
       "     722,\n",
       "     556,\n",
       "     667,\n",
       "     722,\n",
       "     722,\n",
       "     1000,\n",
       "     722,\n",
       "     722,\n",
       "     667,\n",
       "     333,\n",
       "     278,\n",
       "     333,\n",
       "     581,\n",
       "     500,\n",
       "     333,\n",
       "     500,\n",
       "     556,\n",
       "     444,\n",
       "     556,\n",
       "     444,\n",
       "     333,\n",
       "     500,\n",
       "     556,\n",
       "     278,\n",
       "     333,\n",
       "     556,\n",
       "     278,\n",
       "     833,\n",
       "     556,\n",
       "     500,\n",
       "     556,\n",
       "     556,\n",
       "     444,\n",
       "     389,\n",
       "     333,\n",
       "     556,\n",
       "     500,\n",
       "     722,\n",
       "     500,\n",
       "     500,\n",
       "     444,\n",
       "     394,\n",
       "     220,\n",
       "     394,\n",
       "     520,\n",
       "     778,\n",
       "     500,\n",
       "     778,\n",
       "     333,\n",
       "     500,\n",
       "     500,\n",
       "     1000,\n",
       "     500,\n",
       "     500,\n",
       "     333,\n",
       "     1000,\n",
       "     556,\n",
       "     333,\n",
       "     1000,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     333,\n",
       "     333,\n",
       "     500,\n",
       "     500,\n",
       "     350,\n",
       "     500,\n",
       "     1000,\n",
       "     333,\n",
       "     1000,\n",
       "     389,\n",
       "     333,\n",
       "     722,\n",
       "     778,\n",
       "     778,\n",
       "     722,\n",
       "     250,\n",
       "     333,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     220,\n",
       "     500,\n",
       "     333,\n",
       "     747,\n",
       "     300,\n",
       "     500,\n",
       "     570,\n",
       "     333,\n",
       "     747,\n",
       "     500,\n",
       "     400,\n",
       "     549,\n",
       "     300,\n",
       "     300,\n",
       "     333,\n",
       "     576,\n",
       "     540,\n",
       "     250,\n",
       "     333,\n",
       "     300,\n",
       "     330,\n",
       "     500,\n",
       "     750,\n",
       "     750,\n",
       "     750,\n",
       "     500,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     1000,\n",
       "     722,\n",
       "     667,\n",
       "     667,\n",
       "     667,\n",
       "     667,\n",
       "     389,\n",
       "     389,\n",
       "     389,\n",
       "     389,\n",
       "     722,\n",
       "     722,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     570,\n",
       "     778,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     611,\n",
       "     556,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     722,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     278,\n",
       "     278,\n",
       "     278,\n",
       "     278,\n",
       "     500,\n",
       "     556,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     549,\n",
       "     500,\n",
       "     556,\n",
       "     556,\n",
       "     556,\n",
       "     556,\n",
       "     500,\n",
       "     556,\n",
       "     500],\n",
       "    '/BaseFont': '/TimesNewRomanPS-BoldMT',\n",
       "    '/FontDescriptor': {'/Type': '/FontDescriptor',\n",
       "     '/FontName': '/TimesNewRomanPS-BoldMT',\n",
       "     '/Ascent': 677,\n",
       "     '/CapHeight': 500,\n",
       "     '/Descent': -216,\n",
       "     '/Flags': 34,\n",
       "     '/FontBBox': [-558, -307, 2034, 1026],\n",
       "     '/ItalicAngle': 0,\n",
       "     '/StemV': 0,\n",
       "     '/AvgWidth': 427,\n",
       "     '/Leading': 150,\n",
       "     '/MaxWidth': 2592,\n",
       "     '/XHeight': 250,\n",
       "     '/FontFile': {'/Filter': ['/ASCII85Decode'],\n",
       "      '/Length1': 4690,\n",
       "      '/Length2': 46374,\n",
       "      '/Length3': 532}}},\n",
       "   '/F6': {'/Type': '/Font',\n",
       "    '/Subtype': '/Type1',\n",
       "    '/Name': '/F6',\n",
       "    '/Encoding': '/WinAnsiEncoding',\n",
       "    '/FirstChar': 31,\n",
       "    '/LastChar': 255,\n",
       "    '/Widths': [778,\n",
       "     250,\n",
       "     333,\n",
       "     408,\n",
       "     500,\n",
       "     500,\n",
       "     833,\n",
       "     778,\n",
       "     180,\n",
       "     333,\n",
       "     333,\n",
       "     500,\n",
       "     564,\n",
       "     250,\n",
       "     333,\n",
       "     250,\n",
       "     278,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     278,\n",
       "     278,\n",
       "     564,\n",
       "     564,\n",
       "     564,\n",
       "     444,\n",
       "     921,\n",
       "     722,\n",
       "     667,\n",
       "     667,\n",
       "     722,\n",
       "     611,\n",
       "     556,\n",
       "     722,\n",
       "     722,\n",
       "     333,\n",
       "     389,\n",
       "     722,\n",
       "     611,\n",
       "     889,\n",
       "     722,\n",
       "     722,\n",
       "     556,\n",
       "     722,\n",
       "     667,\n",
       "     556,\n",
       "     611,\n",
       "     722,\n",
       "     722,\n",
       "     944,\n",
       "     722,\n",
       "     722,\n",
       "     611,\n",
       "     333,\n",
       "     278,\n",
       "     333,\n",
       "     469,\n",
       "     500,\n",
       "     333,\n",
       "     444,\n",
       "     500,\n",
       "     444,\n",
       "     500,\n",
       "     444,\n",
       "     333,\n",
       "     500,\n",
       "     500,\n",
       "     278,\n",
       "     278,\n",
       "     500,\n",
       "     278,\n",
       "     778,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     333,\n",
       "     389,\n",
       "     278,\n",
       "     500,\n",
       "     500,\n",
       "     722,\n",
       "     500,\n",
       "     500,\n",
       "     444,\n",
       "     480,\n",
       "     200,\n",
       "     480,\n",
       "     541,\n",
       "     778,\n",
       "     500,\n",
       "     778,\n",
       "     333,\n",
       "     500,\n",
       "     444,\n",
       "     1000,\n",
       "     500,\n",
       "     500,\n",
       "     333,\n",
       "     1000,\n",
       "     556,\n",
       "     333,\n",
       "     889,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     778,\n",
       "     333,\n",
       "     333,\n",
       "     444,\n",
       "     444,\n",
       "     350,\n",
       "     500,\n",
       "     1000,\n",
       "     333,\n",
       "     980,\n",
       "     389,\n",
       "     333,\n",
       "     722,\n",
       "     778,\n",
       "     778,\n",
       "     722,\n",
       "     250,\n",
       "     333,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     200,\n",
       "     500,\n",
       "     333,\n",
       "     760,\n",
       "     276,\n",
       "     500,\n",
       "     564,\n",
       "     333,\n",
       "     760,\n",
       "     500,\n",
       "     400,\n",
       "     549,\n",
       "     300,\n",
       "     300,\n",
       "     333,\n",
       "     576,\n",
       "     453,\n",
       "     250,\n",
       "     333,\n",
       "     300,\n",
       "     310,\n",
       "     500,\n",
       "     750,\n",
       "     750,\n",
       "     750,\n",
       "     444,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     889,\n",
       "     667,\n",
       "     611,\n",
       "     611,\n",
       "     611,\n",
       "     611,\n",
       "     333,\n",
       "     333,\n",
       "     333,\n",
       "     333,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     564,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     722,\n",
       "     556,\n",
       "     500,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     667,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     444,\n",
       "     278,\n",
       "     278,\n",
       "     278,\n",
       "     278,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     549,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500,\n",
       "     500],\n",
       "    '/BaseFont': '/TimesNewRomanPSMT',\n",
       "    '/FontDescriptor': {'/Type': '/FontDescriptor',\n",
       "     '/FontName': '/TimesNewRomanPSMT',\n",
       "     '/Ascent': 693,\n",
       "     '/CapHeight': 500,\n",
       "     '/Descent': -216,\n",
       "     '/Flags': 34,\n",
       "     '/FontBBox': [-568, -307, 2028, 1007],\n",
       "     '/ItalicAngle': 0,\n",
       "     '/StemV': 0,\n",
       "     '/AvgWidth': 401,\n",
       "     '/Leading': 150,\n",
       "     '/MaxWidth': 2597,\n",
       "     '/XHeight': 250,\n",
       "     '/FontFile': {'/Filter': ['/ASCII85Decode'],\n",
       "      '/Length1': 4680,\n",
       "      '/Length2': 46205,\n",
       "      '/Length3': 532}}}},\n",
       "  '/ProcSet': ['/PDF', '/Text']},\n",
       " '/Parent': {'/Type': '/Pages',\n",
       "  '/Count': 1,\n",
       "  '/Kids': [IndirectObject(4, 0, 2546711478128)]}}"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pdf_writer.add_page(first_page)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "960cf0d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(False, <_io.BufferedWriter name='MY_BRAND_NEW_PDF'>)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pdf_output=open(\"MY_BRAND_NEW_PDF\",mode='wb')\n",
    "pdf_writer.write(pdf_output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fc94e1b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdf_output.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "56084f9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "976b6bf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "f=open(\"MY_BRAND_NEW_PDF\",'rb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "58644b8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdf_reader=PyPDF2.PdfReader(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1cf63b24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(pdf_reader.pages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3c25fa40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Declaration of Independence\n",
      "IN CONGRESS, July 4, 1776.  \n",
      "The unanimous Declaration of the thirteen united States of America,  \n",
      "When in the Course of human events, it becomes necessary for one people to dissolve thepolitical bands which have connected them with another, and to assume among the powers of theearth, the separate and equal station to which the Laws of Nature and of Nature's God entitlethem, a decent respect to the opinions of mankind requires that they should declare the causeswhich impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed bytheir Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit\n",
      "of Happiness.— \u0014That to secure these rights, Governments are instituted among Men, derivingtheir just powers from the consent of the governed,—  \u0014That whenever any Form of Government\n",
      "becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to\n",
      "institute new Government, laying its foundation on such principles and organizing its powers in\n",
      "such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence,indeed, will dictate that Governments long established should not be changed for light andtransient causes; and accordingly all experience hath shewn, that mankind are more disposed to\n",
      "suffer, while evils are sufferable, than to right themselves by abolishing the forms to which theyare accustomed. But when a long train of abuses and usurpations, pursuing invariably the same\n",
      "Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty,\n",
      "to throw off such Government, and to provide new Guards for their future securit y.— \u0014Such has\n",
      "been the patient sufferance of these Colonies; and such is now the necessity which constrainsthem to alter their former Systems of Government. The history of the present King of GreatBritain is a history of repeated injuries and usurpations, all having in direct object the\n",
      "establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a\n",
      "candid world. \n",
      "He has refused his Assent to Laws, the most wholesome and necessary for the\n",
      "public good.He has forbidden his Governors to pass Laws of immediate and pressingimportance, unless suspended in their operation till his Assent should be obtained;and when so suspended, he has utterly neglected to attend to them.He has refused to pass other Laws for the accommodation of large districts of\n",
      "people, unless those people would relinquish the right of Representation in theLegislature, a right inestimable to them and formidable to tyrants only. He has called together legislative bodies at places unusual, uncomfortable, and distantfrom the depository of their public Records, for the sole purpose of fatiguing them into\n",
      "compliance with his measures.\n"
     ]
    }
   ],
   "source": [
    "print(f_page.extract_text())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "91d53642",
   "metadata": {},
   "outputs": [],
   "source": [
    "f=open('US_Declaration.pdf',mode='rb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "91e18305",
   "metadata": {},
   "outputs": [],
   "source": [
    "pdf_text=[]\n",
    "pdf_reader=PyPDF2.PdfReader(f)\n",
    "for p in range(len(pdf_reader.pages)):\n",
    "    pdf_text.append(pdf_reader.pages[p].extract_text())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ba9d0380",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\"Declaration of Independence\\nIN CONGRESS, July 4, 1776.  \\nThe unanimous Declaration of the thirteen united States of America,  \\nWhen in the Course of human events, it becomes necessary for one people to dissolve thepolitical bands which have connected them with another, and to assume among the powers of theearth, the separate and equal station to which the Laws of Nature and of Nature's God entitlethem, a decent respect to the opinions of mankind requires that they should declare the causeswhich impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed bytheir Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit\\nof Happiness.— \\x14That to secure these rights, Governments are instituted among Men, derivingtheir just powers from the consent of the governed,—  \\x14That whenever any Form of Government\\nbecomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to\\ninstitute new Government, laying its foundation on such principles and organizing its powers in\\nsuch form, as to them shall seem most likely to effect their Safety and Happiness. Prudence,indeed, will dictate that Governments long established should not be changed for light andtransient causes; and accordingly all experience hath shewn, that mankind are more disposed to\\nsuffer, while evils are sufferable, than to right themselves by abolishing the forms to which theyare accustomed. But when a long train of abuses and usurpations, pursuing invariably the same\\nObject evinces a design to reduce them under absolute Despotism, it is their right, it is their duty,\\nto throw off such Government, and to provide new Guards for their future securit y.— \\x14Such has\\nbeen the patient sufferance of these Colonies; and such is now the necessity which constrainsthem to alter their former Systems of Government. The history of the present King of GreatBritain is a history of repeated injuries and usurpations, all having in direct object the\\nestablishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a\\ncandid world. \\nHe has refused his Assent to Laws, the most wholesome and necessary for the\\npublic good.He has forbidden his Governors to pass Laws of immediate and pressingimportance, unless suspended in their operation till his Assent should be obtained;and when so suspended, he has utterly neglected to attend to them.He has refused to pass other Laws for the accommodation of large districts of\\npeople, unless those people would relinquish the right of Representation in theLegislature, a right inestimable to them and formidable to tyrants only. He has called together legislative bodies at places unusual, uncomfortable, and distantfrom the depository of their public Records, for the sole purpose of fatiguing them into\\ncompliance with his measures.\", 'He has dissolved Re presentative Ho uses repeatedly , for opposing wit h manly\\nfirmness his invasions on the rights of the people.\\nHe has refused for a long time, after such dissolutions, to cause others to be\\nelected; whereby the Leg islative powers, incapable of Annihilation, have returned\\nto the People at lar ge for their exe rcise; the State r emaining in the me an time\\nexposed to all the dangers of invasion from without, and convulsions within.\\nHe has endeavou red to prevent the  population of these  States; for that pur pose\\nobstructing the L aws for Natural ization of Foreig ners; refusing  to pass others to\\nencourage their migrations hither, and raising the conditions of new\\nAppropriations of  Lands.\\nHe has obstructed the Administration of Justice, by refusing his Assent to Laws\\nfor establishing  Judiciary pow ers.\\nHe has made Judge s dependent on his Wil l alone, for the te nure of their off ices,\\nand the amount and  payment of t heir salaries.\\nHe has erected  a multitude of New  Offices, and se nt hither swarms of  Officers to\\nharrass our people, and eat out their substance.\\nHe has kept among us, in times of peace, Standing Armies without the Consent of\\nour legislature s.\\nHe has affected to render the Military independent of a nd superior to the Civil power.\\nHe has combined with others to subject us to a jurisdiction foreign to our\\nconstitution, and unacknowledged by our laws; giving his Assent to their Acts of\\npretended Legislation:\\nFor Quartering  large bodies of  armed troops amon g us:\\nFor protecting them, by a mock Trial, from punishment for any  Murders which\\nthey should c ommit on the Inha bitants of these Sta tes:\\nFor cutting off our Trade with all parts of the world:\\nFor imposing Taxe s on us without our Con sent: For deprivi ng us in many  cases,\\nof the benefits of T rial by J ury:\\nFor transporting us beyond Seas to be tried for pretended of fences\\nFor abolishing the free System of English L aws in a neighbouring Province,\\nestablishing therein an Arbitrary government, and e nlarging its Boundaries so as', 'to render it at onc e an example and fi t instrument for intr oducing the same\\nabsolute rule into  these Colonies:\\nFor taking away our Charters, abolishing our most valuable L aws, and altering\\nfundamentally  the Forms of our G overnments:\\nFor suspending  our own Leg islatures, and de claring themse lves invested with\\npower to legislate for us in all cases whatsoever.\\nHe has abdicated Government here, by declar ing us out of his Protection and\\nwaging War ag ainst us.\\nHe has plundered our seas, ravaged our Coasts, burnt our towns, and destroy ed the\\nlives of our people.\\nHe is at this time transporting large Armies of foreign Mercenaries to compleat\\nthe works of death, desolation and tyranny , already begun with circumstances of\\nCruelty & pe rfidy scar cely para lleled in the most ba rbarous ages,  and totally\\nunworthy of the Head of a civilized nation.\\nHe has constrained our fellow Citizens taken Captive on the high Seas to bear\\nArms against their Country, to become the executioners of their friends and\\nBrethren, or to  fall themselves by  their Hands.\\nHe has excited domestic insurrections amongst us, and has endeavoured to bring\\non the inhabitants of our frontiers, the merciless Indian Savages, whose known\\nrule of warfare, is an undistinguished destruction of all ages, sexes and conditions. \\nIn every  stage of these O ppressions We have  Petitioned for Redr ess in the most humble  terms:\\nOur repeated Pe titions have been a nswered only  by repeate d injury. A Pr ince whose char acter is\\nthus marked by every ac t which may define a Tyra nt, is unfit to be the ruler of a free people. \\nNor have We been wanting in attentions to our Brittish brethren. We have warned them from\\ntime to time  of attemp ts by th eir legi slature t o extend an  unwarra ntable jur isdiction  over us. We\\nhave reminded them of the circumstances of our emigration and settlement here. We have\\nappealed to their native justice and magnanimity, and we have c onjured them by the ties of our\\ncommon kindred to disavow these usurpations, which, would inevitably interrupt our\\nconnections and correspondence. They too have bee n deaf to the voice of justice and of\\nconsanguinity. We must, therefore, acquiesce in the necessity , which denounces our Separation,\\nand hold them, as we hold the rest of mankind, Enemies in War, in Peace Friends. \\nWe, therefore, t he Representativ es of the united Sta tes of America, i n General Congr ess,\\nAssembled, appealing to the Supreme Judge of the world for the rectitude of our intentions, do,\\nin the Name, and by Authority of the g ood People of these Colonies, solemnly publish and\\ndeclare, That th ese United Colonie s are, and of Rig ht ought to be Fre e and Indepe ndent States;\\nthat they are Absolved from all Allegiance to the British Crown, and that a ll political connection', 'between them and the State of Great Britain, is and ought to be totally dissolved; and that as Freeand Independent States, they have full Power to levy War, conclude Peace, contract Alliances,\\nestablish Commerce, and to do all other Acts and Things which Independent States may of rightdo. And for the support of this Declaration, with a firm reliance on the protection of divineProvidence, we mutually pledge to each other our Lives, our Fortunes and our sacred Honor.[The 56 signatures on the Declaration were arranged in six columns: ] \\n[Column 1] Georgia:\\n   Button Gwinnett\\n   Lyman Hall\\n   George Walton \\n[Column 2] North Carolina:\\n   William Hooper\\n   Joseph Hewes\\n   John Penn\\n South Carolina:\\n   Edward Ru tledge\\n   Thomas Heyward, Jr.\\n  Thomas Lynch, Jr.\\n  Arthur Middleton \\n[Column 3] Massachusetts:\\n   John Hancock Maryland:\\n   Samuel Chase   William Paca   Thomas Stone   Charles Carroll of Carrollton Virginia:\\n   George Wythe   Richard Henry Lee   Thomas Jefferson   Benjamin Harrison   Thomas Nelson, Jr.   Francis Lightfoot Lee   Carter Braxton [Column 4] Pennsylvania:\\n  Robert Morris   Benjamin Rush\\n   Benjamin Fran klin\\n   John Morton', '   George Clymer\\n   James Smith\\n   George Taylor\\n   James Wilson\\n   George Ross\\n Delaware:\\n   Caesar Rodney\\n   George Read\\n   Thomas McKean \\n[Column 5] New York:\\n   Wi lliam Floyd\\n   Philip Livingston\\n   Francis L ewis\\n   Lewis Morris\\n New Jersey:\\n   Richard Stockton\\n   John Witherspoon\\n   Francis Hopkinson\\n   John Hart\\n   Abraham Clark \\n[Column 6] New Hampshire:\\n   Josiah Bartlett\\n   William Whipple\\n Massachusetts:\\n   Samuel Adams\\n   John Adams\\n   Robert Treat Paine\\n   Elbridge Gerry\\n Rhode Island:\\n   Stephen Hopkins\\n   William Ellery\\n Connecticut:\\n   Roger Sherman\\n   Samuel Huntington\\n   William Williams\\n   Oliver Wolcott\\n New Hampshire:\\n Matthew Thornton\\n ']\n"
     ]
    }
   ],
   "source": [
    "print(pdf_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "4b89c594",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(len(pdf_text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f78bfb09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(pdf_reader.pages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "1df3a068",
   "metadata": {},
   "outputs": [],
   "source": [
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a10a6b55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(pdf_reader.pages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "80c91b40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Declaration of Independence\n",
      "IN CONGRESS, July 4, 1776.  \n",
      "The unanimous Declaration of the thirteen united States of America,  \n",
      "When in the Course of human events, it becomes necessary for one people to dissolve thepolitical bands which have connected them with another, and to assume among the powers of theearth, the separate and equal station to which the Laws of Nature and of Nature's God entitlethem, a decent respect to the opinions of mankind requires that they should declare the causeswhich impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed bytheir Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit\n",
      "of Happiness.— \u0014That to secure these rights, Governments are instituted among Men, derivingtheir just powers from the consent of the governed,—  \u0014That whenever any Form of Government\n",
      "becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to\n",
      "institute new Government, laying its foundation on such principles and organizing its powers in\n",
      "such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence,indeed, will dictate that Governments long established should not be changed for light andtransient causes; and accordingly all experience hath shewn, that mankind are more disposed to\n",
      "suffer, while evils are sufferable, than to right themselves by abolishing the forms to which theyare accustomed. But when a long train of abuses and usurpations, pursuing invariably the same\n",
      "Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty,\n",
      "to throw off such Government, and to provide new Guards for their future securit y.— \u0014Such has\n",
      "been the patient sufferance of these Colonies; and such is now the necessity which constrainsthem to alter their former Systems of Government. The history of the present King of GreatBritain is a history of repeated injuries and usurpations, all having in direct object the\n",
      "establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a\n",
      "candid world. \n",
      "He has refused his Assent to Laws, the most wholesome and necessary for the\n",
      "public good.He has forbidden his Governors to pass Laws of immediate and pressingimportance, unless suspended in their operation till his Assent should be obtained;and when so suspended, he has utterly neglected to attend to them.He has refused to pass other Laws for the accommodation of large districts of\n",
      "people, unless those people would relinquish the right of Representation in theLegislature, a right inestimable to them and formidable to tyrants only. He has called together legislative bodies at places unusual, uncomfortable, and distantfrom the depository of their public Records, for the sole purpose of fatiguing them into\n",
      "compliance with his measures.\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "He has dissolved Re presentative Ho uses repeatedly , for opposing wit h manly\n",
      "firmness his invasions on the rights of the people.\n",
      "He has refused for a long time, after such dissolutions, to cause others to be\n",
      "elected; whereby the Leg islative powers, incapable of Annihilation, have returned\n",
      "to the People at lar ge for their exe rcise; the State r emaining in the me an time\n",
      "exposed to all the dangers of invasion from without, and convulsions within.\n",
      "He has endeavou red to prevent the  population of these  States; for that pur pose\n",
      "obstructing the L aws for Natural ization of Foreig ners; refusing  to pass others to\n",
      "encourage their migrations hither, and raising the conditions of new\n",
      "Appropriations of  Lands.\n",
      "He has obstructed the Administration of Justice, by refusing his Assent to Laws\n",
      "for establishing  Judiciary pow ers.\n",
      "He has made Judge s dependent on his Wil l alone, for the te nure of their off ices,\n",
      "and the amount and  payment of t heir salaries.\n",
      "He has erected  a multitude of New  Offices, and se nt hither swarms of  Officers to\n",
      "harrass our people, and eat out their substance.\n",
      "He has kept among us, in times of peace, Standing Armies without the Consent of\n",
      "our legislature s.\n",
      "He has affected to render the Military independent of a nd superior to the Civil power.\n",
      "He has combined with others to subject us to a jurisdiction foreign to our\n",
      "constitution, and unacknowledged by our laws; giving his Assent to their Acts of\n",
      "pretended Legislation:\n",
      "For Quartering  large bodies of  armed troops amon g us:\n",
      "For protecting them, by a mock Trial, from punishment for any  Murders which\n",
      "they should c ommit on the Inha bitants of these Sta tes:\n",
      "For cutting off our Trade with all parts of the world:\n",
      "For imposing Taxe s on us without our Con sent: For deprivi ng us in many  cases,\n",
      "of the benefits of T rial by J ury:\n",
      "For transporting us beyond Seas to be tried for pretended of fences\n",
      "For abolishing the free System of English L aws in a neighbouring Province,\n",
      "establishing therein an Arbitrary government, and e nlarging its Boundaries so as\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "to render it at onc e an example and fi t instrument for intr oducing the same\n",
      "absolute rule into  these Colonies:\n",
      "For taking away our Charters, abolishing our most valuable L aws, and altering\n",
      "fundamentally  the Forms of our G overnments:\n",
      "For suspending  our own Leg islatures, and de claring themse lves invested with\n",
      "power to legislate for us in all cases whatsoever.\n",
      "He has abdicated Government here, by declar ing us out of his Protection and\n",
      "waging War ag ainst us.\n",
      "He has plundered our seas, ravaged our Coasts, burnt our towns, and destroy ed the\n",
      "lives of our people.\n",
      "He is at this time transporting large Armies of foreign Mercenaries to compleat\n",
      "the works of death, desolation and tyranny , already begun with circumstances of\n",
      "Cruelty & pe rfidy scar cely para lleled in the most ba rbarous ages,  and totally\n",
      "unworthy of the Head of a civilized nation.\n",
      "He has constrained our fellow Citizens taken Captive on the high Seas to bear\n",
      "Arms against their Country, to become the executioners of their friends and\n",
      "Brethren, or to  fall themselves by  their Hands.\n",
      "He has excited domestic insurrections amongst us, and has endeavoured to bring\n",
      "on the inhabitants of our frontiers, the merciless Indian Savages, whose known\n",
      "rule of warfare, is an undistinguished destruction of all ages, sexes and conditions. \n",
      "In every  stage of these O ppressions We have  Petitioned for Redr ess in the most humble  terms:\n",
      "Our repeated Pe titions have been a nswered only  by repeate d injury. A Pr ince whose char acter is\n",
      "thus marked by every ac t which may define a Tyra nt, is unfit to be the ruler of a free people. \n",
      "Nor have We been wanting in attentions to our Brittish brethren. We have warned them from\n",
      "time to time  of attemp ts by th eir legi slature t o extend an  unwarra ntable jur isdiction  over us. We\n",
      "have reminded them of the circumstances of our emigration and settlement here. We have\n",
      "appealed to their native justice and magnanimity, and we have c onjured them by the ties of our\n",
      "common kindred to disavow these usurpations, which, would inevitably interrupt our\n",
      "connections and correspondence. They too have bee n deaf to the voice of justice and of\n",
      "consanguinity. We must, therefore, acquiesce in the necessity , which denounces our Separation,\n",
      "and hold them, as we hold the rest of mankind, Enemies in War, in Peace Friends. \n",
      "We, therefore, t he Representativ es of the united Sta tes of America, i n General Congr ess,\n",
      "Assembled, appealing to the Supreme Judge of the world for the rectitude of our intentions, do,\n",
      "in the Name, and by Authority of the g ood People of these Colonies, solemnly publish and\n",
      "declare, That th ese United Colonie s are, and of Rig ht ought to be Fre e and Indepe ndent States;\n",
      "that they are Absolved from all Allegiance to the British Crown, and that a ll political connection\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "between them and the State of Great Britain, is and ought to be totally dissolved; and that as Freeand Independent States, they have full Power to levy War, conclude Peace, contract Alliances,\n",
      "establish Commerce, and to do all other Acts and Things which Independent States may of rightdo. And for the support of this Declaration, with a firm reliance on the protection of divineProvidence, we mutually pledge to each other our Lives, our Fortunes and our sacred Honor.[The 56 signatures on the Declaration were arranged in six columns: ] \n",
      "[Column 1] Georgia:\n",
      "   Button Gwinnett\n",
      "   Lyman Hall\n",
      "   George Walton \n",
      "[Column 2] North Carolina:\n",
      "   William Hooper\n",
      "   Joseph Hewes\n",
      "   John Penn\n",
      " South Carolina:\n",
      "   Edward Ru tledge\n",
      "   Thomas Heyward, Jr.\n",
      "  Thomas Lynch, Jr.\n",
      "  Arthur Middleton \n",
      "[Column 3] Massachusetts:\n",
      "   John Hancock Maryland:\n",
      "   Samuel Chase   William Paca   Thomas Stone   Charles Carroll of Carrollton Virginia:\n",
      "   George Wythe   Richard Henry Lee   Thomas Jefferson   Benjamin Harrison   Thomas Nelson, Jr.   Francis Lightfoot Lee   Carter Braxton [Column 4] Pennsylvania:\n",
      "  Robert Morris   Benjamin Rush\n",
      "   Benjamin Fran klin\n",
      "   John Morton\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "   George Clymer\n",
      "   James Smith\n",
      "   George Taylor\n",
      "   James Wilson\n",
      "   George Ross\n",
      " Delaware:\n",
      "   Caesar Rodney\n",
      "   George Read\n",
      "   Thomas McKean \n",
      "[Column 5] New York:\n",
      "   Wi lliam Floyd\n",
      "   Philip Livingston\n",
      "   Francis L ewis\n",
      "   Lewis Morris\n",
      " New Jersey:\n",
      "   Richard Stockton\n",
      "   John Witherspoon\n",
      "   Francis Hopkinson\n",
      "   John Hart\n",
      "   Abraham Clark \n",
      "[Column 6] New Hampshire:\n",
      "   Josiah Bartlett\n",
      "   William Whipple\n",
      " Massachusetts:\n",
      "   Samuel Adams\n",
      "   John Adams\n",
      "   Robert Treat Paine\n",
      "   Elbridge Gerry\n",
      " Rhode Island:\n",
      "   Stephen Hopkins\n",
      "   William Ellery\n",
      " Connecticut:\n",
      "   Roger Sherman\n",
      "   Samuel Huntington\n",
      "   William Williams\n",
      "   Oliver Wolcott\n",
      " New Hampshire:\n",
      " Matthew Thornton\n",
      " \n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for page in pdf_text:\n",
    "    print(page)\n",
    "    print('\\n')\n",
    "    print('\\n')\n",
    "    print('\\n')\n",
    "    print('\\n')\n",
    "    print('\\n')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "6b6d3f2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text=\"The phone number of the agent is 408-555-1234. Call Soon!\"\n",
    "\"408-555-1234\" in text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "33f535e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "063efecd",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern='phone'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "f1aa16ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<re.Match object; span=(4, 9), match='phone'>"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.search(pattern,text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "3e22c2e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_match=re.search(pattern,text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "a6d423b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4, 9)"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_match.span()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "169e05c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_match.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "e73bb7d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_match.end()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "78907947",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 8)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text=\"my phone is a new phone\"\n",
    "match=re.search('phone',text)\n",
    "match.span()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "ca5ddf88",
   "metadata": {},
   "outputs": [],
   "source": [
    "all_matches=re.findall(\"phone\",text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "73cd9bb3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['phone', 'phone']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_matches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "d42e93ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(all_matches)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "bd0addd3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<callable_iterator at 0x250f502dbe0>"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.finditer('phone',text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "c094b0e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 8)\n",
      "(18, 23)\n"
     ]
    }
   ],
   "source": [
    "for match in re.finditer('phone',text):\n",
    "    print(match.span())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "7e9122cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "text=\"My telephone number is 123-555-1234\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "65e73c90",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern=r'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "4603bf91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'My telephone number is 123-555-1234'"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "9e06ba55",
   "metadata": {},
   "outputs": [],
   "source": [
    "phone_number=re.search(pattern,text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "6c34cc94",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<re.Match object; span=(23, 35), match='123-555-1234'>"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "phone_number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "3e85eb98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(23, 35)"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "phone_number.span()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "872d1945",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'123-555-1234'"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "phone_number.group()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "6650748e",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern=r'\\d{3}-\\d{3}-\\d{4}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "e769abae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'123-555-1234'"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.search(pattern,text).group()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "e1a22c01",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern=r'\\d{3}-\\d{3}-\\d{4}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "c07a56e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'123-555-1234'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.search(pattern,text).group()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "07ee108e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 10)"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "##Now using pipe operator\n",
    "re.search(r\"man|woman\",\"This woman was here\").span()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "c31f8b4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[' hat', ' sat', 'plat']"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Now using wildcards\n",
    "re.findall(r\"..at\",\"The hat in the sat splat\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "31bd8e33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['2']"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r\"\\d$\",\"1 is the lonelist number 2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "a87515a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "phrase=\"There are 3 numbers 34 inside 5 this sentence\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "9d4dc255",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['There are ', ' numbers ', ' inside ', ' this sentence']"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r\"[^\\d]+\",phrase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "b0167c7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_phrase=\"This is a string! but it has punctuation. How to remove it?\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "85201b48",
   "metadata": {},
   "outputs": [],
   "source": [
    "mylist=re.findall(r\"[^!?.]+\",test_phrase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "f89a545d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This is a string but it has punctuation How to remove it'"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\".join(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "47db329e",
   "metadata": {},
   "outputs": [],
   "source": [
    "text=\"Only find the hyphen-words. Were are the long-ish dash words?\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "09abf8cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hyphen-words.', 'long-ish ']"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall('[\\w]+-[\\w]+',text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d09c411",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
