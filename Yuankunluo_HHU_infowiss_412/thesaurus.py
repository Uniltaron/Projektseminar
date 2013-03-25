#!/usr/bin/python
# -*- coding: UTF-8 -*-
#File: thesaurus.py
#Project: Projektseminar Gruppe 412
#Project Teilnehmer: Yuankun LUO & Jingwen Wu
#Author: Yuankun LUO 2039781
#Kommentarsprache： Deusche & Chinesische,weil alle die zwei Gruppenteilnehmen chinesen sind.
#Email: yuankun.luo@hhu.de
#Version: 2013.03.22
#Python Version: 2.7.3

"""
Das Programm ist ein einfacher ThesaurusDatabank.
Ein Thesaurus wird durch eine Instance von Class Thesaurus implenmentiert.
Nach alle Operationen wird die Instance gespeichert.

这个简单的程序只用来操作一个辞典项目即可，但是为了方便，我设计了一个辞典类class Thesaurus,
每一个辞典是这个词典类的一个实例。
"""
#Benutzen pickle Modul um Datein zu speichern  运用pickle模块来储存所有数据

import pickle
import xml
import json
import csv
import collections

def convert(data):
    """
    Da json.load() Funktion macht alles in Unicode,
    deshablb muss ich mit diesen Funktion allen Sting
    ins ASSII conventieren.

    jason.load()函数会把所有读取的信息转换成unicode编码，
    这样会在每一个字符串之前，加一个u，于整体不协调。
    所以设计一个convert函数来转换。
    """
    if isinstance(data, unicode):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data



#============================================================
#class Thesaurus 辞典类
#Jeder Thesaurus ist eine Instance von class Thesaurus.
#Thesaurusinstance hat einen Projektnam und eine Dict inhalts
#um alle Deksriptorsaetze zu speichern
#
#每一个辞典都是辞典类的一个实例，由于我们的程序很简单，我们只需要一个实例；
#但是为了方便起见，更好的面向对象，我们需要用这个类来保存数据。
#每一个实例有一个属性projectname来标记项目名称以及一个
#字典类型的inhalts属性来记录所有词条
#============================================================

