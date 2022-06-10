#!/usr/bin/env python
# coding: utf-8

# In[1]:


myList = list()


# In[2]:


type(myList)


# ## instance ve attribute

# In[2]:


superKahramanAdi = "Superman"
superKahramanYasi = 30


# In[3]:


class SuperKahraman():
    
    ozelGuc = "Görünmezlik"
    
    def __init__(self,isim,yas,meslek):
        print("init cagirilidi")
        self.isim = isim
        self.yas = yas
        self.meslek = meslek
        
        
    def ornekMethod(self):
        print(f"ben süperkahramanım ve meslegim: {self.meslek}")


# In[4]:


superman = SuperKahraman("Superman",30,"gazeteci")


# In[5]:


superman.isim = "Clark Kent"


# In[6]:


superman.isim


# In[7]:


superman.ozelGuc = "Uçabilirlik"


# In[8]:


superman.ozelGuc


# ## Methods

# In[9]:


superman.ornekMethod()


# In[10]:


class Kopek():
    
    yilCarpani = 7
    
    def __init__(self,yas=5):
        self.yas = yas
        self.insanYasinaCevrilmisAttribute = yas * 7
    
    def insanYasiniHesapla(self):
        return self.yas * Kopek.yilCarpani


# In[11]:


benimKopek = Kopek()


# In[12]:


benimKopek.yas


# In[13]:


benimKopek = Kopek(3)


# In[14]:


benimKopek.insanYasiniHesapla()


# ## inheritance

# In[15]:


class Hayvan():
    def __init__(self):
        print("hayvan sınıfı init çağırıldı.")
        
    def method1(self):
        print("hayvan sınıfı method1 çağırıldı.")
        
    def method2(self):
        print("hayvan sınıfı method2 çağırıldı.")


# In[16]:


benimHayvanim = Hayvan()


# In[17]:


benimHayvanim.method1()


# In[18]:


benimHayvanim.method2()


# In[19]:


class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi sınıfı init çağırıldı.")
    
    def miyavla(self):
        print("miyav")
    #override    
    def method1(self):
        print("kedi sınıfındaki method1 çağırıldı")


# In[20]:


benimKedim = Kedi()


# In[21]:


benimKedim.method1()


# In[22]:


benimKedim.method2()


# In[23]:


benimKedim.miyavla()


# In[24]:


digerHayvan = Hayvan()


# In[25]:


digerHayvan.method1()


# In[26]:


digerKedi = Kedi()


# In[27]:


digerKedi.method1()


# ## Polymorphism

# In[ ]:





# In[32]:


class Elma():
    def __init__(self, isim):
        self.isim = isim
        
    def bilgiVer(self):
        return self.isim + " 100 kaloridir "


# In[33]:


class Muz():
    def __init__(self, isim):
        self.isim = isim
        
    def bilgiVer(self):
        return self.isim + " 160 kaloridir "


# In[34]:


elma = Elma("elma")


# In[35]:


elma.bilgiVer()


# In[36]:


muz = Muz("muz")


# In[37]:


muz.bilgiVer()


# In[38]:


meyveListesi = [elma,muz]


# In[40]:


for meyve in meyveListesi:
    print(meyve.bilgiVer())


# In[51]:


def bilgiAl(meyve):
    print(meyve.bilgiVer())


# In[52]:


bilgiAl(muz)


# In[53]:


bilgiAl(elma)

