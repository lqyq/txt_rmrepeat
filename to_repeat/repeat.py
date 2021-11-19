# -*- coding = utf-8 -*-
import sys, os
import time
from io import StringIO

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

'''
如果是小文件，直接全部读入内存，然后处理就可以了，这个是很快的，但是当数据大了之后，直接读入内存，会承受不住，所以只能分割。
我的处理方式是先把大文件分割成小文件，在分割的时候，就直接把小文件按照小文件排序去重的流程直接排序去重了。
然后再通过不断的获取所有文件的最小行，写入到最终文件中，就实现了这一目的。
'''

class Ui_MainWindow( object ):
    '''
    ui方面的设置和操作
    '''

    def __init__(self):
        # output file path
        self.output_path = ""
        # input file path
        self.input_path = ""
        # 选择操作模式
        self.mode = ""
        # frame init
        self.frame_init()

    def frame_init(self):
        app = QApplication( sys.argv )
        self.frame = QMainWindow()
        self.setupUi( self.frame )
        self.frame.show()
        sys.exit( app.exec_() )

    def setupUi(self, MainWindow):
        '''
        QT Desiger 自动生成页面
        :param MainWindow:
        :return:
        '''
        MainWindow.setObjectName( "MainWindow" )
        MainWindow.resize( 873, 492 )
        self.centralwidget = QtWidgets.QWidget( MainWindow )
        self.centralwidget.setObjectName( "centralwidget" )
        self.horizontalLayoutWidget = QtWidgets.QWidget( self.centralwidget )
        self.horizontalLayoutWidget.setGeometry( QtCore.QRect( 30, 140, 411, 91 ) )
        self.horizontalLayoutWidget.setObjectName( "horizontalLayoutWidget" )
        self.horizontalLayout = QtWidgets.QHBoxLayout( self.horizontalLayoutWidget )
        self.horizontalLayout.setContentsMargins( 0, 0, 0, 0 )
        self.horizontalLayout.setObjectName( "horizontalLayout" )
        self.lab_output = QtWidgets.QLabel( self.horizontalLayoutWidget )
        self.lab_output.setObjectName( "label_2" )
        self.horizontalLayout.addWidget( self.lab_output )
        self.edi_output = QtWidgets.QLineEdit( self.horizontalLayoutWidget )
        self.edi_output.setObjectName( "lineEdit_2" )
        self.horizontalLayout.addWidget( self.edi_output )
        self.but_scan_output = QtWidgets.QPushButton( self.horizontalLayoutWidget )
        self.but_scan_output.setObjectName( "pushButton_3" )
        self.horizontalLayout.addWidget( self.but_scan_output )
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget( self.centralwidget )
        self.horizontalLayoutWidget_2.setGeometry( QtCore.QRect( 30, 30, 411, 80 ) )
        self.horizontalLayoutWidget_2.setObjectName( "horizontalLayoutWidget_2" )
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout( self.horizontalLayoutWidget_2 )
        self.horizontalLayout_2.setContentsMargins( 0, 0, 0, 0 )
        self.horizontalLayout_2.setObjectName( "horizontalLayout_2" )
        self.lab_input = QtWidgets.QLabel( self.horizontalLayoutWidget_2 )
        self.lab_input.setObjectName( "label" )
        self.horizontalLayout_2.addWidget( self.lab_input )
        self.edi_input = QtWidgets.QLineEdit( self.horizontalLayoutWidget_2 )
        self.edi_input.setObjectName( "lineEdit" )
        self.horizontalLayout_2.addWidget( self.edi_input )
        self.but_scan_input = QtWidgets.QPushButton( self.horizontalLayoutWidget_2 )
        self.but_scan_input.setObjectName( "pushButton_2" )
        self.horizontalLayout_2.addWidget( self.but_scan_input )
        self.but_start = QtWidgets.QPushButton( self.centralwidget )
        self.but_start.setGeometry( QtCore.QRect( 380, 360, 93, 28 ) )
        self.but_start.setObjectName( "pushButton" )
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget( self.centralwidget )
        self.horizontalLayoutWidget_3.setGeometry( QtCore.QRect( 550, 30, 231, 91 ) )
        self.horizontalLayoutWidget_3.setObjectName( "horizontalLayoutWidget_3" )
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout( self.horizontalLayoutWidget_3 )
        self.horizontalLayout_3.setContentsMargins( 0, 0, 0, 0 )
        self.horizontalLayout_3.setObjectName( "horizontalLayout_3" )
        self.lab_split_file = QtWidgets.QLabel( self.horizontalLayoutWidget_3 )
        self.lab_split_file.setObjectName( "label_3" )
        self.horizontalLayout_3.addWidget( self.lab_split_file )
        self.edi_split_size = QtWidgets.QLineEdit( self.horizontalLayoutWidget_3 )
        self.edi_split_size.setObjectName( "lineEdit_3" )
        self.horizontalLayout_3.addWidget( self.edi_split_size )
        self.pro_bar = QtWidgets.QProgressBar( self.centralwidget )
        self.pro_bar.setGeometry( QtCore.QRect( 50, 280, 781, 23 ) )
        self.pro_bar.setProperty( "value", 0 )
        self.pro_bar.setObjectName( "pro_bar" )
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget( self.centralwidget )
        self.horizontalLayoutWidget_4.setGeometry( QtCore.QRect( 550, 150, 211, 80 ) )
        self.horizontalLayoutWidget_4.setObjectName( "horizontalLayoutWidget_4" )
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout( self.horizontalLayoutWidget_4 )
        self.horizontalLayout_4.setContentsMargins( 0, 0, 0, 0 )
        self.horizontalLayout_4.setObjectName( "horizontalLayout_4" )
        self.lab_select_mode = QtWidgets.QLabel( self.horizontalLayoutWidget_4 )
        self.lab_select_mode.setEnabled( True )
        self.lab_select_mode.setObjectName( "label_4" )
        self.horizontalLayout_4.addWidget( self.lab_select_mode )
        self.com_select_mode = QtWidgets.QComboBox( self.horizontalLayoutWidget_4 )
        self.com_select_mode.setObjectName( "comboBox" )
        self.com_select_mode.addItem( "" )
        self.com_select_mode.addItem( "" )
        self.horizontalLayout_4.addWidget( self.com_select_mode )

        MainWindow.setCentralWidget( self.centralwidget )
        self.menubar = QtWidgets.QMenuBar( MainWindow )
        self.menubar.setGeometry( QtCore.QRect( 0, 0, 873, 26 ) )
        self.menubar.setObjectName( "menubar" )
        MainWindow.setMenuBar( self.menubar )
        self.statusbar = QtWidgets.QStatusBar( MainWindow )
        self.statusbar.setObjectName( "statusbar" )
        MainWindow.setStatusBar( self.statusbar )

        self.retranslateUi( MainWindow )
        QtCore.QMetaObject.connectSlotsByName( MainWindow )

    def retranslateUi(self, MainWindow):
        '''
        关于图形界面的逻辑层，都在这里，比如事件监听
        :param MainWindow:
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle( _translate( "MainWindow", "txt行排序去重  v1.0  三月软件·python组出品" ) )
        self.lab_output.setText( _translate( "MainWindow", "输出文件：" ) )
        self.but_scan_output.setText( _translate( "MainWindow", "浏览" ) )
        self.lab_input.setText( _translate( "MainWindow", "数据文件：" ) )
        self.but_scan_input.setText( _translate( "MainWindow", "浏览" ) )
        self.but_start.setText( _translate( "MainWindow", "开始" ) )
        self.lab_split_file.setText( _translate( "MainWindow", "分割文件大小(MB)：" ) )
        self.edi_split_size.setText( _translate( "MainWindow", "200" ) )
        self.lab_select_mode.setText( _translate( "MainWindow", "模式：" ) )
        self.com_select_mode.setItemText( 0, _translate( "MainWindow", "排序并去重" ) )
        self.com_select_mode.setItemText( 1, _translate( "MainWindow", "仅排序" ) )

        self.edi_input.setText( "" )
        self.edi_output.setText( "" )
        # set not edit 不能编辑
        self.edi_input.setFocusPolicy( QtCore.Qt.NoFocus )
        self.edi_output.setFocusPolicy( QtCore.Qt.NoFocus )
        # set click event
        self.but_scan_output.clicked.connect( self.scan_output )
        self.but_scan_input.clicked.connect( self.scan_input )
        self.but_start.clicked.connect( self.start )

    def start(self):
        '''
        点击确定按钮触发的事件
        :return:
        '''
        start = time.time()  # 保存一下当前时间
        self.pro_bar.setProperty( "value", 0 )  # 把进度条设置为0%
        if self.input_path and self.output_path and self.edi_split_size.text().isdigit():  # 如果input path和out put path都不为空，而且分割数值也填写规范，就可以继续
            # 需要传过去输入数据的路径，输出数据的路径，以及当前分割的文件大小（默认200MB），即如果超过200MB，就按单个200MB文件分割，否则，就不分割，直接去重排序
            ToRepeatAndSort( self.input_path, self.output_path, self.edi_split_size.text(),
                             self.com_select_mode.currentIndex() )
            # 上面的操作完成后，把进度条设置为100.  （进度条动态显示，我不会。。。欢迎您指教）
            self.pro_bar.setProperty( "value", 100 )

        end = time.time()  # 保存结束时间
        QMessageBox.information( None, "完成", "用时：" + str( end - start ) + "s", QMessageBox.Yes )  # 弹出框，花费了多少秒

    def scan_input(self):
        '''
        点击输入数据右边的浏览按钮触发的事件，用来找到输入文件，限制只能是以.txt结尾的数据。
        因为getOpenFileName方法返回的是一个元组，0号是文件名，1号是文件后缀，所以我只要了第一个
        默认文件管理器弹出在C盘
        :return:
        '''
        self.input_path = \
            (QFileDialog.getOpenFileName( None, "浏览", " C:\\", "*.txt" ))[0]
        self.edi_input.setText( self.input_path )

    def scan_output(self):
        '''
        点击输出数据右边的浏览按钮触发的事件，用来找到输出文件夹。
        默认文件管理器弹出在C盘
        :return:
        '''
        self.output_path = QFileDialog.getExistingDirectory( None, "浏览",
                                                             " C:\\" )
        self.edi_output.setText( self.output_path )

class ToRepeatAndSort:
    '''
    关于行处理的逻辑操作
    '''
    def __init__(self, input_path, output_path, split_size, mode):
        # 存储一下路径
        self.input_path = input_path
        self.output_path = output_path
        # 获取分割大小（MB），转换为字节
        self.split_size = int( split_size ) * 1024 * 1024
        # 因为txt一行最多是1.1KB，这样就能算出在这个分割大小下，最多能装多少行
        self.split_line = int( int( split_size ) * 1024 / 1.1 )
        # 获取输入文件的字节大小
        self.input_file_size = self.get_file_size( self.input_path )
        # 获取模式
        self.mode = mode

        # 文件描述符列表（open(...))
        self.file_ds = []
        # 最终的文件数据存放的列表
        self.final_data = []
        # 数据操作的临时存储列表
        self.temp_data = []

        # 文件的数量
        self.file_count = 1
        # 删除的文件数量
        self.del_count = 0

        # 文件名后缀的数字迭代初始化
        self.file_name_index = 0
        # 最终存储的文件的名字
        self.final_file_name = "final_sorted0"

        self.main()

    def main(self):
        '''
        主逻辑，用来判断调用哪个函数
        最小的分割单元，可以自己设置，默认200MB，大概需要花费0.7G的内存。
        如果小于200MB，不用担心内存被撑爆，所以直接简单处理了。对于大文件，就要进行分治。
        :return:
        '''

        # 获取最终存储的文件的名字（确保不会被冲突）
        self.check_file()

        # 判断数据文件是否小于等于分割文件
        if (self.input_file_size <= self.split_size):
            # 这个mode来自下拉框的选择
            if (self.mode == 0):
                # 排序并去重
                self.line_sort_repeat_little( self.input_path, self.final_file_name )
            else:
                # 排序
                data = self.line_sort_little( self.input_path )
                # 把data保存到文件中
                self.file_story( data, self.final_file_name )
        else:
            # 先分割文件
            self.split_file( self.input_path )

            if (self.mode == 0):
                # 排序并去重
                self.merge_file()
            else:
                # 排序
                self.merge_file_sort()
            # 最后把分割的文件都删掉
            self.del_file()

    def line_sort_little(self, file_path):
        '''
        给一个文件，把里面的数据按行存到列表里，返回这个列表
        :param file_path:文件
        :return:data
        '''
        with open( file_path, "r" ) as f:
            data = f.read().splitlines()
        list.sort( data )
        return data

    def line_sort_repeat_little(self, input_path, output_path):
        '''
        排序并去重，little的后缀，代表是对于小文件使用的
        :param input_path: 输入文件路径
        :param output_path: 输出文件路径
        :return:void
        '''
        # 先给这个文件排序
        data = self.line_sort_little( input_path )
        # 然后直接把data按行写入文件，因为是排序过的，相同的会挨着，直接用continue过滤了
        with open( output_path, "a" ) as f:
            prev = ""
            for line in data:
                if prev.__eq__( line ):
                    continue
                f.write( line + "\n" )
                prev = line

    def file_yield(self, input_name):
        '''
        利用yield生成器，迭代的获取这个文件的行信息
        :param input_name:
        :return:
        '''
        with open( input_name, 'r' ) as f:
            for line in f:
                yield line

    def split_file(self, input_name):
        '''
        大文件分割成小文件
        :param input_name:文件路径
        :return:void
        '''

        # 行的数量
        line_count = 0
        # 初始化IO
        io = StringIO()

        # 每读取一行，行的数量自加，当达到上面设置的最大行的时候，清空一次内存，存入文件
        for line in self.file_yield( input_name ):
            io.write( line )
            line_count += 1

            if line_count == self.split_line:
                with open( str( self.file_count ) + ".txt", 'a' ) as f:
                    f.write( io.getvalue() )
                # 达到最大行了，未必就达到了分割的大小，如果没达到，就再循环一次，如果发现字节数已经超过了，就对这个小文件进行排序和去重。
                if os.path.getsize( str( self.file_count ) + ".txt" ) >= self.split_size:
                    # 因为排序和去重 与 仅去重 这两种方式的逻辑并不一样，所以用了一个分支来表达
                    if self.mode == 0:
                        self.line_sort_repeat_little( str( self.file_count ) + ".txt",
                                                      str( self.file_count ) + "h" + ".txt" )
                    else:
                        data = self.line_sort_little( str( self.file_count ) + ".txt" )
                        self.file_story( data, str( self.file_count ) + "h" + ".txt" )
                    # 加h的是我们已经处理好的单个文件，那么分割处理的文件就可以删掉了。
                    os.remove( str( self.file_count ) + ".txt" )
                    # 记录一下，文件的数量自加1，这样可以让我们知道，我们一共分割了多少文件
                    self.file_count += 1

                line_count = 0
                io = StringIO()

        # 排序最后一个文件
        with open( str( self.file_count ) + ".txt", 'a' ) as f:
            f.write( io.getvalue() )
        if self.mode == 0:
            self.line_sort_repeat_little( str( self.file_count ) + ".txt",
                                          str( self.file_count ) + "h" + ".txt" )
        else:
            data = self.line_sort_little( str( self.file_count ) + ".txt" )
            self.file_story( data, str( self.file_count ) + "h" + ".txt" )
        os.remove( str( self.file_count ) + ".txt" )

    def merge_file(self):
        '''
        去重，又排序的合并
        :return:
        '''
        # get all file descriptor 先获取所有的文件描述符
        for index in range( 1, self.file_count + 1 ):
            self.file_ds.append( open( str( index ) + "h.txt", 'r' ) )

        # 再存储每个文件的第一行
        for file in self.file_ds:
            self.temp_data.append( file.readline() )

        # 这个list存储要删除数据的下标
        del_index_list = []

        while 1:
            # temp_data存的是当前各个文件中的最小值，然后这句话是获取当前temp_data中的最小值，也就是所有文件的最小值
            min_data = min( self.temp_data )
            # 这个最小值就是最终数据的第一个，然后循环
            self.final_data.append( min_data )

            # 下标的计数，代表走到了第几个文件
            index_count = 0
            for index in self.temp_data:
                '''
                这个循环是用来去重的，当我们找到最小的元素后，而且已经把这个元素添加进final_data了，那么防止之后我们再遇到这个
                元素，我们就遍历temp_data，只要发现与min_data相同的，就把这个数据对应的文件描述符的下一行，存进这个下标。
                
                如果下一行数据是有值的，说明每到最后，如果是空，就说明这个文件已经取完了，所以把这个下标存进del_list里，一会统一删除。
                '''
                if index.__eq__( min_data ) or index == min_data:
                    next_line = self.file_ds[index_count].readline()
                    if next_line:
                        self.temp_data[index_count] = next_line
                    else:
                        del_index_list.append( index_count )
                        self.del_count += 1

                index_count += 1
            # 删除del_list里下标对应的数据，fild_ds和temp_data的数据都是彼此呼应的，所以两个都删除，需要注意的是，当你删除前面的
            # 时候，后面的下标就会往前移动
            del_count_temp = 0
            for del_index in del_index_list:
                del self.file_ds[del_index - del_count_temp]
                del self.temp_data[del_index - del_count_temp]
                del_count_temp += 1
            del_index_list[:] = []
            # 如果最终数据的list已经有10000个数据了，就清空一下，写入文件
            if len( self.final_data ) == 10000:

                with open( self.final_file_name, 'a' ) as f:
                    for string in self.final_data:
                        f.write( string )

                self.final_data[:] = []
            # 如果删除文件的数量和之前分割的文件数量相同，说明所有的文件都合并完了，但此时final_data未必就是正好清空的，所以需要清空一下
            if self.del_count == self.file_count:
                if self.final_data:

                    with open( self.final_file_name, 'a' ) as f:
                        for string in self.final_data:
                            f.write( string )

                    self.final_data[:] = []
                break

    def merge_file_sort(self):
        '''
        这个和上一个差不多，但是这个不带去重，独立出来，只是为了阅读性，强行的靠分支，也能合到一起。
        这个只需要一直找所有文件的最小行，然后插入，循环这一过程即可
        :return:
        '''
        # get all file descriptor
        for index in range( 1, self.file_count + 1 ):
            self.file_ds.append( open( str( index ) + "h.txt", 'r' ) )

        # 存储每个文件的第一行
        for line in self.file_ds:
            self.temp_data.append( line.readline() )

        while 1:
            # 获取当前temp_data中的最小值，存起来
            min_data = min( self.temp_data )

            self.final_data.append( min_data )

            next_index = self.temp_data.index( min_data )
            next_line = self.file_ds[next_index].readline()

            if next_line:
                self.temp_data[next_index] = next_line
            else:
                del self.temp_data[next_index]
                del self.file_ds[next_index]
                self.del_count += 1

            if len( self.final_data ) == 10000:
                with open( self.final_file_name, 'a' ) as f:
                    for string in self.final_data:
                        f.write( string )

                self.final_data[:] = []

            if self.del_count == self.file_count:
                if self.final_data:
                    with open( self.final_file_name, 'a' ) as f:
                        for string in self.final_data:
                            f.write( string )
                    self.final_data[:] = []
                break

    def get_file_size(self, file_path):
        '''
        传过来一个文件，返回这个文件的字节大小
        :param file:path
        :return:file size
        '''
        return os.path.getsize( file_path )

    def file_story(self, data, output_path):
        '''
        传过来一个列表，和一个路径，把data里的数据遍历写入到这个文件中。
        :param data:列表数据
        :param output_path:输出的文件存储位置
        :return: void
        '''
        with open( output_path, "a" ) as f:
            for line in data:
                f.write( line + "\n" )

    def check_file(self):
        '''
        先在用户给的out put path里面找默认的final_sorted0,如果发现已经有了这个文件（我们总不能覆盖或者删掉吧），我采取
        的策略是让一个数自加1，然后把后缀换一下，这个时候再检查final_sorted1，如果还存在，继续自加，这样最终文件就不会重叠了。
        :return:
        '''
        find_file = True
        while find_file:
            find_file = False
            # os.listdir() 获取当前目录的所有文件，返回为一个列表
            for file in os.listdir( self.output_path ):
                if file.__eq__( self.final_file_name + ".txt" ):
                    '''
                    如果发现这个文件和我们目前准备存储的文件名字相同，我们就得换名字了
                    把final_file_name的第0位，到减去file_name_index位，如果是final_sorted15 就是指final_sorted这个部分，
                    然后加上新的index，如果一直没有找到重复的，就会结束循环，然后最后再把路径前面的部分补充上，这就是最终文件路径了。
                    '''
                    self.final_file_name = self.final_file_name[
                                           0:len( self.final_file_name ) - len( str( self.file_name_index ) )] + str(
                        self.file_name_index )
                    self.file_name_index += 1
                    find_file = True
                    break

        self.final_file_name = os.path.join( self.output_path, self.final_file_name + ".txt" )

    def del_file(self):
        '''
        删除文件，假如说分割文件数量为5，就删除1h.txt 2h.txt 3h.txt 4h.txt 5h.txt
        :return:
        '''
        for i in range( 1, self.file_count + 1 ):
            os.remove( str( i ) + "h.txt" )