class Thesaurus(dict):
    
    def __init__(self, name):
        """
        Konbasestringuktor __init__(self,name):
        wir brachen eine basestringing name als projectname.
        alle Informationen werden in eine Dict heisst inhalts gespeichert.
        Alle Deksriptorsatze werden in disen inhalts nach Keys gespeichert.

        构造器函数 __init__(self，name):
        需要传入一个name字符串参数用作项目名称标记。
        其次，我们用一个名为inhalts属性的字典类型来储存所有字条，这样的储存方式是按键key储存。
        """
        self.projectname=name
        self.inhalts={}
        self.bglist=[]
        self.update_bglist()
        print "Thesaurus {t} wird erfolgrich erzeugt!\nBitte sprichern!\n".format(t=self.projectname)


    def __repr__(self):
        """
        @Override __repr__:
        um die Inhalts von Thesaurusinstance als eine List zu zeigen.

        @重写__repr__:
        为了在直输入辞典实例时，显示这个辞典实例所包含的的词条，
        并且用一个list来显示。
        """
        return "   {projectname}\n{line}\n{de}\n{line}".format(projectname=self.projectname,line='-'*20,de=self.inhalts.keys())


    #--------------------------------------------
    #Hier werden zwei Suchen Methoden definiet,
    #Eine ist search_ds(), die mit Suchen nach Deskriptor zu tun hat.
    #Eine ist search(), die eine Stichwort-Sucher ist.
    #
    #这里定义两个搜索方法：
    #一个是搜索词条方法search_ds()，用来搜索指定词条。
    #一个是搜索关键字方法search(),用来在整个辞典内按关键字搜索。
    #--------------------------------------------
    def search_ds(self, bf):
        """
        search_ds(self,bf) ist eine Methode, die nach eingegebenen Deskriptor sucht. 

        搜索词条方法: 如果词条搜索成功，就返回词词条.
        """
        if isinstance(bf,basestring):
            try:
                if self.inhalts.has_key(bf):
                    print self.inhalts[bf]
                    return True
                else:
                    return False
            except:
                print "Exception:\nseach_ds() in Class Thesaurus."

                
    def search(self,nbg):
        """
        search(self,nbg) ist eine Instancemethode von Class Thesaurus.
        Sie suche nach das eingegebennen basestringing als Stichwort.
        Return True und print Deskriptorsatz, falls gefunden;
        Return False,sonst.

        辞典的关键字搜索，传入一个字符串用作搜索参数。
        如果找到，则打印出包含这个字符串的字条，并且返回True；
        否则，返回False。
        """
        try:
            self.update_bglist()
            if nbg in self.bglist:
                if self.search_ds(nbg):
                    print self.inhalts[nbg]
                    return True
                else:
                    for ds in self.inhalts.keys():
                        if self.inhalts[ds].search_bg(nbg):
                            print self.inhalts[ds]
                    return True
            else:
                return False
        except:
            print "Exception:\nsearch_bg() in Class Thesaurus."
                
                


    def collect_bglist(self):
        """
        collocet_bg(self) ist eine Instancemethode von Class Thesaurus.
        Sie sammelet alle Begriifen in Thesaurus an,
        und speichert diese Information in self.bglist.

        搜集概念方法：
        这个方法是一个辞典类的实例方法，用于把所有实例包含的概念都保存在
        实例自己的bglist列表型属性内。以供关键字搜索。
        """
        dslist=[]
        try:
            for ds in self.inhalts.keys():
                for item in self.inhalts[ds].__dict__.keys():
                    if (item is 'bglist'):
                        dslist.extend(self.inhalts[ds].__dict__[item])
            return dslist
        except:
            print "Exception:\ncollect_ds()."

    def update_bglist(self):
        try:
            self.bglist=self.collect_bglist()
        except:
            print "Exception:\nupdate_bg(self) in Class Thesaurus."

    #----------------------------------------
    #Hier werden einigen Operator Funktionen definier,
    #ZB: add_ds(), del_ds()
    #
    #这里定义一些辞典类实例的操作方法：
    #比如添加词条，删除词条等
    #----------------------------------------
        
                
    def add_ds(self,ds):
        """
        Methode add_ds(self,ds) ist eine Instancemethode von Class Thesaurus.
        Sie fuegt eine Deskriptorsatz in Thesaurus inhalts hin.
        Sie braucht eine Instance von Class Deskriptorsatz als notwendig Argument.
        Oder sie braucht ein String als Argument, damit eine neue Instance von Deskriprotsatz
        zu erzeugen, dann fuegt ihn dazu hin.

        添加词条方法，用于将一个词条类的实例添加到辞典累实例的inhalts属性内。
        作为必要参数，一种方式是传递一个词条类的实例引用，
        另外一种方式，是传递一个字符串。
        如果传递一个字符串，则会生成一个以字符串调用词条类构造器产生的对象，
        并添加。
        """
        try:
            if isinstance(ds,Deskriptorsatz):
                if not self.inhalts.has_key(ds.deskriptor):
                    self.inhalts[ds.deskriptor]=ds
                    print "{d} wird erfolgricht in {t} hinzufugt!\n{keys}\nBittle Speichern!".format(d=ds.deskriptor,t=self.projectname,keys=self.inhalts.keys())
                    return True
                else:
                    return False
            elif isinstance(ds,basestring) and (not ds in self.inhalts.keys()):
                d=Deskriptorsatz(ds)
                self.add_ds(d)
                return True
            else:
                raise Exception()
                return False
        except:
            print "Exception:\n{t} has schon {ds}, Sie koennen nicht Dupulicate hinzufugen.".format(t=self.projectname,ds=ds)
            print self.inhalts.keys()
            return False
        
        
                


    def del_ds(self, bf):
        """
        delete_ds(self,bf) ist eine Methode von Instance der Thesaurus,
        um einen gegebenen Deskriptorsatz zu loeschen.
        Sie brucht ein basestringing bf als formale Argument.

        删除词条方法：是一个辞典Thesaurus类的实例方法，由实例来调用。
        需要传入一个字符串参数，用作被删除的目标。
        """
        if isinstance(bf,basestring):
            try:
                if self.inhalts.has_key(bf):
                    self.inhalts.pop(bf)
                    print "{bf} wird erfolgricht von {t} entfernt!".format(bf=bf,t=self.projectname)
                    print "   {projectname}\n{line}\n{de}\n{line}".format(projectname=self.projectname,line='-'*20,de=self.inhalts.keys())
                    return True
                else:
                    raise Exception()
            except:
                print "Exception:\nBei Anrufen von delete_ds(self,bf).\nEs gibt keine {bf} in {t}\n{t} has die forgenden Deskripotorsaetze:".format(bf=bf, t=self.projectname)
                print self.inhalts.keys()
                return False
        else:
            print "Error:\ndelete_ds(self,bf) barucht eine Instance von Thesauruse anzurufen\n und ein basestringing als argument!"
            return False

    def get_ds(self,ds):
        """
        
        """
        try:
            if isinstance(ds,basestring) and (ds in self.inhalts.keys()):
                return self.inhalts[ds]
            else:
                raise Exception()
        except:
            print "{ds} wird nicht in Thesaurus erfolgrich angeruft".format(ds=ds)
        
    
        
    #--------------------------------------------------
    #Hier werden viele Methoden, die mit Sprichern oder Im/EXport
    #Funktionen zu tun haben, definiet.
    #
    #这里将定义一些与保存，导入，导出功能相关的方法。
    #--------------------------------------------------
            
    def save_thesaurus(self):
        """
        save_thesaurus() ist eine Funktion, um die Instance von class Thesaurus zu speichern,
        wir bentuzen pickle modul, weil pickle ist einfache und schnell.
        Alle Informationen von dieser Instance werden in einen 'datenbank' Dokument gespeichert.
        Bei Anrufen des Methodes muss noch eine Argument als dateinamen eingeben werden.
        
        我们要将这个Thesaurus辞典类的实例持久化保存，通过save_thesaurus方法。
        这是一个有参数的方法，直接新建一个根据传入的字符串参数作为数据库名称的文档把对象转化为字节码储存。
        并且自动储存在一个以.projectname明白的.dat文档内
        """
        try:
            filename=self.projectname+'.dat'
            ouf=open(filename,'wb')
            data=self
            pickle.dump(data,ouf)
            ouf.close()
            print "Thesaurus {t} wird erfolgricht gespeichert!\n".format(t=self.projectname)
            return True
        except:
            print "Nicht erfolgreicht gesprichert!\n"
            return False

    def load_thesaurus(self, datenbank):
        """
        load_thesaurus() ist eine Funkion, die die schon in 'datenbank' gepeichert Information
        neue zu laden.

        同样用pickle模块的load()来装载已经保存的thesaurus辞典。
        """
        try:
            f=open(datenbank,'rb')
            data=pickle.load(f)
            self=data
            f.close()
            print "Thesaurus {name} wird erfolgricht gelaedt!".format(name=self.projectname)
            print self.inhalts.keys()
            return True
        except:
            print "Wird nicht erfolgricht gelaedet!"
            return False
    

    def export_ds_json(self):
        """
        export_ds_json():
        Diese Mehtode macht eine Export von Instance Thesaurus,und
        speichert die .inhalts eine Thesaurus Instance in einen .json Datein,
        mit den Name von .peojectname.

        导出json方法：
        这个方法是辞典类实例方法，辞典类的实例调用这个方法，不需要其他参数。
        这是将自动以辞典实例的.projectname属性为文件名，在本地磁盘生成这个
        projectname.json的文档。
        然后将这个辞典含有的所有词条信息通过dump()方法，保存在这个.json文档内。
        这样就完成了json的输出。
        """
        try:
            filename=self.projectname+'.json'
            with open(filename,mode='w') as f:
                data={}
                for key in self.inhalts.keys():
                    data[key]=self.inhalts[key].__dict__
                json.dump(data,f,indent=4,encoding='utf-8',skipkeys=True,ensure_ascii=False)
                return True
        except:
            return False



        
    def import_ds_json(self,filename):
        """
        import_ds_json():
        Diese Methode braucht eine String als Argument,um eine .json Datei
        zu lesen. Dann mit die Information von dieser .json Datein erzeugt
        Dekripotorsatz Instance und fuegt diese Deskriptorsatze in self.

        导入json方法：
        这个方法需要一个.json的文件名作为参数，并解析这个文件内读取到的信息。
        然后通过调用词条内的构造器来生成符合这些信息的词条对象，并把这些对象
        添加到这个辞典对象内。
        """
        try:
            with open(filename, mode='r') as f:
                data=json.load(f,encoding='utf-8')
                data=convert(data)
                for key in data.keys():
                    d=Deskriptorsatz(data[key]['deskriptor'],
                                   data[key]['bf'],
                                   data[key]['bs'],
                                   data[key]['sb'],
                                   data[key]['ob'],
                                   data[key]['vb'],
                                   data[key]['ub'])
                    self.add_ds(d)
                self.save_thesaurus()
                return True      
        except:
            print "{filename}.json wurde nicht gefunden und importiert.".format(filename=filename)
            return False

    def export_ds_csv(self):
        """
        export_ds_csv soergt dafuet, alle Deskriptorsatze in disem Thesaurus
        als eine .csv datein exportieren zu koennen.
        Wir benutzen hier ein Object von class DictWriter,
        um alle Information in Dict zu schreiben.

        输出词条csv方法，是一个辞典类的实例方法，
        用作把这个辞典实例的.inhalts信息序列化，并输出为一个.csv文档.
        我们在这里运用DictWriter类来写入dict类型的数据。
        """
        try:
            filename=self.projectname+'.csv'
            with open(filename,'wb') as f:
                #Fieldsname im Exceldatein,
                fields=['deskriptor','bf','bs','sb','ob','ub','vb','bglist']
                #Schreiben Fieldsname in ersten Reihe
                writer=csv.DictWriter(f,fieldnames=fields)
                writer.writerow(dict(zip(fields,fields)))
                for ds in self.inhalts.keys():
                    #self.inhalts[ds].__dict__ bekommt man jedes mal all Information
                    #ueber die Deskriprotsatz Instance
                   writer.writerow(self.inhalts[ds].__dict__)
                return True
        except:
            print "Exception:\nexport_ds_csv() von Class Thesaurs."
            return False

    def import_ds_csv(self,filename):
        """
        import_ds_csv() ist eine Methoden, um eine passenden .csv Datein
        zu lesen und dann fuegt alle Information von disen Datein hin.
        wir benutzen hier auch class DictReader un den .csv datein zu handeln.

        导入词条csv方法，是一个辞典类的实例方法，
        用作把一个合适的.csv文档内包含词条信息导入到这个辞典内。
        我们这里也运用DictReader 类来读取文档。
        """
        try:
            with open(filename,'rb') as f:
                reader=csv.DictReader(f,fieldnames=None)
                data={}
                for row in reader:
                    d=Deskriptorsatz(row['deskriptor'],row['bf'],row['bs'],row['sb'],row['ob'],row['vb'],row['ub'])
                    self.add_ds(d)
            return True
        except:
            return False
            print "Exception:\nimport_ds_csv() in Class Thesaurus."
            
                



