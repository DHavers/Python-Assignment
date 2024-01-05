{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bd4d4f5d-0cf1-4d80-8889-e55210572c5c",
   "metadata": {},
   "source": [
    "# Ultimatly this code will hopefully be able to predict whether a protein is likely to be secreted via the Sec or Tat system, or not secreted at all, based on the protein sequence input "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3ec03d3-fce9-44a1-9564-99050f363a77",
   "metadata": {},
   "source": [
    "## Section one"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d0c9859-c0f3-42a7-8313-d0518689bba9",
   "metadata": {},
   "source": [
    "In the first section of the code the data needs to be downloaded and sorted into sequences that are secreted by Sec, secreted by Tat or not secreted "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19ecc209-cae1-4e54-b35b-a14d1f4f2786",
   "metadata": {},
   "source": [
    "**Step one**: Read in protein sequences from the protein database, that have been filtered to contain a signal sequence (a feature of secreted proteins) and are present in *E. coli* (my organism of interest). This data should contain the entry and the sequence of the respective protieins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4f00aab1-54d4-47a9-8635-3170440699c0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Entry                                           Sequence\n",
      "0    P00634  MKQSTIALALLPLLFTPVTKARTPEMPVLENRAAQGDITAPGGARR...\n",
      "1    P00805  MEFFKKTALAALVMGFSGAALALPNITILATGGTIAGGGDSATKSN...\n",
      "2    P00811  MFKTTLCALLITASCSTFAAPQQINDIVHRTITPLIEQQKIPGMAV...\n",
      "3    P02925  MNMKKLATLVSAVALSATVSANAMAKDTIALVVSTLNNPFFVSLKD...\n",
      "4    P02930  MKKLLPILIGLSLSGFSSLSQAENLMQVYQQARLSNPELRKSAADR...\n",
      "..      ...                                                ...\n",
      "508  Q47702  MKKIICLVITLLMTLPVYAKLTAHEEARINAMLEGLAQKKDLIFVR...\n",
      "509  Q6BEX5  MKRFPLFLLFTLLTLSTVPAQADIIDDTIGNIQQAINDAYNPDRGR...\n",
      "510  Q9JMR4  MCPECFFLMLFFCGYRACYCSSSFSSSSSSSSSSSFRSSPAYGFSG...\n",
      "511  Q9JMR5  MCCVYRMNRPASGLTVVFCGKLSGKPGPKSAAWRMPWQKSGADDGG...\n",
      "512  Q9JMT5  MFNRRVLFLSVFSCAVFMLSGCSSNRFASRDANATYVNTQLKIIPR...\n",
      "\n",
      "[513 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df1 = pd.read_csv(\"https://raw.githubusercontent.com/DHavers/Python-Assignment/main/231215_ecoli_signalseq.csv\")\n",
    "print(df1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b7584e5-4b25-4ac0-94a6-f01478ff1df6",
   "metadata": {},
   "source": [
    "**Step two:** Create a column containing the first 30 amino acids (aa) - this is the signal sequence of the secreted proteins, so they can then be investigated to catagorise the proteins secretion system in Step three."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e039dca2-bc53-41ce-a0b9-dc6a79347b1e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Entry                                           Sequence  \\\n",
      "0    P00634  MKQSTIALALLPLLFTPVTKARTPEMPVLENRAAQGDITAPGGARR...   \n",
      "1    P00805  MEFFKKTALAALVMGFSGAALALPNITILATGGTIAGGGDSATKSN...   \n",
      "2    P00811  MFKTTLCALLITASCSTFAAPQQINDIVHRTITPLIEQQKIPGMAV...   \n",
      "3    P02925  MNMKKLATLVSAVALSATVSANAMAKDTIALVVSTLNNPFFVSLKD...   \n",
      "4    P02930  MKKLLPILIGLSLSGFSSLSQAENLMQVYQQARLSNPELRKSAADR...   \n",
      "..      ...                                                ...   \n",
      "508  Q47702  MKKIICLVITLLMTLPVYAKLTAHEEARINAMLEGLAQKKDLIFVR...   \n",
      "509  Q6BEX5  MKRFPLFLLFTLLTLSTVPAQADIIDDTIGNIQQAINDAYNPDRGR...   \n",
      "510  Q9JMR4  MCPECFFLMLFFCGYRACYCSSSFSSSSSSSSSSSFRSSPAYGFSG...   \n",
      "511  Q9JMR5  MCCVYRMNRPASGLTVVFCGKLSGKPGPKSAAWRMPWQKSGADDGG...   \n",
      "512  Q9JMT5  MFNRRVLFLSVFSCAVFMLSGCSSNRFASRDANATYVNTQLKIIPR...   \n",
      "\n",
      "                         Signal seq  \n",
      "0    MKQSTIALALLPLLFTPVTKARTPEMPVLE  \n",
      "1    MEFFKKTALAALVMGFSGAALALPNITILA  \n",
      "2    MFKTTLCALLITASCSTFAAPQQINDIVHR  \n",
      "3    MNMKKLATLVSAVALSATVSANAMAKDTIA  \n",
      "4    MKKLLPILIGLSLSGFSSLSQAENLMQVYQ  \n",
      "..                              ...  \n",
      "508  MKKIICLVITLLMTLPVYAKLTAHEEARIN  \n",
      "509  MKRFPLFLLFTLLTLSTVPAQADIIDDTIG  \n",
      "510  MCPECFFLMLFFCGYRACYCSSSFSSSSSS  \n",
      "511  MCCVYRMNRPASGLTVVFCGKLSGKPGPKS  \n",
      "512  MFNRRVLFLSVFSCAVFMLSGCSSNRFASR  \n",
      "\n",
      "[513 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "# I am defining a function to select the first 30aa in each sequence\n",
    "\n",
    "def signal_seq(sequence):\n",
    "    \"\"\"\n",
    "    Count the fist 30 amino acids in the given sequence.\n",
    "    \"\"\"\n",
    "    return sequence[:30] if len(sequence) >= 30 else sequence\n",
    "   \n",
    "signal_seq_list = []\n",
    "\n",
    "# I am adding the signal sequence of each protein into a new column on the dataframe\n",
    "\n",
    "for i in range(df1['Entry'].count()):\n",
    "    # print(df.loc[i,'Entry'])\n",
    "    signal_seq_list.append(signal_seq(df.loc[i,'Sequence']))\n",
    "\n",
    "df1['Signal seq'] = signal_seq_list\n",
    "\n",
    "\n",
    "print(df1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2beab634-4a4f-4103-a5dc-572b50d2210d",
   "metadata": {},
   "source": [
    "**Step three:** Search these signal sequences for the \"RR\" motif which is a known feature present in the signal sequences of protiens secreted by the Tat system. So if it is present the proteins secreteion system will be catagorised as tat and if that sequence motif isnt there catagorise as Sec (as these are the two secretion systems in *E.coli*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e7127bdd-461a-4cdc-9b4e-649abd47b0b1",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<function RR_motif at 0x12adcb7e0>\n",
      "      Entry                                           Sequence  \\\n",
      "0    P00634  MKQSTIALALLPLLFTPVTKARTPEMPVLENRAAQGDITAPGGARR...   \n",
      "1    P00805  MEFFKKTALAALVMGFSGAALALPNITILATGGTIAGGGDSATKSN...   \n",
      "2    P00811  MFKTTLCALLITASCSTFAAPQQINDIVHRTITPLIEQQKIPGMAV...   \n",
      "3    P02925  MNMKKLATLVSAVALSATVSANAMAKDTIALVVSTLNNPFFVSLKD...   \n",
      "4    P02930  MKKLLPILIGLSLSGFSSLSQAENLMQVYQQARLSNPELRKSAADR...   \n",
      "..      ...                                                ...   \n",
      "508  Q47702  MKKIICLVITLLMTLPVYAKLTAHEEARINAMLEGLAQKKDLIFVR...   \n",
      "509  Q6BEX5  MKRFPLFLLFTLLTLSTVPAQADIIDDTIGNIQQAINDAYNPDRGR...   \n",
      "510  Q9JMR4  MCPECFFLMLFFCGYRACYCSSSFSSSSSSSSSSSFRSSPAYGFSG...   \n",
      "511  Q9JMR5  MCCVYRMNRPASGLTVVFCGKLSGKPGPKSAAWRMPWQKSGADDGG...   \n",
      "512  Q9JMT5  MFNRRVLFLSVFSCAVFMLSGCSSNRFASRDANATYVNTQLKIIPR...   \n",
      "\n",
      "                         Signal seq Secretion system  \n",
      "0    MKQSTIALALLPLLFTPVTKARTPEMPVLE              sec  \n",
      "1    MEFFKKTALAALVMGFSGAALALPNITILA              sec  \n",
      "2    MFKTTLCALLITASCSTFAAPQQINDIVHR              sec  \n",
      "3    MNMKKLATLVSAVALSATVSANAMAKDTIA              sec  \n",
      "4    MKKLLPILIGLSLSGFSSLSQAENLMQVYQ              sec  \n",
      "..                              ...              ...  \n",
      "508  MKKIICLVITLLMTLPVYAKLTAHEEARIN              sec  \n",
      "509  MKRFPLFLLFTLLTLSTVPAQADIIDDTIG              sec  \n",
      "510  MCPECFFLMLFFCGYRACYCSSSFSSSSSS              sec  \n",
      "511  MCCVYRMNRPASGLTVVFCGKLSGKPGPKS              sec  \n",
      "512  MFNRRVLFLSVFSCAVFMLSGCSSNRFASR              tat  \n",
      "\n",
      "[513 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "# First, define a function that can count if \"RR\" is present in the singal sequence, and use this information to catagorise the secretion sysetm\n",
    "\n",
    "def RR_motif(signal_seq_list):\n",
    "    \"\"\"\n",
    "    Identify if \"RR\" is in the sequence \n",
    "    \"\"\"\n",
    "    if signal_seq_list.count(\"RR\") == 1:\n",
    "        return \"tat\"\n",
    "    else:\n",
    "        return \"sec\"\n",
    "    \n",
    "print(RR_motif)\n",
    "\n",
    "RR_motif_list = []\n",
    "\n",
    "# Create a new column in the data frame that will contain the information about the secretion system for each protein\n",
    "\n",
    "for i in range(df['Entry'].count()):\n",
    "    signal_sequence = df1.loc[i, 'Signal seq']\n",
    "    \n",
    "    system_label = RR_motif(signal_sequence)\n",
    "    \n",
    "    RR_motif_list.append(system_label)\n",
    "\n",
    "df1['Secretion system'] = RR_motif_list\n",
    "\n",
    "print(df1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07e7be60-585a-4fc9-97a2-b18ad2573563",
   "metadata": {},
   "source": [
    "**Step four:** Now an additional dataframe will be downloaded also from the protein database, this time filtered for *E.coli* proteins that do not contain signal sequences (and therefore are not secreted) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ca612ef4-e099-4866-8fdf-87f6e83f0f55",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Entry                                           Sequence\n",
      "0     A5A616                    MLGNMNVFMAVLGIILFSGFLAAYFSHKWDD\n",
      "1     O32583  MQILFNDQAMQCAAGQTVHELLEQLDQRQAGAALAINQQIVPREQW...\n",
      "2     P00350  MSKQQIGVVGMAVMGRNLALNIESRGYTVSIFNRSREKTEEVIAEN...\n",
      "3     P00363  MQTFQADLAIVGAGGAGLRAAIAAAQANPNAKIALISKVYPMRSHT...\n",
      "4     P00370  MDQTYSLESFLNHVQKRDPNQTEFAQAVREVMTTLWPFLEQNPKYR...\n",
      "...      ...                                                ...\n",
      "4585  Q9S4X4  MPFDLLTVLFTRLDVEVNGFNGGVLNGVPSAYHWYTEQYGVKGPCG...\n",
      "4586  Q9S4X5  MPNWCSNRMYFSGEPAQIAEIKRLASGAVTPLYRRATNEGIQLFLA...\n",
      "4587  Q9XB42  MKIISKRRAMTIYRQHPESRIFRYCTGKYQWHGSVCHYTGRDVPDI...\n",
      "4588  Q9Z3A0  MIRKNKWLRFQTVCRYIPLSLKNHNRLVIFVCQRIEWRYIFSTNTG...\n",
      "4589  V9HVX0  MTIAERLRQEGHQIGWQEGKLEGLHEQAIKIALRMLEQGFDRDQVL...\n",
      "\n",
      "[4590 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "df2 = pd.read_csv(\"https://raw.githubusercontent.com/DHavers/Python-Assignment/main/231215_all_ecoli_proteins.csv\")\n",
    "print(df2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89d713af-41cf-4f69-b75a-3b6f0a6e470f",
   "metadata": {},
   "source": [
    "**Step five:** Now these dataframes need to be combined into a single dataframe that does not contain any protein duplicates so that later in the code a single dataframe containing all the proteins can be used "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "fb00a03f-8d0c-4173-bde4-443f91aca8a2",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Entry</th>\n",
       "      <th>Sequence</th>\n",
       "      <th>Secretion system</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>P00634</td>\n",
       "      <td>MKQSTIALALLPLLFTPVTKARTPEMPVLENRAAQGDITAPGGARR...</td>\n",
       "      <td>sec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>P00805</td>\n",
       "      <td>MEFFKKTALAALVMGFSGAALALPNITILATGGTIAGGGDSATKSN...</td>\n",
       "      <td>sec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>P00811</td>\n",
       "      <td>MFKTTLCALLITASCSTFAAPQQINDIVHRTITPLIEQQKIPGMAV...</td>\n",
       "      <td>sec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>P02925</td>\n",
       "      <td>MNMKKLATLVSAVALSATVSANAMAKDTIALVVSTLNNPFFVSLKD...</td>\n",
       "      <td>sec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>P02930</td>\n",
       "      <td>MKKLLPILIGLSLSGFSSLSQAENLMQVYQQARLSNPELRKSAADR...</td>\n",
       "      <td>sec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4585</th>\n",
       "      <td>Q9S4X4</td>\n",
       "      <td>MPFDLLTVLFTRLDVEVNGFNGGVLNGVPSAYHWYTEQYGVKGPCG...</td>\n",
       "      <td>N/A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4586</th>\n",
       "      <td>Q9S4X5</td>\n",
       "      <td>MPNWCSNRMYFSGEPAQIAEIKRLASGAVTPLYRRATNEGIQLFLA...</td>\n",
       "      <td>N/A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4587</th>\n",
       "      <td>Q9XB42</td>\n",
       "      <td>MKIISKRRAMTIYRQHPESRIFRYCTGKYQWHGSVCHYTGRDVPDI...</td>\n",
       "      <td>N/A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4588</th>\n",
       "      <td>Q9Z3A0</td>\n",
       "      <td>MIRKNKWLRFQTVCRYIPLSLKNHNRLVIFVCQRIEWRYIFSTNTG...</td>\n",
       "      <td>N/A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4589</th>\n",
       "      <td>V9HVX0</td>\n",
       "      <td>MTIAERLRQEGHQIGWQEGKLEGLHEQAIKIALRMLEQGFDRDQVL...</td>\n",
       "      <td>N/A</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4590 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Entry                                           Sequence  \\\n",
       "0     P00634  MKQSTIALALLPLLFTPVTKARTPEMPVLENRAAQGDITAPGGARR...   \n",
       "1     P00805  MEFFKKTALAALVMGFSGAALALPNITILATGGTIAGGGDSATKSN...   \n",
       "2     P00811  MFKTTLCALLITASCSTFAAPQQINDIVHRTITPLIEQQKIPGMAV...   \n",
       "3     P02925  MNMKKLATLVSAVALSATVSANAMAKDTIALVVSTLNNPFFVSLKD...   \n",
       "4     P02930  MKKLLPILIGLSLSGFSSLSQAENLMQVYQQARLSNPELRKSAADR...   \n",
       "...      ...                                                ...   \n",
       "4585  Q9S4X4  MPFDLLTVLFTRLDVEVNGFNGGVLNGVPSAYHWYTEQYGVKGPCG...   \n",
       "4586  Q9S4X5  MPNWCSNRMYFSGEPAQIAEIKRLASGAVTPLYRRATNEGIQLFLA...   \n",
       "4587  Q9XB42  MKIISKRRAMTIYRQHPESRIFRYCTGKYQWHGSVCHYTGRDVPDI...   \n",
       "4588  Q9Z3A0  MIRKNKWLRFQTVCRYIPLSLKNHNRLVIFVCQRIEWRYIFSTNTG...   \n",
       "4589  V9HVX0  MTIAERLRQEGHQIGWQEGKLEGLHEQAIKIALRMLEQGFDRDQVL...   \n",
       "\n",
       "     Secretion system  \n",
       "0                 sec  \n",
       "1                 sec  \n",
       "2                 sec  \n",
       "3                 sec  \n",
       "4                 sec  \n",
       "...               ...  \n",
       "4585              N/A  \n",
       "4586              N/A  \n",
       "4587              N/A  \n",
       "4588              N/A  \n",
       "4589              N/A  \n",
       "\n",
       "[4590 rows x 3 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Merge dataframes on multiple columns ('sequence' and 'entry')\n",
    "merged_df = pd.merge(df1, df2, on=['Entry','Sequence'], how='outer', indicator=True)\n",
    "\n",
    "# Filter out the rows that have a match in both df and df2\n",
    "unique_rows = merged_df[merged_df['_merge'] == 'both'].drop(columns=['_merge'])\n",
    "\n",
    "# Change the \"NaN\" to \"N/A\" (for the proitens that are not secreted) so this can be used as a catagory later\n",
    "merged_df[\"Secretion system\"] = merged_df[\"Secretion system\"].fillna('N/A')\n",
    "\n",
    "# Tidy up what the dataframe looks like\n",
    "merged_df.drop(['Signal seq','_merge'], axis=1, inplace=True)\n",
    "df = merged_df\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a96c739-da4f-4bf1-a009-2253ac9756b7",
   "metadata": {},
   "source": [
    "Now I have a dataframe containing lots of *E. coli* protein sequences catagorised by their secretion system"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25b698e0-25ed-428e-b206-28e59c044782",
   "metadata": {},
   "source": [
    "# Section two:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7d05112-e841-4bb6-9430-01979b0daaa6",
   "metadata": {},
   "source": [
    "In the second section of this code we will investigate weather the amino acid composition of a protein may influence if and via what system the protein is secreted "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d05a969-11f0-45dc-bbc1-be9144987149",
   "metadata": {},
   "source": [
    "**Step one:** Investigate the proteins amino acid composition using libraries and newly defined functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "31597262-bbdf-46b9-92f5-228069691292",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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VF0WKN0ZVTty5Ii6du2q1atXq1WrVvL399f58+cVFRWlmTNnasGCBapUqZIGDRqkOXPmqGnTpho1apQCAwO1fPlyTZkyRX369LH8w3uRIkXUokULjRgxQoULF9bnn3+uqKgojR07VtmyZZOkVNfUq1cv+fr6qlatWipcuLBiYmI0evRo5cqVK8URyMQPm2PHjlXjxo3l7u6uSpUq2S/n+buMPj93Gz16tBo0aKB69erp5ZdflpeXl6ZMmaIff/xR8+fP/8cjVSdOnND333+vhIQEXbp0Sbt377ZfqvTBBx8oPDzcoiORgoKCNGrUKA0bNkxHjhxRo0aNlCdPHv3+++/64YcflD17do0cOTLFbaT2vS8tKlSoIEn69NNPlTNnTvn4+Cg4ONjpJYXSndBUrFgxNW/eXGXLllVCQoL27NmjDz74QDly5NCAAQPSfLyTJ09W8+bN9dhjj2nQoEEKCAjQiRMntHr1as2dOzfF+mvVqqXnnntO3bp1044dO1SnTh1lz55dZ8+e1ebNm1WxYkX16dNH0p3X/pIlSzR16lRVr15dbm5uyYba4cOHa9myZapXr57efPNN5c2bV3PnztXy5cv13nvvKVeuXGk6z8lJ7flMlDt3bj377LOaOnWqAgMDk3xP+M0339SpU6dUv359FStWTBcvXtSECRMcvm9csmRJ+fr6au7cuQoJCVGOHDlUpEgRFSlSRJ988okaN26shg0bqmvXripatKj++usvHTx4ULt27dIXX3xhyXHf7/sXYOeiiTSATC25mbbu5uw+V7dv3zbjxo2z39ckR44cpmzZsub55583v/zyi73f1q1bTWhoqMmWLZspUKCA6dmzp9m1a1eSmZIS7ytzt8QZqpLzxx9/GC8vL/PUU08l2+fChQvG19fXPjW3s5nEUqohLCzMlC9f3v48pdkC795m4jlOvI+RMXdmDHvttddMYGCg8fT0NIULFzZ9+vS5532uqlSpYgoWLGhu3ryZbJ/HHnvM5M+f397nwIED5plnnjH58uUzXl5eJiAgwHTt2vWe97n67LPPzCOPPGK8vLxM6dKlTWRkZKpvImzMnRnlZs+ebZ544gmTN29e4+HhYQoUKGAaN25s5s2b5zDj3/Hjx03Hjh1Nvnz5jKenpylTpox5//33k72P098l1v/FF184tDt7bSfed+jLL7805cuXN15eXiYoKCjJrFqprWn27NmmXr16xt/f33h5eZkiRYqYtm3bmn379iWp7+/n9+bNm6Znz56mQIECxmazObw+krvP1f2eH2Oc3z/obimtn3ifq+zZsxtfX1/z2GOPmW+++cahT2rfS+7eX+LD3d3dfo+6gQMHOkwTnuifzhaYaOnSpaZevXrGz8/PeHt7m8DAQNOmTRuzdu1ae5/k3guMSf17X+Lr7W5hYWFJ3k/Hjx9vgoODjbu7e7KzyCVauHCh6dixo3nkkUdMjhw5jKenpwkICDARERHmwIED93W8xtyZ9a9x48YmV65cxtvb25QsWdIMGjTIvjylc2qMMZGRkebRRx+1v05Klixpnn32WbNjxw57n7/++su0adPG5M6d2/7aT+Tsdbp//37TvHlzkytXLuPl5WUqV66c5Nwk9x7g7H3ambSeT2Pu3KJAkhkzZkySZcuWLTONGzc2RYsWNV5eXqZgwYKmSZMmZtOmTQ795s+fb8qWLWs8PT2THPvevXtN27ZtTcGCBY2np6cpVKiQeeKJJxzuRZnW1/7dr+nUvH8BKbEZY/G0QwCALCUoKEgVKlTQsmXLXF0KgCzspZde0tSpU3Xy5MlkRxiBBx2XBQIAAOC+ff/99zp8+LCmTJmi559/nmCFhxrhCgAAAPctNDRU2bJlU7NmzfT222+7uhzApbgsEAAAAAAswFTsAAAAAGABwhUAAAAAWIBwBQAAAAAWYEILJxISEnTmzBnlzJnzH98IEgAAAEDWZYzR5cuXVaRIEbm5pTw2Rbhy4syZMypevLirywAAAACQSZw8eVLFihVLsQ/hyomcOXNKunMC/fz8XFwNAAAAAFeJjY1V8eLF7RkhJYQrJxIvBfTz8yNcAQAAAEjV14WY0AIAAAAALEC4AgAAAAALEK4AAAAAwAJ85woAAAAPtfj4eN2+fdvVZcCFvLy87jnNemoQrgAAAPBQMsYoJiZGFy9edHUpcDE3NzcFBwfLy8vrH22HcAUAAICHUmKwKliwoLJly5aq2eDw4ElISNCZM2d09uxZBQQE/KPXAeEKAAAAD534+Hh7sMqXL5+ry4GLFShQQGfOnFFcXJw8PT3veztMaAEAAICHTuJ3rLJly+biSpAZJF4OGB8f/4+2Q7gCAADAQ4tLASFZ9zogXAEAAACABQhXAAAAQBY2a9Ys5c6d29VlQIQrAAAAwMG5c+f0/PPPKyAgQN7e3ipUqJAaNmyo6OhoV5emoKAgjR8/3qGtXbt2Onz4cLrv+8iRI+rQoYOKFCkiHx8fFStWTC1btrRs33Xr1tXAgQMt2ZarMFsgAAAA8DetW7fW7du3NXv2bJUoUUK///671q1bp7/++ivd9nnr1q37vseSr6+vfH19La7I0a1bt9SgQQOVLVtWS5YsUeHChXXq1CmtWLFCly5dStd9ZykGSVy6dMlIMpcuXXJ1KQAAAEgH169fNwcOHDDXr193aL9w4YKRZDZs2JDi+hcvXjS9evUyBQoUMDlz5jT16tUze/bscejz1VdfmerVqxtvb2+TL18+06pVK/uywMBA89Zbb5kuXboYPz8/8+yzzxpjjNmyZYupXbu28fHxMcWKFTMvvviiuXLlijHGmLCwMCPJ4WGMMTNnzjS5cuVy2PeUKVNMiRIljKenpyldurSZM2eOw3JJZvr06eapp54yvr6+plSpUuarr75K9nh3795tJJljx44l26devXqmX79+Dm3nz583Xl5eZt26dcYYYyZPnmxKlSplvL29TcGCBU3r1q2NMcZ06dIlybEdPXrUGGPMTz/9ZBo3bmyyZ89uChYsaDp37mz++OMP+z7CwsLMCy+8YAYMGGBy585tChYsaD755BNz5coV07VrV5MjRw5TokQJs2LFimRrT+71YEzasgGXBQIAAAD/X44cOZQjRw4tXbpUN2/edNrHGKOmTZsqJiZGK1as0M6dO1WtWjXVr1/fPrq1fPlyPf3002ratKl2796tdevWqUaNGg7bef/991WhQgXt3LlTb7zxhvbv36+GDRvq6aef1r59+7Rw4UJt3rxZL7zwgiRpyZIlKlasmEaNGqWzZ8/q7NmzTuv73//+pwEDBuill17Sjz/+qOeff17dunXT+vXrHfqNHDlSbdu21b59+9SkSRN16tQp2dG5AgUKyM3NTV9++WWy05X37NlT8+bNczhvc+fOVZEiRVSvXj3t2LFD/fv316hRo3To0CGtWrVKderUkSRNmDBBoaGh6tWrl/3YihcvrrNnzyosLExVqlTRjh07tGrVKv3+++9q27atw75nz56t/Pnz64cfftCLL76oPn366JlnnlHNmjW1a9cuNWzYUBEREbp27ZrT2i1zz/j1EGLkCgAA4MGW0kjFl19+afLkyWN8fHxMzZo1zdChQ83evXvty9etW2f8/PzMjRs3HNYrWbKk+eSTT4wxxoSGhppOnTolu//AwEDz1FNPObRFRESY5557zqFt06ZNxs3NzV5nYGCg+eijjxz63D1yVbNmTdOrVy+HPs8884xp0qSJ/bkk8/rrr9ufX7lyxdhsNrNy5cpka540aZLJli2bfaRu1KhR5rfffrMvv3HjhsmbN69ZuHChva1KlSpmxIgRxhhjFi9ebPz8/ExsbKzT7YeFhZkBAwY4tL3xxhsmPDzcoe3kyZNGkjl06JB9vccff9y+PC4uzmTPnt1ERETY286ePWskmejoaKf7ZuQKAAAASAetW7fWmTNn9PXXX6thw4basGGDqlWrplmzZkmSdu7cqStXrihfvnz2ka4cOXLo6NGj+u233yRJe/bsUf369VPcz90jWTt37tSsWbMcttmwYUMlJCTo6NGjqa7/4MGDqlWrlkNbrVq1dPDgQYe2SpUq2f+dPXt25cyZU+fOnUt2u/369VNMTIw+//xzhYaG6osvvlD58uUVFRUlSfL29lbnzp0VGRkp6c452Lt3r7p27SpJatCggQIDA1WiRAlFRERo7ty59xxJ2rlzp9avX+9wTsqWLStJ9nN997G4u7srX758qlixor3N399fklI8PiswoQUAAABwFx8fHzVo0EANGjTQm2++qZ49e2r48OHq2rWrEhISVLhwYW3YsCHJeolToqdmgons2bM7PE9ISNDzzz+v/v37J+kbEBCQpvrvvimuMSZJm6enZ5J1EhISUtxuzpw51aJFC7Vo0UJvv/22GjZsqLffflsNGjSQdOfSwCpVqujUqVOKjIxU/fr1FRgYaF93165d2rBhg9asWaM333xTI0aM0Pbt25OdSj4hIUHNmzfX2LFjkywrXLhwisfy97bEY7/X8f1TjFwBAAAA91CuXDldvXpVklStWjXFxMTIw8NDpUqVcnjkz59f0p2RlHXr1qVpH9WqVdNPP/2UZJulSpWyzyTo5eWV7HeeEoWEhGjz5s0ObVu3blVISEia6rkXm82msmXL2s+LJFWsWFE1atTQ9OnTNW/ePHXv3t1hHQ8PDz355JN67733tG/fPh07dkzffvutJOfHlnhOgoKCkpyTu8NpZsDIFQAgywgastxp+7ExTTO4EgAPqj///FPPPPOMunfvrkqVKilnzpzasWOH3nvvPbVs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si4AAAAAyFLSHK7OnTun9u3ba8OGDcqdO7eMMbp06ZLq1aunBQsWqECBAulRJwAAAABkamkOVy+++KJiY2P1008/KSQkRJJ04MABdenSRf3799f8+fMtLxJA5pbsTEc+GVwIAACAC6U5XK1atUpr1661BytJKleunCZPnqzw8HBLiwMAAACArCLNNxFOSEhIMv26JHl6eiohIcGSogAAAAAgq0lzuHriiSc0YMAAnTlzxt52+vRpDRo0SPXr17e0OAAAAADIKtIcriZNmqTLly8rKChIJUuWVKlSpRQcHKzLly/r448/To8aAQAAACDTS/N3rooXL65du3YpKipKP//8s4wxKleunJ588sn0qA8AAAAAsoT7vs9VgwYN1KBBAytrAQAAAIAsK1XhauLEiXruuefk4+OjiRMnpti3f//+lhQGAAAAAFlJqsLVRx99pE6dOsnHx0cfffRRsv1sNhvhCgAAAMBDKVXh6ujRo07/DQAAAAC4I82zBY4aNUrXrl1L0n79+nWNGjXKkqIAAAAAIKtJc7gaOXKkrly5kqT92rVrGjlypCVFAQAAAEBWk+bZAo0xstlsSdr37t2rvHnzWlIUAAAAkO5G5Eph2aWMqwMPjFSHqzx58shms8lms6l06dIOASs+Pl5XrlxR796906VIAAAAAMjsUh2uxo8fL2OMunfvrpEjRypXrv9L+l5eXgoKClJoaGi6FAkAAAAAmV2qw1WXLl0kScHBwapZs6Y8PT3TrSgAAAAAyGpSFa5iY2Pl5+cnSapataquX7+u69evO+2b2A8AAAAAHiapCld58uTR2bNnVbBgQeXOndvphBaJE13Ex8dbXiQAAAAAZHapClfffvutfSbA9evXp2tBAAAAAJJXcXZFp+37u+zP4Epwt1SFq7CwMKf/BgAAAADckeabCK9atUqbN2+2P588ebKqVKmijh076sKFC5YWBwAAAABZRZrD1SuvvKLY2FhJ0v79+zV48GA1adJER44c0eDBgy0vEAAAAACyglRPxZ7o6NGjKleunCRp8eLFat68ud59913t2rVLTZo0sbxAAAAAAMgK0jxy5eXlpWvXrkmS1q5dq/DwcElS3rx57SNaAAAAAPCwSfPI1eOPP67BgwerVq1a+uGHH7Rw4UJJ0uHDh1WsWDHLCwQAAACArCDNI1eTJk2Sh4eHvvzyS02d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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from Bio.SeqUtils import ProtParam\n",
    "\n",
    "# Define a function to calculate amino acid composition\n",
    "def calculate_amino_acid_composition(sequence):\n",
    "    analyser = ProtParam.ProteinAnalysis(str(sequence))\n",
    "    return analyser.get_amino_acids_percent()\n",
    "\n",
    "# Calculate amino acid composition for each sequence\n",
    "df['Amino Acid Composition'] = df['Sequence'].apply(calculate_amino_acid_composition)\n",
    "\n",
    "# Convert the 'Amino Acid Composition' column into a dataframe\n",
    "amino_acid_df = pd.DataFrame(df['Amino Acid Composition'].tolist(), index=df.index)\n",
    "\n",
    "# Combine the 'Secretion system' column with the amino acid composition dataframe\n",
    "combined_df = pd.concat([df['Secretion system'], amino_acid_df], axis=1)\n",
    "\n",
    "# Group by 'Secretion system' and calculate the mean composition for each group\n",
    "grouped_df = combined_df.groupby('Secretion system').mean()\n",
    "\n",
    "# Plot the composition of all amino acids for each secretion system\n",
    "grouped_df.T.plot(kind='bar', figsize=(10, 6))\n",
    "plt.xlabel('Amino Acid')\n",
    "plt.ylabel('Mean Composition')\n",
    "plt.title('Mean Amino Acid Composition for Different Secretion Systems')\n",
    "plt.legend(title='Secretion System')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "168e7ee2-40bb-4dcc-a2ce-ac493ba8a579",
   "metadata": {},
   "source": [
    "There appears to be some differences between the amino acid composition of the different catagories so next we can develop a model to use the amino acid composition of the sequence to predict the protein secretion system"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a448cb5-9e57-479d-a291-e50219e10209",
   "metadata": {},
   "source": [
    "**Step two:** Use this to create a model using a Random Forrest Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "c1e218df-156e-4a72-a049-d67fd7c96662",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.9146341463414634\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# Feature matrix X (amino acid composition) and target variable y (Secreted)\n",
    "X = pd.DataFrame(list(df['Amino Acid Composition']))\n",
    "y = df['Secretion system']\n",
    "\n",
    "# Split the data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y)\n",
    "\n",
    "# Train a RandomForest classifier\n",
    "classifier = RandomForestClassifier()\n",
    "classifier.fit(X_train, y_train)\n",
    "\n",
    "# Make predictions on the test set\n",
    "y_pred = classifier.predict(X_test)\n",
    "\n",
    "# Evaluate accuracy\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(f'Accuracy: {accuracy}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d646fd9-433c-473b-b366-b7f4b28314fe",
   "metadata": {},
   "source": [
    "**Step three:** Trying to understand what is important for this model to make its predictions "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "eef1d8d5-7566-47f6-a69f-0bba2894dbc5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA/IAAAInCAYAAAA75mIQAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABpRklEQVR4nO3deVxU9f7H8fcICO4LKIoLYt6UMs3QSo3cIVxaxNLKLZdCK1PylmsuXZfUjNxviXk1My1tlVTKNEvSVLRU1LqpmIKKGy4JAt/fH/2Y68igSOBw6vV8PM7j4XzP95z5nDNnRt5ntRljjAAAAAAAgCUUc3UBAAAAAAAg7wjyAAAAAABYCEEeAAAAAAALIcgDAAAAAGAhBHkAAAAAACyEIA8AAAAAgIUQ5AEAAAAAsBCCPAAAAAAAFkKQBwAAAADAQgjyAP62Fi5cKJvN5nQYOnRoobznnj17NHbsWB08eLBQ5v9nHDx4UDabTdOmTXN1Kfm2adMmjR07VmfOnHF1KQVm2bJluv3221WiRAnZbDbt2LGjUN8vISFBPXr0UO3ateXl5SUfHx/dddddeu6555Samlqo7/1nxMTEaOzYsU7H1apVS717976p9WS72evz4sWLGjt2rNavX1/g8/6zevfu7fA76+npqbp162rMmDG6dOlSob9/9m/cwoUL7W1jx46VzWa74Xm99957ioqKcjrOZrPlui0CQEFxd3UBAOBq77zzjurVq+fQ5ufnVyjvtWfPHo0bN04tW7ZUrVq1CuU9/s42bdqkcePGqXfv3ipfvryry/nTTpw4oR49euiBBx7QnDlz5OnpqVtvvbXQ3i8+Pl7NmzdXYGCgXnnlFdWqVUspKSnauXOn3n//fQ0dOlRly5YttPf/M2JiYjR79mynAeqjjz5ySd2uWJ8XL17UuHHjJEktW7Ys0HkXhBIlSmjdunWSpNOnT2vp0qUaP3689u7dq2XLlt30evr166cHHnjghqd77733tGvXLg0ePDjHuLi4OFWvXr0AqgOA3BHkAfzt1a9fX40bN3Z1GX/K5cuXZbPZ5O7+9/xZ//333+Xl5eXqMgrc/v37dfnyZXXv3l0tWrQokHlevHhRJUuWdDouKipKxYoV0/r161WmTBl7e5cuXfTqq6/KGFMgNeRF9mean6OlV2vUqFEBVHTjitL6LCqKFSume++91/46LCxMBw8e1PLlyzV9+nRVq1bN6XS///67SpQoUeD1VK9evcBD95XLBwCFhVPrAeA6li1bpqZNm6pUqVIqXbq0QkNDFR8f79Bn69at6tatm2rVqqUSJUqoVq1aevzxx3Xo0CF7n4ULF+rRRx+VJLVq1cp+emn2aZ65nf7bsmVLhyNr69evl81m0+LFi/Xiiy+qWrVq8vT01C+//CJJ+vLLL9WmTRuVLVtWJUuWVPPmzfXVV1/la9mzLz9Yt26d+vfvL29vb5UtW1Y9e/bUhQsXlJycrMcee0zly5dX1apVNXToUF2+fNk+ffaprFOmTNGECRNUs2ZNeXl5qXHjxk5r+vbbb9WmTRuVKVNGJUuWVLNmzbRq1SqnNa1du1Z9+vRRpUqVVLJkSQ0fPlz//Oc/JUkBAQH29Zt9ivGyZcsUEhKiqlWrqkSJEgoMDNSwYcN04cIFh/n37t1bpUuX1i+//KL27durdOnSqlGjhl588UWlpaU59E1LS9P48eMVGBgoLy8veXt7q1WrVtq0aZO9jzFGc+bM0Z133qkSJUqoQoUK6tKli3799ddrrvvevXvrvvvukyR17dpVNpvNYTv49NNP1bRpU5UsWVJlypRRu3btFBcX5zCP7NOGt2/fri5duqhChQq65ZZbcn3PkydPqmzZsipdurTT8VeH6rxua3v37tXjjz8uX19feXp6qmbNmurZs6d9feb2mWaPv953sHfv3po9e7a9xuwh+xIWZ9+txMREde/eXZUrV5anp6cCAwP1+uuvKysry97nystNpk+froCAAJUuXVpNmzbV999/n+t6vNH1+eqrr8rd3V2HDx/O0adPnz7y9va2n3q+bt06tWzZUt7e3ipRooRq1qyp8PBwXbx4UQcPHlSlSpUkSePGjbOvhyuX/eeff9YTTzzhsNzZ6y5b9m/Me++9p5dffllVq1ZV6dKl1alTJx07dkznzp3T008/LR8fH/n4+Oipp57S+fPnr7s+cpMdfLN/L2vVqqWOHTtq5cqVatSokby8vOxnGSQnJ+uZZ55R9erVVbx4cQUEBGjcuHHKyMhwmOfRo0f12GOPqUyZMipXrpy6du2q5OTkHO+d26n17733npo2barSpUurdOnSuvPOOxUdHS3pj9/kVatW6dChQw7bWzZnp9bv2rVLDz30kCpUqCAvLy/deeed+s9//uPQJ3u9L126VCNHjpSfn5/Kli2rtm3bat++fTe4VgH81RHkAfztZWZmKiMjw2HINnHiRD3++OO67bbbtHz5ci1evFjnzp1TcHCw9uzZY+938OBB1a1bV1FRUVqzZo1ee+01JSUlqUmTJkpJSZEkdejQQRMnTpQkzZ49W3FxcYqLi1OHDh3yVffw4cOVmJioefPm6bPPPlPlypX17rvvKiQkRGXLltV//vMfLV++XBUrVlRoaGi+w7z0x+mn5cqV0/vvv69Ro0bpvffeU//+/dWhQwc1bNhQH374oXr16qXXX39dM2fOzDH9rFmztHr1akVFRendd99VsWLFFBYW5hA8N2zYoNatW+vs2bOKjo7W0qVLVaZMGXXq1MnpKbd9+vSRh4eHFi9erA8//FADBgzQ888/L0lauXKlff3eddddkv4IMO3bt1d0dLRWr16twYMHa/ny5erUqVOOeV++fFkPPvig2rRpo08++UR9+vTRG2+8oddee83eJyMjQ2FhYXr11VfVsWNHffTRR1q4cKGaNWumxMREe79nnnlGgwcPVtu2bfXxxx9rzpw52r17t5o1a6Zjx47lus5Hjx5tD1gTJ05UXFyc5syZI+mPkPHQQw+pbNmyWrp0qaKjo3X69Gm1bNlS3377bY55de7cWXXq1NEHH3ygefPm5fqeTZs2VVJSkp588klt2LBBv//+e65987qt7dy5U02aNNH333+v8ePH64svvtCkSZOUlpam9PR0h3le/Zl6eHjk6Ts4evRodenSRZLsn3tcXJyqVq3qtPYTJ06oWbNmWrt2rV599VV9+umnatu2rYYOHarnnnsuR//Zs2crNjZWUVFRWrJkiS5cuKD27dvr7Nmzua6fG1mfzzzzjNzd3fXvf//bof3UqVN6//331bdvX3l5eengwYPq0KGDihcvrgULFmj16tWaPHmySpUqpfT0dFWtWlWrV6+WJPXt29e+HkaPHi3pj0t7mjRpol27dun111/X559/rg4dOmjQoEH2oHylESNG6Pjx41q4cKFef/11rV+/Xo8//rjCw8NVrlw5LV26VC+99JIWL16sESNGXHNdXEv2TsjsnRCStH37dv3zn//UoEGDtHr1aoWHhys5OVl333231qxZo1deeUVffPGF+vbtq0mTJql///72aX///Xe1bdtWa9eu1aRJk/TBBx+oSpUq6tq1a57qeeWVV/Tkk0/Kz89PCxcu1EcffaRevXrZdzTMmTNHzZs3V5UqVRy2t9zs27dPzZo10+7duzVjxgytXLlSt912m3r37q0pU6bk6D9ixAgdOnRI8+fP11tvvaWff/5ZnTp1UmZmZp7qB/A3YQDgb+qdd94xkpwOly9fNomJicbd3d08//zzDtOdO3fOVKlSxTz22GO5zjsjI8OcP3/elCpVyrz55pv29g8++MBIMl9//XWOafz9/U2vXr1ytLdo0cK0aNHC/vrrr782ksz999/v0O/ChQumYsWKplOnTg7tmZmZpmHDhubuu+++xtow5sCBA0aSmTp1qr0tex1dvQ4efvhhI8lMnz7dof3OO+80d911V455+vn5md9//93enpqaaipWrGjatm1rb7v33ntN5cqVzblz5+xtGRkZpn79+qZ69eomKyvLoaaePXvmWIapU6caSebAgQPXXNasrCxz+fJls2HDBiPJ7Ny50z6uV69eRpJZvny5wzTt27c3devWtb9etGiRkWTefvvtXN8nLi7OSDKvv/66Q/vhw4dNiRIlzEsvvXTNOrM/6w8++MDelpmZafz8/Mwdd9xhMjMz7e3nzp0zlStXNs2aNbO3jRkzxkgyr7zyyjXfJ9ulS5fsn60k4+bmZho1amRGjhxpjh8/bu93I9ta69atTfny5R2mv1pun+mNfAefffZZk9ufNVd/t4YNG2Ykmc2bNzv0GzBggLHZbGbfvn3GmP9tv3fccYfJyMiw99uyZYuRZJYuXZrrMhmT9/VpzB/bXeXKlU1aWpq97bXXXjPFihWzb88ffvihkWR27NiR63ueOHHCSDJjxozJMS40NNRUr17dnD171qH9ueeeM15eXubUqVPGmP9td1d/voMHDzaSzKBBgxzaH374YVOxYsVrrovsZSxVqpS5fPmyuXz5sjlx4oR58803jc1mM02aNLH38/f3N25ubvbPIdszzzxjSpcubQ4dOuTQPm3aNCPJ7N692xhjzNy5c40k88knnzj069+/v5Fk3nnnHXtb9nck26+//mrc3NzMk08+ec1l6dChg/H393c67ur1361bN+Pp6WkSExMd+oWFhZmSJUuaM2fOGGP+t97bt2/v0G/58uVGkomLi7tmTQD+XjgiD+Bvb9GiRfrhhx8cBnd3d61Zs0YZGRnq2bOnw9F6Ly8vtWjRwuGu0OfPn9fLL7+sOnXqyN3dXe7u7ipdurQuXLighISEQqk7PDzc4fWmTZt06tQp9erVy6HerKwsPfDAA/rhhx9ynEaeVx07dnR4HRgYKEk5ziYIDAx0uJwgW+fOnR2uYc8+0v7NN98oMzNTFy5c0ObNm9WlSxeH05Dd3NzUo0cP/fbbbzlOLb16+a/n119/1RNPPKEqVarIzc1NHh4e9uvOr/6MbDZbjiP1DRo0cFi2L774Ql5eXurTp0+u7/n555/LZrOpe/fuDp9JlSpV1LBhw3zdWXzfvn06evSoevTooWLF/vffeOnSpRUeHq7vv/9eFy9edJgmr+vK09NTH330kfbs2aM33nhD3bp104kTJzRhwgQFBgbaP4O8bmsXL17Uhg0b9Nhjjzkcbc3N1XXeyHfwRqxbt0633Xab7r77bof23r17yxhjvxlbtg4dOsjNzc3+ukGDBpLkdFu/Ul7XpyS98MILOn78uD744ANJUlZWlubOnasOHTrYb4x55513qnjx4nr66af1n//857qXZ1zp0qVL+uqrr/TII4+oZMmSDuuzffv2unTpUo7LBW7ke3/q1Kk8nV5/4cIFeXh4yMPDQ5UqVdLgwYMVFhamjz76yKFfgwYNctzY8fPPP1erVq3k5+fnUH9YWJikP87qkaSvv/5aZcqU0YMPPugw/RNPPHHd+mJjY5WZmalnn332un3zat26dWrTpo1q1Kjh0N67d29dvHgxx9H8q+vO6/YG4O/l73lXJAC4QmBgoNOb3WWf9tykSROn010Zop544gl99dVXGj16tJo0aaKyZcvKZrOpffv21zw9+c+4+rTh7HqzTzF25tSpUypVqtQNv1fFihUdXhcvXjzXdmePkapSpYrTtvT0dJ0/f17nzp2TMcbpqdDZTxA4efKkQ3tup007c/78eQUHB8vLy0v/+te/dOutt6pkyZI6fPiwOnfunOMzKlmyZI6b53l6ejos24kTJ+Tn5+ewHVzt2LFjMsbI19fX6fjatWvneRmyZa+H3NZVVlaWTp8+7XBDuxtZV9If34ns0GaMUVRUlCIjIzV69GgtX748z9tasWLFlJmZmeebieW2TeflO3gjTp486fSpEblta97e3g6vPT09JSnP3+3rrU/pjxvyBQcHa/bs2XryySf1+eef6+DBgw6n299yyy368ssvNWXKFD377LO6cOGCateu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x44dzb333pvj8gtX1ZO9I6dfv36mUqVKZsWKFebYsWPmm2++MW+99ZapW7eu8fPzM/fee2+RuV7WGMcwP2TIEFeX45SzMJ+Wlmaee+454+bmZuLj411b4P9LTEw0W7duNSdOnHBoz8zMNI8++qgZNWqUw2+Cq+zdu9eEhYWZ0qVLG29vbxMREWFCQ0NNWFiY6dKli3nkkUdMx44dzY8//uiyGq/8zK8M81euu5YtW5onnnjCFeU5SE1NNZUqVTITJkzIMS673lGjRpnbb7/dXL58OcelAjfT4cOHTeXKlc2DDz5oDh486LTPiy++aB599FGX73T87bffnNZ65Tbw4osvmmHDhrnsO3Xw4EHTuHFj07RpUxMUFGT69etn/P39zbx588yyZctMx44d7Tt4du/ebdq2bWs6depkzp4965J6s33wwQemadOmJiMjw/Tt29f4+vqaXbt2GWOM+eWXX8zs2bNdfuDhStl/h2RmZpr333/ftGrVytx77705fmtdaf/+/SYsLMy0aNHCVKhQwQwePNg+rij+HfXLL7+YkJAQExYWlutvrCv9+OOP5umnnzYBAQGmZs2a5sUXXzQ//vij2bp1q6levbr5+OOPjTGuW7dXny2wfv1688ADD5iYmBjz+++/m1mzZpny5cubqVOnmtDQUFO+fHmzY8cOl9RalBDk/2b27t1rQkNDTbt27cyWLVvs7adPnzaLFi0yI0eONHfddVeRuZnIlT+M2acqGvNHiPfy8jJbt251YXX/k9ve2Ct/EPft22d+/fVXV5SXJwkJCaZLly7m0KFDri7FGOO4TqdOnZpj/Llz58ymTZvMf//7XxdUd21nz541b7/9trHZbGbYsGGuLsepK4Pd119/bV566SVTokSJIvPdz01aWpoZNWqU8fPzM/v373d1OXY///yz6dChg2nXrp1LA/u15HY2RmZmpjl8+LAJCwszCxcuNMa49o/Pc+fOmcaNG5tmzZqZX375xd5+5U6bZ5991vTr1y/HJQKu8OGHH5rixYubHj16OIS1s2fPmn/+85+mQoUK9lDnaitWrDCenp45ar1w4YIZPny48ff3tx8Bd5X9+/ebzp07m4cfftisXLnSfPzxx6Zly5bm4YcfNjabzdx99932Mwb27t3r8ksWst1///2mWLFixs/PzxIBI/u7lJWVZf7zn/+YsLCwIvP/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RhMmTNDWrVtVtWpVzZkz53qrEQAASyHIAwBgYdHR0erevbsk6YEHHtD58+f11Vdf5ej3r3/9S82bN1ejRo3Ut29fbdiwQXPnzlWjRo0UHBysLl266Ouvv77me7Vv314DBw5UnTp19PLLL8vHx0fr16+XJC1ZskS///67Fi1apPr166t169aaNWuWFi9erGPHjuU6zy+//FIXL15UaGioJKl79+4Op9d/+eWX2rJli1auXKl27dqpdu3a6tixo8LCwpzOLyoqSn369FG/fv1Ut25d/etf/9Jtt912zeUCAMBqCPIAAFjUvn37tGXLFnXr1k2S5O7urq5du2rBggU5+jZo0MD+b19fX5UsWVK1a9d2aDt+/Pg13+/KedhsNlWpUsU+TUJCgho2bKhSpUrZ+zRv3lxZWVnat29frvOMjo5W165d5e7uLkl6/PHHtXnzZvs0O3bsUPXq1XXrrbdes7ZsCQkJatq0qUPb1a8BALA6d1cXAAAA8ic6OloZGRmqVq2avc0YIw8PD50+fVoVKlSwt3t4eNj/bbPZHF5nt2VlZV3z/a41jTFGNpvN6XS5tZ86dUoff/yxLl++rLlz59rbMzMztWDBAr322msqUaLENWsCAODviCPyAABYUEZGhhYtWqTXX39dO3bssA87d+6Uv7+/lixZclPrue2227Rjxw6HG9V99913KlasWK5H05csWaLq1atr586dDssQFRWl//znP8rIyFCDBg3022+/5fkRc4GBgTkeYXejj7QDAKCoI8gDAGBBn3/+uU6fPq2+ffuqfv36DkOXLl1u+DFuf9aTTz4pLy8v9erVS7t27dLXX3+t559/Xj169JCvr6/TaaKjo9WlS5cc9ffp00dnzpzRqlWr1KJFC91///0KDw9XbGysDhw4oC+++EKrV692Os8XXnhBCxYs0IIFC7R//36NGTNGu3fvLsxFBwDgpiPIAwBgQdHR0Wrbtq3KlSuXY1x4eLh27Nih7du337R6SpYsqTVr1ujUqVNq0qSJunTpojZt2mjWrFlO+2/btk07d+5UeHh4jnFlypRRSEiIfWfEihUr1KRJEz3++OO67bbb9NJLLykzM9PpfLt27apXXnlFL7/8soKCgnTo0CENGDCg4BYUAIAiwGacPaMGAAAAAAAUSRyRBwAAAADAQgjyAAAAAABYCEEeAAAAAAALIcgDAAAAAGAhBHkAAAAAACyEIA8AAAAAgIUQ5AEAAAAAsBCCPAAAAAAAFkKQBwAAAADAQgjyAAAAAABYCEEeAAAAAAALIcgDAAAAAGAh/wfJ/AfH/fHfbgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Train a RandomForest classifier\n",
    "classifier = RandomForestClassifier()\n",
    "classifier.fit(X_train, y_train)\n",
    "\n",
    "# Get feature importances\n",
    "feature_importances = classifier.feature_importances_\n",
    "\n",
    "# Create a dataframe to display feature importances\n",
    "importance_df = pd.DataFrame({'Amino Acid': amino_acid_df.columns, 'Importance': feature_importances})\n",
    "\n",
    "# Sort the dataframe by importance in descending order\n",
    "importance_df = importance_df.sort_values(by='Importance', ascending=False)\n",
    "\n",
    "# Plot the feature importances\n",
    "plt.figure(figsize=(12, 6))\n",
    "plt.bar(importance_df['Amino Acid'], importance_df['Importance'])\n",
    "plt.xlabel('Amino Acid')\n",
    "plt.ylabel('Importance')\n",
    "plt.title('Feature Importance for Secretion System Prediction')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae9a2c61-c9a8-40ae-8395-4eb87d334d45",
   "metadata": {},
   "source": [
    "**Step four:** To understand this representation more intuitivly it would be good to visully represent certain catagorise of amino acids"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "0baab740-7e2d-4ee4-bf5e-01252e416bf3",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positively charged Amino Acids (K, R, H): Lysine, Arginine, Histidine\n",
      "Negatively charged Amino Acids (D, E): Aspartic Acid, Glutamic Acid\n",
      "Uncharged Amino Acids (S, T, N, Q): Serine, Threonine, Asparagine, Glutamine\n",
      "Hydrophobic Amino Acids (A, V, L, I, M, F, W, Y): Alanine, Valine, Leucine, Isoleucine, Methionine, Phenylalanine, Tryptophan, Tyrosine\n",
      "Special cases Amino Acids (C, G, P): Cysteine, Glycine, Proline\n"
     ]
    }
   ],
   "source": [
    "# Create a dictionary of amino acid categories with one-letter codes\n",
    "amino_acid_categories = {\n",
    "    'Positively charged': ['K', 'R', 'H'],\n",
    "    'Negatively charged': ['D', 'E'],\n",
    "    'Uncharged': ['S', 'T', 'N', 'Q'],\n",
    "    'Hydrophobic': ['A', 'V', 'L', 'I', 'M', 'F', 'W', 'Y'],\n",
    "    'Special cases': ['C', 'G', 'P'],\n",
    "}\n",
    "\n",
    "# Mapping of one-letter codes to full names\n",
    "amino_acid_names = {\n",
    "    'S': 'Serine', 'T': 'Threonine', 'Y': 'Tyrosine', 'N': 'Asparagine', 'Q': 'Glutamine',\n",
    "    'A': 'Alanine', 'V': 'Valine', 'L': 'Leucine', 'I': 'Isoleucine', 'M': 'Methionine',\n",
    "    'D': 'Aspartic Acid', 'E': 'Glutamic Acid',\n",
    "    'K': 'Lysine', 'R': 'Arginine', 'H': 'Histidine',\n",
    "    'F': 'Phenylalanine', 'W': 'Tryptophan',\n",
    "    'C': 'Cysteine', 'G': 'Glycine', 'P': 'Proline',\n",
    "}\n",
    "\n",
    "# Print the amino acid categories\n",
    "for category, amino_acids in amino_acid_categories.items():\n",
    "    full_names = [amino_acid_names[code] for code in amino_acids]\n",
    "    print(f'{category} Amino Acids ({\", \".join(amino_acids)}): {\", \".join(full_names)}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "c3651ace-1383-4fd9-a436-cace6b5811d5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA/IAAAInCAYAAAA75mIQAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAACS4klEQVR4nOzdd3xO9///8eclexAkVkiIWqlRJNqiMTooqrTaomqUUOuTWjVrV9UoKSXa2mq2RVVTo5QaoUW0VlENUZISe1Tm+f3hl+vrkoSIJFeuetxvt+t2c73P+5zzOue6kvaZ8z7vYzIMwxAAAAAAALAJ+axdAAAAAAAAyDyCPAAAAAAANoQgDwAAAACADSHIAwAAAABgQwjyAAAAAADYEII8AAAAAAA2hCAPAAAAAIANIcgDAAAAAGBDCPIAAAAAANgQgjyAR9b8+fNlMpnSfQ0YMCBH9nn48GGNGjVKJ0+ezJHtP4yTJ0/KZDJp8uTJ1i4ly3bu3KlRo0bp8uXL1i4l2yxfvlyVK1eWi4uLTCaT9u/fn6P7O3LkiNq3b6+yZcvK2dlZXl5eqlmzpnr37q2rV6/m6L4fRnh4uEaNGpXusjJlyqhTp065Wk+q3D6fN2/e1KhRo7Rly5Zs3/bD6tSpk8XvWScnJ1WsWFEjR47UrVu3cnz/qb/j5s+fb24bNWqUTCbTA29ryZIlCg0NTXeZyWTK8LsIANnF3toFAIC1zZs3T5UqVbJo8/b2zpF9HT58WKNHj1aDBg1UpkyZHNnHo2znzp0aPXq0OnXqpIIFC1q7nId2/vx5tW/fXi+++KJmzpwpJycnVahQIcf2FxkZqbp168rf318jRoxQmTJlFBcXp99++03Lli3TgAEDVKBAgRzb/8MIDw/XjBkz0g1Qq1atskrd1jifN2/e1OjRoyVJDRo0yNZtZwcXFxdt3rxZknTp0iUtXbpUY8aM0R9//KHly5fnej3BwcF68cUXH3i9JUuW6ODBg+rTp0+aZRERESpVqlQ2VAcAGSPIA3jkValSRYGBgdYu46EkJibKZDLJ3v7R/LX+77//ytnZ2dplZLtjx44pMTFRb731lurXr58t27x586ZcXV3TXRYaGqp8+fJpy5Ytyp8/v7n9tdde09ixY2UYRrbUkBmpn2lWrpberUaNGtlQ0YPLS+czr8iXL5+efvpp8/smTZro5MmTWrFihaZMmaKSJUumu96///4rFxeXbK+nVKlS2R667zw+AMgpDK0HgPtYvny5ateuLTc3N7m7u6tx48aKjIy06LNnzx61adNGZcqUkYuLi8qUKaO2bdvq1KlT5j7z58/X66+/Lklq2LCheXhp6jDPjIb/NmjQwOLK2pYtW2QymbRo0SL1799fJUuWlJOTk/78809J0o8//qjnnntOBQoUkKurq+rWratNmzZl6dhTbz/YvHmzunbtKk9PTxUoUEAdOnTQjRs3FBsbqzfeeEMFCxZUiRIlNGDAACUmJprXTx3KOnHiRI0bN06+vr5ydnZWYGBgujVt375dzz33nPLnzy9XV1fVqVNH33//fbo1bdiwQZ07d1aRIkXk6uqqIUOG6L333pMk+fn5mc9v6hDj5cuXq1GjRipRooRcXFzk7++vwYMH68aNGxbb79Spk9zd3fXnn3+qadOmcnd3l4+Pj/r376/4+HiLvvHx8RozZoz8/f3l7OwsT09PNWzYUDt37jT3MQxDM2fOVPXq1eXi4qJChQrptdde019//XXPc9+pUyc988wzkqTWrVvLZDJZfA/WrFmj2rVry9XVVfnz59cLL7ygiIgIi22kDhvet2+fXnvtNRUqVEiPPfZYhvu8cOGCChQoIHd393SX3x2qM/td++OPP9S2bVsVK1ZMTk5O8vX1VYcOHcznM6PPNHX5/X4GO3XqpBkzZphrTH2l3sKS3s9WdHS03nrrLRUtWlROTk7y9/fXxx9/rJSUFHOfO283mTJlivz8/OTu7q7atWtr165dGZ7HBz2fY8eOlb29vU6fPp2mT+fOneXp6Wkeer5582Y1aNBAnp6ecnFxka+vr1q1aqWbN2/q5MmTKlKkiCRp9OjR5vNw57EfP35cb775psVxp567VKm/Y5YsWaJBgwapRIkScnd3V/PmzfXPP//o2rVr6tatm7y8vOTl5aW3335b169fv+/5yEhq8E39fVmmTBm99NJLWrlypWrUqCFnZ2fzKIPY2Fi98847KlWqlBwdHeXn56fRo0crKSnJYptnz57VG2+8ofz588vDw0OtW7dWbGxsmn1nNLR+yZIlql27ttzd3eXu7q7q1atrzpw5km7/Tv7+++916tQpi+9bqvSG1h88eFAtWrRQoUKF5OzsrOrVq2vBggUWfVLP+9KlSzVs2DB5e3urQIECev75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8+ZJkgzD0MSJE1W2bFm5uLjoiSee0Ndff53ucd24cUMFChRIs/y7776Tm5ubrl27lu56KSkpmjBhgsqVKycnJyf5+vpq3LhxFn3++usvNWzYUK6urnriiScUERFhXnbhwgW1bdtWpUqVkqurq6pWraqlS5darN+gQQP17t1b/fr1k5eXl1544QVJ0po1a1S+fHm5uLioYcOGWrBggUwmk8VIhvt9XufOnVPz5s3Nn9fixYvTPc7sZrUgn5CQoL1796pRo0YW7Y0aNdLOnTvTXSciIiJN/8aNG2vPnj1KTEyUJD3zzDPau3evfvnlF0m3P/Tw8HA1a9Ysw1ri4+N19epVixcAAAAAZJadnZ0+/PBDTZ8+XX///Xe6fQ4cOKDGjRvr1Vdf1e+//67ly5dr+/bt6t27t7lPhw4ddPbsWW3ZskXffPONPv/8c507d85iO/ny5dO0adN08OBBLViwQJs3b9bAgQMlSXXq1FFoaKgKFCigmJgYxcTEaMCAAWlqadeundasWWP+A4AkrV+/Xjdu3FCrVq0kSe+//77mzZunsLAwHTp0SH379tVbb72lrVu3ptmem5ub2rRpY/4jQKp58+bptddeU/78+dM9J0OGDNGECRM0fPhwHT58WEuWLFGxYsUs+gwbNkwDBgzQ/v37VaFCBbVt21ZJSUmSpFu3bikgIEBr167VwYMH1a1bN7Vv3167d++22MaCBQtkb2+vHTt26LPPPtPJkyf12muvqWXLltq/f7/eeecdDRs27IE/r06dOunkyZPavHmzvv76a82cOTPN55UTrHaPfFxcnJKTk9N8SMWKFVNsbGy668TGxqbbPykpSXFxcSpRooTatGmj8+fP65lnnpFhGEpKSlKPHj0s7lW52/jx4zV69OiHPygAAAAAj6xXXnlF1atX18iRIzVnzpw0yydNmqQ333zTPAla+fLlNW3aNNWvX19hYWE6efKkfvzxR/36668KDAyUJM2ePVvly5e32M6dk6j5+flp7Nix6tGjh2bOnClHR0d5eHjIZDKpePHiGdbauHFjubm5adWqVWrfvr0kacmSJWrevLkKFCigGzduaMqUKdq8ebNq164tSSpbtqy2b9+uzz77TPXr10+zzeDgYNWpU0dnz56Vt7e34uLitHbtWm3cuDHdGq5du6ZPPvlEn376qTp27ChJeuyxx/TMM89Y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3XffNW+zVq1aGdb2/vvvm/9dpkwZ9e/fX8uXL9fAgQMzdWwzZsyQh4eHli1bZn7cd4UKFczLn332WYv+n332mQoVKqStW7fqpZdeUnR0tIoXL67nn39eDg4O8vX11ZNPPilJOnHihJYuXaq///5b3t7ekqQBAwZo3bp1mjdvnj788ENFR0erVatW5vBftmzZTNX9KOCKPAAAAAA8hFatWuns2bNas2aNGjdurC1btqhmzZppJu++e+K72rVrm6/I7927V3/++afy589vvspfuHBh3bp1SydOnNC5c+d09uxZPffcc5mu6+uvv9Yzzzyj4sWLy93dXcOHD7d4Ktj97N+/X0FBQeYQf7dz586pe/fuqlChgjw8POTh4aHr16+b9/H666/r33//VdmyZdW1a1etWrXKfDV/3759MgxDFSpUMB+vu7u7tm7dah66HxISog8++EB169bVyJEj9fvvv2e69v86gjwAAAAAPCRnZ2e98MILGjFihHbu3KlOnTpp5MiR910v9ep7SkqKAgICtH//fovXsWPH9Oabb8rFxeWB6tm1a5fatGmjJk2aaO3atYqMjNSwYcPMw/Qz43777NSpk/bu3avQ0FDt3LlT+/fvl6enp3kfPj4+Onr0qGbMmCEXFxf17NlT9erVU2JiolJSUmRnZ6e9e/daHO+RI0f0ySefSJKCg4P1119/qX379jpw4IACAwM1ffr0BzoP/1UEeQAAAADIZo8//rhu3Lhh0bZr16407ytVqiRJqlmzpo4fP66iRYuqXLlyFi8PDw/lz59fZcqU0aZNmzK1/x07dqh06dIaNmyYAgMDVb58eZ06deqBjqFatWratm1bhhPkbdu2TSEhIWratKl5Ar64uDiLPi4uLnr55Zc1bdo0bdmyRRERETpw4IBq1Kih5ORknTt3Ls3x3jn7vo+Pj7p3766VK1eqf//++uKLLx7oGP6rCPIAAAAAkEUXLlzQs88+qy+//FK///67oqKi9NVXX2nixIlq0aKFRd+vvvpKc+fO1bFjxzRy5Ej98ssv5lnn27VrJy8vL7Vo0ULbtm1TVFSUtm7dqnfffVd///23pNszwH/88ceaNm2ajh8/rn379mV4hbpcuXKKjo7WsmXLdOLECU2bNk2rVq16oGPr3bu3rl69qjZt2mjPnj06fvy4Fi1apKNHj5r3sWjRIh05ckS7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",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "# Assign colours to each amino acid category\n",
    "category_colours = {\n",
    "    'Positively charged': 'blue',\n",
    "    'Negatively charged': 'red',\n",
    "    'Uncharged': 'green',\n",
    "    'Hydrophobic': 'purple',\n",
    "    'Special cases': 'orange',\n",
    "}\n",
    "\n",
    "# Use the same code as in section two\n",
    "classifier = RandomForestClassifier()\n",
    "classifier.fit(X_train, y_train)\n",
    "\n",
    "feature_importances = classifier.feature_importances_\n",
    "\n",
    "importance_df = pd.DataFrame({'Amino Acid': amino_acid_df.columns, 'Importance': feature_importances})\n",
    "\n",
    "# Then map amino acids to their categories\n",
    "importance_df['Category'] = importance_df['Amino Acid'].apply(\n",
    "    lambda amino_acid: next(category for category, acids in amino_acid_categories.items() if amino_acid in acids)\n",
    ")\n",
    "\n",
    "# And then map categories to colours\n",
    "importance_df['Colour'] = importance_df['Category'].map(category_colours)\n",
    "\n",
    "# Sort the dataframe by importance in descending order\n",
    "importance_df = importance_df.sort_values(by='Importance', ascending=False)\n",
    "\n",
    "# Plot the feature importances with coloured bars\n",
    "plt.figure(figsize=(12, 6))\n",
    "bars = plt.bar(importance_df['Amino Acid'], importance_df['Importance'], color=importance_df['Colour'])\n",
    "\n",
    "# Add legend\n",
    "legend_labels = [(category, colour) for category, colour in category_colours.items()]\n",
    "plt.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=colour, label=label) for label, colour in legend_labels], loc='upper right')\n",
    "\n",
    "plt.xlabel('Amino Acid')\n",
    "plt.ylabel('Importance')\n",
    "plt.title('Feature Importance for Secretion System Prediction')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e654b0c-524c-46f9-8d82-263ccfb0352c",
   "metadata": {},
   "source": [
    "This suggests hydrophobic amino acids are not very important when making these predicrions, and therefore suggesting they are not very improtant in determining a protiens secretion system, along with the special case amino acids. \n",
    "\n",
    "This will be useful when designing protein constructs to use in the lab with the different protien secretion systems, and these sequences can be inputed to the model which can predict if the sequences are likely to be secreted via the system they are designed for or not. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9505988a-c4f6-470d-a1de-8b1b09e6be78",
   "metadata": {},
   "source": [
    "# Section three:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa8633fe-506c-46f8-8617-8600e961888d",
   "metadata": {},
   "source": [
    "In section three we are going to use the model to make a prediction based off a sequence I have designed in the lab that is intended for secretion via the Sec system. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16383762-9439-44a1-a4a8-77ff9af40b52",
   "metadata": {},
   "source": [
    "**Step one:** Input a lab sequence of interest "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a25ea49d-6ebb-4d97-81dd-086b121fbe83",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted Secretion System: sec\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Using a lab sequence \n",
    "lab_sequence = \"MGRKLTALFVASTLALGAANLAHAADTTTAAPADAKPMMHHKGKFGPHQDMMFKDLNLTDAQKQQIREIMKGQRDQMKRPPLEERRAMHDIIASDTFDKVKAEAQIAKMEEQRKANMLAHMETQNKIYNILTPEQKKQFNANFEKRLTERPAAKGKMPATAE\"\n",
    "\n",
    "# Calculate amino acid composition for the new sequence\n",
    "new_amino_acid_composition = calculate_amino_acid_composition(lab_sequence)\n",
    "\n",
    "# Create a dataframe for the new sequence\n",
    "lab_sequence_df = pd.DataFrame([new_amino_acid_composition])\n",
    "\n",
    "# Use the trained RandomForest classifier to predict the secretion system\n",
    "predicted_secretion_system = classifier.predict(lab_sequence_df)\n",
    "\n",
    "print(f\"Predicted Secretion System: {predicted_secretion_system[0]}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db814841-19df-4503-94fb-e8a1bda8b600",
   "metadata": {},
   "source": [
    "This is the output from the model, predicting that this input sequence will be secreted via the Sec system, as this is what the protien was designed for I can now progress with the production of this protein and its use in lab based experiments. "
   ]
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
