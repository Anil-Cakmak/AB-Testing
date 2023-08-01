import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

# Verilerin okutulması, analiz edilmesi ve birleştirilmesi.
df_control = pd.read_excel("datasets/ab_testing.xlsx", sheet_name="Control Group")
df_test = pd.read_excel("datasets/ab_testing.xlsx", sheet_name="Test Group")


def check_df(dataframe, head=5, quantiles=[0.05, 0.50, 0.95, 0.99]):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Index ####################")
    print(dataframe.index)
    print("##################### Quantiles #####################")
    print(dataframe.describe(quantiles).T)


check_df(df_control)
check_df(df_test)

df = pd.concat([df_control, df_test], axis=0, ignore_index=True)
df["Group"] = pd.Series(["control" if (i < df_control.shape[0]) else "test" for i in df.index])

#####################################################
#  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# HO: M1 = M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında fark yoktur.)
# H1: M1!= M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında fark vardır.)

# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz
print(df.groupby("Group")["Purchase"].mean())
# Group
# control    550.894059
# test       582.106097

#####################################################################################################
# Hipotez Testinin Gerçekleştirilmesi (AB Testi (Bağımsız İki Örneklem T Testi))
#####################################################################################################

# Normallik ve Varyans Homojenliği varsayımlarının kontrol edilmesi

# HO: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.

test_stat, pvalue = shapiro(df.loc[df["Group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value = 0.5891 > 0.05
# HO reddedilemez. Kontrol grubunun değerleri normal dağılım varsayımını sağlamaktadır.

test_stat, pvalue = shapiro(df.loc[df["Group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.1541 > 0.05
# HO reddedilemez. Test grubunun değerleri normal dağılım varsayımını sağlamaktadır.


# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir
test_stat, pvalue = levene(df.loc[df["Group"] == "control", "Purchase"],
                           df.loc[df["Group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.1083 > 0.05
# HO reddedilemez. Kontrol ve Test grubunun değerleri varyans homejenliği varsayımını sağlamaktadır.

# Varsayımlar sağlandığı için "Bağımsız İki Örneklem T Testi"ni kullanabilirim.

test_stat, pvalue = ttest_ind(df_control["Purchase"],
                              df_test["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value = 0.3493 > 0.05
# HO reddedilemez. Kontrol grubu ve test grubu satın alma ortalamaları arasında istatiksel olarak anlamlı bir
# fark yoktur.