#===================================================================
#class Deskriptorsatz mit OPP-Idee
#
#基于面向对象思想定义的词条类
#===================================================================



class Deskriptorsatz(dict):
    """
    Deskriptorsatz ist der Baustandteil von eine Thesaurus.
    Alle Relation zwischen basestringing werden als Eingenschaften von Deskriptorsatz
    definiert.
    我们定义一个词条类来定义每一个词条，因为题目要求必须用到面向对象。
    """
    def __init__(self, deskriptor, bf=[], bs=[], sb=[], ob=[], ub=[], vb=[]):
        """
        Konbasestringuctor von Klasse Deskriptorsatz,
        um eine Instance von Deskriptorsatz zu bauen.
        Eine Instance von Deskriptorsatz wird direct in dict thesaurus hinzufuegt,
        durch die Befehlen thesaurus[deskriptor]=self.
        Jede Instance ist ein Objekt. Sie hat Properties:
        deskriptor, bf, bs, sb, ob, ub und vb.
        Mann kan direckt durch Konbasestringuktor ein Instance
        mit vorllstandigen Informationen bauen,
        oder nur ein Instance mit deskriptor machen.
        Weiter mit methode Z.B op_add(rel, newbg) machen.
        Wir benutzen eine list heisst bglist um alle Begriiffe
        von diesem Desrkiptor zu sammelen und sprichern.
        Ausserdem besitzt jedes Deskriptor eine list heisst bglist,
        um allen Begriifen unter dem Deskriptor zu sammeln,
        durch anrufen von collect_bglist().
        Das ist besser fuer Suchenfunktionen Entwicklung.

        这里是词条类 class Deskriptorsatz 的构造器。 形式参数列表解释如下：
        deskriptor 也就是这个词条的名称；
        bf， bs, sb, ob, ub, vb 的参数初始默认值是一个空列表类型。
        在构造之前会先检测这个词条是否已经在thesaurus中出现，
        如果已经出现了，会抛出错误，告诉构造不成功。
        我们用构造器来做添加词条的工具。
        在构造器完成后会打印这个已经构造好的词条。
        此外，词条的每一个实例还有一个列表类型的属性叫做bglist，用于储存所有在这个词条下出现的概念，
        这样有助于关键字搜索功能的开发。
        """
        try:
            if not isinstance(deskriptor,basestring):
                raise Exception()
            self.deskriptor=deskriptor
            self.bf=bf
            self.bs=bs
            self.sb=sb
            self.ob=ob
            self.ub=ub
            self.vb=vb
            self.bglist=self.collect_bglist()
            #print "Deskriptor '{ds}' wird erzeugt:{self}".format(ds=self.deskriptor,self=self)
        except:
            print "Exception:\n__init__() wird nicht erfolgrich angeruft.\nVielleicht du hast ein schon existierte Deskriptor hinzufuegt!\n "
    
    def __repr__(self):
        """
        @override __repr__ funktion,
        um die print Funktion zu definieren wie folgende Stil:
        @重载的运算符 __repr__ 会将print函数的格式改变，打印下列样式：
        
                  Infowiss
            ------------------------------
            BF:['Bf1', 'Bf2']
            BS:['BS1', 'BS2']
            SB:['SB']
            OB:['OB1', 'OB2']
            UB:['UB1', 'UB2']
            VB:['VB2', 'VB1']
            ==============================
            
        """
        return "\n   {deskriptor}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(deskriptor=self.deskriptor, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,ub=self.ub,vb=self.vb, stars='='*30,line='-'*30)
    
    
    #---------------------------------------------------------
    #Hier werden alle reset_xxx() methode definiert.
    #rest_reg() methoden machen alle Properties von Deskriptor leer.
    #
    #这里定义一些reset_xxx()方法，用作把每一个词条的各项子类清空。
    #---------------------------------------------------------


    def collect_bglist(self):
        """
        Methoden collect_bg(self) ist eine Methode,
        um alle Begriffen von Deskriptor zu sammeln,
        und speicher allen Begriffen jeweils Deskriptors in eine List heist newbglist.
        Und return diesen newbglist.

        搜集概念列表方法，这是一个词条类的实例方法，
        用于将这个词条实例包含的所有概念（字符串）搜集起来，
        并且保存在一个名为newbglist的列表类型变量内，
        然后返回这个列表。
        """
        newbglist=[]
        for key in self.__dict__.keys():
            if isinstance(self.__dict__[key],list):
                newbglist.extend(self.__dict__[key])
            elif isinstance(self.__dict__[key],basestring):
                newbglist.append(self.__dict__[key])
        return newbglist

    def update_bglist(self):
        """
        update_bglist(self) ist eine Instance Methode von Class Deskriptorsatz,
        um die self.bglist upzudate. Mit hilfe von Methode collect_bglist().
        Sie wird angeruft nach jede Veranderung eines Desekriptor.

        更新概念列表方法，这是一个词条类的实例方法。
        用于在每一次词条发生改变之后更新词条实例的bglist属性。
        """
        self.bglist=[]
        newbglist=self.collect_bglist()
        self.bglist=newbglist
    
    def reset_all(self):
        """
        Hier werden alle reset_xxx() methode definiert.
        rest_reg() methoden machen alle Properties von Deskriptor leer.
    
        这里定义一些reset_xxx()方法，用作把每一个词条的各项子类清空。
        """
        try:
            self.bf = [];
            self.bs = [];
            self.sb = [];
            self.ob = [];
            self.ub = [];
            self.vb = [];
            self.update_bglist()
            print self;
            return True
        except:
            print "Exception:\n reset_all() in Class Deskriptorsatz."
            return False
    
    def reset_bf(self):
        """
        Machen die BF von Instance leer.

        清空实例的BF属性。
        """
        try:
            self.bf=[]
            print "Der BF von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
            return True
        except:
            print "Methode reset_bf ist kappt"
            return False
        finally:
            self.update_bglist()

    def reset_bs(self):
        """
        Machen die BS von Instance leer.

        清空实例的BS属性。
        """
        try:
            self.bs=[]
            print "Der BS von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
            return True
        except:
            print "Methode reset_bf ist kappt"
            return False
        finally:
            self.update_bglist()

    def reset_sb(self):
        """
        Machen die SB von Instance leer.

        清空实例的SB属性。
        """
        try:
            self.sb=[]
            print "Der SB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
            return True
        except:
            print "Methode reset_bf ist kappt"
            return False
        finally:
            self.update_bglist()

    def reset_ob(self):
        """
        Machen die OB von Instance leer.

        清空实例的OB属性。
        """
        try:
            self.ob=[]
            print "Der OB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
            return True
        except:
            print "Methode reset_bf ist kappt"
            return False
        finally:
            self.update_bglist()

    def reset_ub(self):
        """
        Machen die UB von Instance leer.

        清空实例的UB属性。
        """
        try:
            self.ub=[]
            print "Der UB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
            return True
        except:
            print "Methode reset_bf ist kappt"
            return False
        finally:
            self.update_bglist()

    def reset_vb(self):
        """
        Machen die VB von Instance leer.

        清空实例的VB属性。
        """
        try:
            self.vb=[]
            print "Der VB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
            return True
        except:
            print "Methode reset_bf ist kappt"
            return False
        finally:
            self.update_bglist()


    #------------------------------------------------------
    #Hier werde alle add_reg() methode definiert.
    #reg kann als bf, bs ... benennen.
    #Nur Sring oder eine Liste von basestringing durfen hinzufuegt werden.
    #Am besten, nur ein basestringing als Argument eingeben, wenn mit GUI entwickeln.
    #wir benutzen Variable item um den Ziel des add_xx() methoden auf zu zeigen.
    #
    #这里定义一些add_xxx()发法，都是字条类实例的方法
    #用作给字条实例添加概念。
    #添加的方式是添加一个字符串或者一个由字符串组成的列表。
    #每个reg代表字条实例的每一个子项，用小写字母表示，比如bs，bf...
    #添加时会检测形式参数，必须是字符串或者字符串的列表才能被添加成功。
    #添加成功打印一个更新后的词条。
    #最好是传入一个字符串的参数，特别是当用作GUI开发的时候
    #我们用一个叫做item的变量来知识add_xx()方法的目的地。
    #------------------------------------------------------

    def add_bf(self,newbf):
        """
        add_bf(self,newbf) ist eine Instancemethode von Class Deskriptorsatz,
        um eine List oder eine basestringing in BF hinzufugen.
        Sie ueberprueft, ob das eigegebene basestringing schon in dem Deskriptorsatz.
        Dann ueberprueft, ob die Argument eine List oder eine basestringing sind.

        添加BF方法，这是一个词条类的实例方法，用作往词条实例添加概念。
        首先这个方法会验证，这个需要被添加的实例是否已经存在在这个实例中，如果是的话，
        这返回提示，并且抛出错误
        """
        item=self.bf
        try:
            if newbf in self.bglist:
                print "Error:\n{newbf} ist schon in {ds}.\nSie koennen nicht Dupulicate machen!".format(newbf=newbf,ds=self.deskriptor)
                print self
                raise Exception()
            elif isinstance(newbf,basestring):
                if not newbf in item:
                    item.append(newbf)
                    print "{nbf} wird erfolgreich in '{ds}' hinzufuegt.".format(nbf=newbf,ds=self.deskriptor)
                    return True
                else:
                    print "Error:\n{nbf} ist schon in '{ds}'.Es kann nicht hinzufuegt werden!".format(nbf=newbf,ds=self.deskriptor)
                    raise Exception()
            elif isinstance(newbf,list):
                for e in newbf:
                    if (not e in self.bglist) and isinstance(e,basestring):
                        item.append(e)
                        print "{e} wird erfolrciht in '{ds}' hinzufuegt.".format(e=e,ds=self.deskriptor)
                        return True
                    else:
                        print "Error:\n{e} ist schon in '{ds}'.\nSie koennen nicht Dupulicate machen!".format(e=e,ds=self.deskriptor)
                        print self
                        raise Exception()
            else:
                raise Exception()
        except:
            print "Exception bei add_bf().\nBitte eine basestringing oder eine Liste von basestringing als Argument eingeben."
            return False
        finally:
            self.update_bglist()

    def add_bs(self,newbf):
        """
        add_bs(self,newbf) ist eine Instancemethode von Class Deskriptorsatz,
        um eine List oder eine basestringing in BS hinzufugen.
        Sie ueberprueft, ob das eigegebene basestringing schon in dem Deskriptorsatz.
        Dann ueberprueft, ob die Argument eine List oder eine basestringing sind.

        添加BS方法，这是一个词条类的实例方法，用作往词条实例添加概念。
        首先这个方法会验证，这个需要被添加的实例是否已经存在在这个实例中，如果是的话，
        这返回提示，并且抛出错误
        """
        item=self.bs
        try:
            if newbf in self.bglist:
                print "Error:\n{newbf} ist schon in {ds}.\nSie koennen nicht Dupulicate machen!".format(newbf=newbf,ds=self.deskriptor)
                print self
                raise Exception()
            elif isinstance(newbf,basestring):
                if not newbf in item:
                    item.append(newbf)
                    print "{nbf} wird erfolgreich in '{ds}' hinzufuegt.".format(nbf=newbf,ds=self.deskriptor)
                    return True
                else:
                    print "Error:\n{nbf} ist schon in '{ds}'.Es kann nicht hinzufuegt werden!".format(nbf=newbf,ds=self.deskriptor)
                    raise Exception()
            elif isinstance(newbf,list):
                for e in newbf:
                    if (not e in self.bglist) and isinstance(e,basestring):
                        item.append(e)
                        print "{e} wird erfolrciht in '{ds}' hinzufuegt.".format(e=e,ds=self.deskriptor)
                        return True
                    else:
                        print "Error:\n{e} ist schon in '{ds}'.\nSie koennen nicht Dupulicate machen!".format(e=e,ds=self.deskriptor)
                        print self
                        raise Exception()
            else:
                raise Exception()
        except:
            print "Exception bei add_bf().\nBitte eine basestringing oder eine Liste von basestringing als Argument eingeben."
            return False
        finally:
            self.update_bglist()

    def add_sb(self,newbf):
        """
        add_sb(self,newbf) ist eine Instancemethode von Class Deskriptorsatz,
        um eine List oder eine basestringing in SB hinzufugen.
        Sie ueberprueft, ob das eigegebene basestringing schon in dem Deskriptorsatz.
        Dann ueberprueft, ob die Argument eine List oder eine basestringing sind.

        添加SB方法，这是一个词条类的实例方法，用作往词条实例添加概念。
        首先这个方法会验证，这个需要被添加的实例是否已经存在在这个实例中，如果是的话，
        这返回提示，并且抛出错误
        """
        item=self.sb
        try:
            if newbf in self.bglist:
                print "Error:\n{newbf} ist schon in {ds}.\nSie koennen nicht Dupulicate machen!".format(newbf=newbf,ds=self.deskriptor)
                print self
                raise Exception()
            elif isinstance(newbf,basestring):
                if not newbf in item:
                    item.append(newbf)
                    print "{nbf} wird erfolgreich in '{ds}' hinzufuegt.".format(nbf=newbf,ds=self.deskriptor)
                    return True
                else:
                    print "Error:\n{nbf} ist schon in '{ds}'.Es kann nicht hinzufuegt werden!".format(nbf=newbf,ds=self.deskriptor)
                    raise Exception()
            elif isinstance(newbf,list):
                for e in newbf:
                    if (not e in self.bglist) and isinstance(e,basestring):
                        item.append(e)
                        print "{e} wird erfolrciht in '{ds}' hinzufuegt.".format(e=e,ds=self.deskriptor)
                        return True
                    else:
                        print "Error:\n{e} ist schon in '{ds}'.\nSie koennen nicht Dupulicate machen!".format(e=e,ds=self.deskriptor)
                        print self
                        raise Exception()
            else:
                raise Exception()
        except:
            print "Exception bei add_bf().\nBitte eine basestringing oder eine Liste von basestringing als Argument eingeben."
            return False
        finally:
            self.update_bglist()

    def add_ob(self,newbf):
        """
        add_ob(self,newbf) ist eine Instancemethode von Class Deskriptorsatz,
        um eine List oder eine basestringing in OB hinzufugen.
        Sie ueberprueft, ob das eigegebene basestringing schon in dem Deskriptorsatz.
        Dann ueberprueft, ob die Argument eine List oder eine basestringing sind.

        添加OB方法，这是一个词条类的实例方法，用作往词条实例添加概念。
        首先这个方法会验证，这个需要被添加的实例是否已经存在在这个实例中，如果是的话，
        这返回提示，并且抛出错误
        """
        item=self.ob
        try:
            if newbf in self.bglist:
                print "Error:\n{newbf} ist schon in {ds}.\nSie koennen nicht Dupulicate machen!".format(newbf=newbf,ds=self.deskriptor)
                print self
                raise Exception()
            elif isinstance(newbf,basestring):
                if not newbf in item:
                    item.append(newbf)
                    print "{nbf} wird erfolgreich in '{ds}' hinzufuegt.".format(nbf=newbf,ds=self.deskriptor)
                    return True
                else:
                    print "Error:\n{nbf} ist schon in '{ds}'.Es kann nicht hinzufuegt werden!".format(nbf=newbf,ds=self.deskriptor)
                    raise Exception()
            elif isinstance(newbf,list):
                for e in newbf:
                    if (not e in self.bglist) and isinstance(e,basestring):
                        item.append(e)
                        print "{e} wird erfolrciht in '{ds}' hinzufuegt.".format(e=e,ds=self.deskriptor)
                        return True
                    else:
                        print "Error:\n{e} ist schon in '{ds}'.\nSie koennen nicht Dupulicate machen!".format(e=e,ds=self.deskriptor)
                        print self
                        raise Exception()
            else:
                raise Exception()
        except:
            print "Exception bei add_bf().\nBitte eine basestringing oder eine Liste von basestringing als Argument eingeben."
            return False
        finally:
            self.update_bglist()

    def add_ub(self,newbf):
        """
        add_ub(self,newbf) ist eine Instancemethode von Class Deskriptorsatz,
        um eine List oder eine basestringing in UB hinzufugen.
        Sie ueberprueft, ob das eigegebene basestringing schon in dem Deskriptorsatz.
        Dann ueberprueft, ob die Argument eine List oder eine basestringing sind.

        添加UB方法，这是一个词条类的实例方法，用作往词条实例添加概念。
        首先这个方法会验证，这个需要被添加的实例是否已经存在在这个实例中，如果是的话，
        这返回提示，并且抛出错误
        """
        item=self.ub
        try:
            if newbf in self.bglist:
                print "Error:\n{newbf} ist schon in {ds}.\nSie koennen nicht Dupulicate machen!".format(newbf=newbf,ds=self.deskriptor)
                print self
                raise Exception()
            elif isinstance(newbf,basestring):
                if not newbf in item:
                    item.append(newbf)
                    print "{nbf} wird erfolgreich in '{ds}' hinzufuegt.".format(nbf=newbf,ds=self.deskriptor)
                    return True
                else:
                    print "Error:\n{nbf} ist schon in '{ds}'.Es kann nicht hinzufuegt werden!".format(nbf=newbf,ds=self.deskriptor)
                    raise Exception()
            elif isinstance(newbf,list):
                for e in newbf:
                    if (not e in self.bglist) and isinstance(e,basestring):
                        item.append(e)
                        print "{e} wird erfolrciht in '{ds}' hinzufuegt.".format(e=e,ds=self.deskriptor)
                        return True
                    else:
                        print "Error:\n{e} ist schon in '{ds}'.\nSie koennen nicht Dupulicate machen!".format(e=e,ds=self.deskriptor)
                        print self
                        raise Exception()
            else:
                raise Exception()
        except:
            print "Exception bei add_bf().\nBitte eine basestringing oder eine Liste von basestringing als Argument eingeben."
            return False
        finally:
            self.update_bglist()

    def add_vb(self,newbf):
        """
        add_vb(self,newbf) ist eine Instancemethode von Class Deskriptorsatz,
        um eine List oder eine basestringing in VB hinzufugen.
        Sie ueberprueft, ob das eigegebene basestringing schon in dem Deskriptorsatz.
        Dann ueberprueft, ob die Argument eine List oder eine basestringing sind.

        添加VB方法，这是一个词条类的实例方法，用作往词条实例添加概念。
        首先这个方法会验证，这个需要被添加的实例是否已经存在在这个实例中，如果是的话，
        这返回提示，并且抛出错误
        """
        item=self.vb
        try:
            if newbf in self.bglist:
                print "Error:\n{newbf} ist schon in {ds}.\nSie koennen nicht Dupulicate machen!".format(newbf=newbf,ds=self.deskriptor)
                print self
                raise Exception()
            elif isinstance(newbf,basestring):
                if not newbf in item:
                    item.append(newbf)
                    print "{nbf} wird erfolgreich in '{ds}' hinzufuegt.".format(nbf=newbf,ds=self.deskriptor)
                    return True
                else:
                    print "Error:\n{nbf} ist schon in '{ds}'.Es kann nicht hinzufuegt werden!".format(nbf=newbf,ds=self.deskriptor)
                    raise Exception()
            elif isinstance(newbf,list):
                for e in newbf:
                    if (not e in self.bglist) and isinstance(e,basestring):
                        item.append(e)
                        print "{e} wird erfolrciht in '{ds}' hinzufuegt.".format(e=e,ds=self.deskriptor)
                        return True
                    else:
                        print "Error:\n{e} ist schon in '{ds}'.\nSie koennen nicht Dupulicate machen!".format(e=e,ds=self.deskriptor)
                        print self
                        raise Exception()
            else:
                raise Exception()
        except:
            print "Exception bei add_bf().\nBitte eine basestringing oder eine Liste von basestringing als Argument eingeben."
            return False
        finally:
            self.update_bglist()
            



    #------------------------------------------------------
    #Hier werden alle del_reg() methode definiert.
    #Um jeden Brgriff unter verschiedenen Relationen zu loeschen.
    #Wenn man eine Relation oder ganz Deskriptor leer machen,
    #dann benutzen rest_reg() methoden.
    #
    #这里定义一些删除字条字项的方法，因为我们用字典来保存子项的每一个属性，如果是删除子项里面的一个字符串，
    #则需要传入字符串作为形式参数。如果是想清空子项，或者完全清空，将调用reset_reg()方法。
    #------------------------------------------------------

    
    def del_bg(self,bf):
        """
        del_bg(self,bg) ist eine Instancemethode von Class Deksriptorsatz.
        Sie loescht bf in dem Deskriptorsatz.

        删除概念方法。这个方法是一个词条类的实例方法，由实例调用。
        传入一个字符串形式参数，并在词条内寻找这个参数然后删除它。
        """
        try:
            if isinstance(bf,basestring) and (bf in self.bglist) and (not bf is self.deskriptor):
                for key in self.__dict__.keys():
                    if bf in self.__dict__[key] and isinstance(self.__dict__[key],list):
                        self.__dict__[key].remove(bf)
                        print "BF {bf} wurde von '{deskriptor}' erfogreich geloescht.'".format(bf=bf, deskriptor=self.deskriptor)
                        print self
                        return True
            else:
                print "Error:\n{bf} wurden nicht in {ds} gefunden!".format(bf=bf,ds=self.deskriptor)
                raise Exception()
        except:
            print "Exception:\ndel_bf().Bittle ein basestringing als Argument geben."
            return False
        finally:
            self.update_bglist()

    def search_bg(self,sbg):
        """
        search_bg(self,sbg) ist eine Instance Methode von Class Deskriptorsatz.
        Sie braucht einen Begriffe als Argument,
        und suchen nach den Begriffe in dem Deskriptosatz.
        Return True, falls gefunden.Sonst, return False.
        Diese Methode dient fuer die Methode search_bg() von Class Thesaurus,
        um einen Begriff in ganz Thesaurus zu finden.

        词条实例概念搜索方法：
        这是一个词条类的实例所拥有的方法，用于搜索被传入的字符串参数.
        这个方法一般不自己调用，他作用于辞典类的search_bg()方法。
        """
        try:
            if isinstance(sbg,basestring):
                if (sbg in self.bglist):
                    return True
                else:
                    return False
            else:
                raise Exception()
        except:
            print "Exception:\nsearch_bg(self,sbg)in Class Deskriptorsatz."




#===================================================================
#Test Code
#
#测试用代码
#===================================================================


if __name__ == '__main__':
    t1=Thesaurus('t1')
    d=Deskriptorsatz
    t=Thesaurus    
    d1=Deskriptorsatz('Infowiss',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB2','VB1'])
    d2=Deskriptorsatz('Python',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['B1','VB2'])
    d3=d('Goggle')
    d4=d('Baidu')
    t1.add_ds(d1)
    t1.add_ds(d2)
    t1.add_ds(d3)
    t1.save_thesaurus()
    t2=t('t2')
    
