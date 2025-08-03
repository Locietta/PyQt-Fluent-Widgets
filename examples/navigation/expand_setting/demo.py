# coding:utf-8
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit

from qfluentwidgets import (
    ScrollArea, FluentIcon as FIF, setTheme, Theme, isDarkTheme,
    PushButton, PrimaryPushButton, RadioButton, SwitchButton, ComboBox,
    Slider, SpinBox, DoubleSpinBox, LineEdit, SearchLineEdit,
    BodyLabel, TitleLabel, setFont
)

# Import all the expand setting card classes
from qfluentwidgets.components.settings.expand_setting_card import (
    ExpandSettingCard, ExpandGroupSettingCard, SimpleExpandGroupSettingCard,
    HeaderSettingCard, ExpandButton, SpaceWidget, GroupSeparator, ExpandBorderWidget
)


class ExpandSettingDemo(ScrollArea):
    """Demo widget for expand setting cards"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)
        
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("expandSettingDemo")
        
        self.__initWidget()
        self.__initLayout()

    def __initWidget(self):
        """Initialize widgets"""
        # Title
        self.titleLabel = TitleLabel("Expand Setting Cards Demo", self)
        setFont(self.titleLabel, 20)
        
        # Basic ExpandSettingCard
        self.basicExpandCard = ExpandSettingCard(
            FIF.SETTING,
            "Basic Expand Card",
            "This is a basic expandable setting card"
        )
        
        # Add some content to the basic expand card
        self.basicContent = QWidget()
        self.basicContentLayout = QVBoxLayout(self.basicContent)
        
        # Add various controls to the basic expand card
        self.pushBtn = PushButton("Push Button")
        self.primaryBtn = PrimaryPushButton("Primary Button")
        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("Enter some text...")
        self.slider = Slider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        
        self.basicContentLayout.addWidget(BodyLabel("Controls inside expand card:"))
        self.basicContentLayout.addWidget(self.pushBtn)
        self.basicContentLayout.addWidget(self.primaryBtn)
        self.basicContentLayout.addWidget(self.lineEdit)
        self.basicContentLayout.addWidget(self.slider)
        self.basicContentLayout.setContentsMargins(48, 18, 48, 18)
        
        self.basicExpandCard.viewLayout.addWidget(self.basicContent)
        
        # ExpandGroupSettingCard with radio buttons
        self.groupExpandCard = ExpandGroupSettingCard(
            FIF.PALETTE,
            "Group Expand Card",
            "Card with grouped widgets and separators"
        )
        
        # Create radio button group
        self.radioGroup1 = QWidget()
        self.radioGroup1Layout = QVBoxLayout(self.radioGroup1)
        self.radioGroup1Layout.setContentsMargins(48, 18, 48, 18)
        
        self.radioGroup1Layout.addWidget(BodyLabel("Theme Selection:"))
        self.lightRadio = RadioButton("Light Theme")
        self.darkRadio = RadioButton("Dark Theme")
        self.autoRadio = RadioButton("Auto Theme")
        self.lightRadio.setChecked(True)
        
        self.radioGroup1Layout.addWidget(self.lightRadio)
        self.radioGroup1Layout.addWidget(self.darkRadio)
        self.radioGroup1Layout.addWidget(self.autoRadio)
        
        # Create another group with combo box
        self.comboGroup = QWidget()
        self.comboGroupLayout = QVBoxLayout(self.comboGroup)
        self.comboGroupLayout.setContentsMargins(48, 18, 48, 18)
        
        self.comboGroupLayout.addWidget(BodyLabel("Language Selection:"))
        self.languageCombo = ComboBox()
        self.languageCombo.addItems(["English", "中文", "日本語", "Français", "Deutsch"])
        self.languageCombo.setCurrentIndex(0)
        self.comboGroupLayout.addWidget(self.languageCombo)
        
        # Create switch group
        self.switchGroup = QWidget()
        self.switchGroupLayout = QVBoxLayout(self.switchGroup)
        self.switchGroupLayout.setContentsMargins(48, 18, 48, 18)
        
        self.switchGroupLayout.addWidget(BodyLabel("Feature Toggles:"))
        
        self.switchContainer1 = QWidget()
        self.switchLayout1 = QHBoxLayout(self.switchContainer1)
        self.switchLayout1.setContentsMargins(0, 0, 0, 0)
        self.enableNotifications = SwitchButton()
        self.enableNotifications.setChecked(True)
        self.switchLayout1.addWidget(BodyLabel("Enable Notifications"))
        self.switchLayout1.addStretch()
        self.switchLayout1.addWidget(self.enableNotifications)
        
        self.switchContainer2 = QWidget()
        self.switchLayout2 = QHBoxLayout(self.switchContainer2)
        self.switchLayout2.setContentsMargins(0, 0, 0, 0)
        self.enableAutoUpdate = SwitchButton()
        self.switchLayout2.addWidget(BodyLabel("Auto Update"))
        self.switchLayout2.addStretch()
        self.switchLayout2.addWidget(self.enableAutoUpdate)
        
        self.switchGroupLayout.addWidget(self.switchContainer1)
        self.switchGroupLayout.addWidget(self.switchContainer2)
        
        # Add groups to the expand group card
        self.groupExpandCard.addGroupWidget(self.radioGroup1)
        self.groupExpandCard.addGroupWidget(self.comboGroup)
        self.groupExpandCard.addGroupWidget(self.switchGroup)
        
        # SimpleExpandGroupSettingCard
        self.simpleGroupCard = SimpleExpandGroupSettingCard(
            FIF.EDIT,
            "Simple Group Card",
            "Simple expand group without manual separator management"
        )
        
        # Add simple widgets to simple group card
        self.inputGroup1 = QWidget()
        self.inputLayout1 = QVBoxLayout(self.inputGroup1)
        self.inputLayout1.setContentsMargins(48, 18, 48, 18)
        
        self.inputLayout1.addWidget(BodyLabel("Personal Information:"))
        self.nameInput = LineEdit()
        self.nameInput.setPlaceholderText("Enter your name")
        self.emailInput = LineEdit()
        self.emailInput.setPlaceholderText("Enter your email")
        
        self.inputLayout1.addWidget(BodyLabel("Name:"))
        self.inputLayout1.addWidget(self.nameInput)
        self.inputLayout1.addWidget(BodyLabel("Email:"))
        self.inputLayout1.addWidget(self.emailInput)
        
        self.inputGroup2 = QWidget()
        self.inputLayout2 = QVBoxLayout(self.inputGroup2)
        self.inputLayout2.setContentsMargins(48, 18, 48, 18)
        
        self.inputLayout2.addWidget(BodyLabel("Settings:"))
        self.volumeSlider = Slider(Qt.Orientation.Horizontal)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(75)
        self.brightnessSlider = Slider(Qt.Orientation.Horizontal)
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setValue(50)
        
        self.inputLayout2.addWidget(BodyLabel("Volume:"))
        self.inputLayout2.addWidget(self.volumeSlider)
        self.inputLayout2.addWidget(BodyLabel("Brightness:"))
        self.inputLayout2.addWidget(self.brightnessSlider)
        
        self.simpleGroupCard.addGroupWidget(self.inputGroup1)
        self.simpleGroupCard.addGroupWidget(self.inputGroup2)
        
        # HeaderSettingCard standalone (just the header part)
        self.headerCard = HeaderSettingCard(
            FIF.INFO,
            "Header Only Card",
            "This is just a header setting card without expand functionality"
        )
        
        # Add some widgets to the header card
        self.headerToggle = SwitchButton()
        self.headerCard.addWidget(self.headerToggle)
        
        # Cards with different icons and themes
        self.mediaCard = ExpandSettingCard(
            FIF.MUSIC,
            "Media Settings",
            "Configure audio and video preferences"
        )
        
        self.mediaContent = QWidget()
        self.mediaContentLayout = QVBoxLayout(self.mediaContent)
        self.mediaContentLayout.setContentsMargins(48, 18, 48, 18)
        
        # Volume control
        self.volumeContainer = QWidget()
        self.volumeContainerLayout = QHBoxLayout(self.volumeContainer)
        self.volumeContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.volumeContainerLayout.addWidget(BodyLabel("Master Volume:"))
        self.volumeContainerLayout.addStretch()
        self.masterVolumeSlider = Slider(Qt.Orientation.Horizontal)
        self.masterVolumeSlider.setMinimum(0)
        self.masterVolumeSlider.setMaximum(100)
        self.masterVolumeSlider.setValue(80)
        self.masterVolumeSlider.setFixedWidth(200)
        self.volumeContainerLayout.addWidget(self.masterVolumeSlider)
        
        # Quality selection
        self.qualityContainer = QWidget()
        self.qualityContainerLayout = QHBoxLayout(self.qualityContainer)
        self.qualityContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.qualityContainerLayout.addWidget(BodyLabel("Audio Quality:"))
        self.qualityContainerLayout.addStretch()
        self.qualityCombo = ComboBox()
        self.qualityCombo.addItems(["Low (96 kbps)", "Normal (128 kbps)", "High (320 kbps)", "Lossless"])
        self.qualityCombo.setCurrentIndex(2)
        self.qualityCombo.setFixedWidth(150)
        self.qualityContainerLayout.addWidget(self.qualityCombo)
        
        self.mediaContentLayout.addWidget(self.volumeContainer)
        self.mediaContentLayout.addWidget(self.qualityContainer)
        
        self.mediaCard.viewLayout.addWidget(self.mediaContent)
        
        # Security settings card
        self.securityCard = ExpandGroupSettingCard(
            FIF.SETTING,
            "Security Settings",
            "Manage security and privacy options"
        )
        
        # Security toggles group
        self.securityToggles = QWidget()
        self.securityTogglesLayout = QVBoxLayout(self.securityToggles)
        self.securityTogglesLayout.setContentsMargins(48, 18, 48, 18)
        
        self.securityTogglesLayout.addWidget(BodyLabel("Security Options:"))
        
        # Two-factor authentication
        self.twoFactorContainer = QWidget()
        self.twoFactorLayout = QHBoxLayout(self.twoFactorContainer)
        self.twoFactorLayout.setContentsMargins(0, 0, 0, 0)
        self.twoFactorSwitch = SwitchButton()
        self.twoFactorLayout.addWidget(BodyLabel("Two-Factor Authentication"))
        self.twoFactorLayout.addStretch()
        self.twoFactorLayout.addWidget(self.twoFactorSwitch)
        
        # Automatic login
        self.autoLoginContainer = QWidget()
        self.autoLoginLayout = QHBoxLayout(self.autoLoginContainer)
        self.autoLoginLayout.setContentsMargins(0, 0, 0, 0)
        self.autoLoginSwitch = SwitchButton()
        self.autoLoginSwitch.setChecked(True)
        self.autoLoginLayout.addWidget(BodyLabel("Remember Login"))
        self.autoLoginLayout.addStretch()
        self.autoLoginLayout.addWidget(self.autoLoginSwitch)
        
        self.securityTogglesLayout.addWidget(self.twoFactorContainer)
        self.securityTogglesLayout.addWidget(self.autoLoginContainer)
        
        # Password settings group
        self.passwordGroup = QWidget()
        self.passwordGroupLayout = QVBoxLayout(self.passwordGroup)
        self.passwordGroupLayout.setContentsMargins(48, 18, 48, 18)
        
        self.passwordGroupLayout.addWidget(BodyLabel("Password Settings:"))
        self.changePasswordBtn = PushButton("Change Password")
        self.exportBackupBtn = PushButton("Export Backup Codes")
        
        self.passwordGroupLayout.addWidget(self.changePasswordBtn)
        self.passwordGroupLayout.addWidget(self.exportBackupBtn)
        
        self.securityCard.addGroupWidget(self.securityToggles)
        self.securityCard.addGroupWidget(self.passwordGroup)
        
        # Connect signals
        self.__connectSignals()

    def __initLayout(self):
        """Initialize layout"""
        self.vBoxLayout.setSpacing(20)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Add title
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(20)
        
        # Add description
        descLabel = BodyLabel("This demo showcases all the expand setting card types available in PyQt-Fluent-Widgets:")
        self.vBoxLayout.addWidget(descLabel)
        self.vBoxLayout.addSpacing(10)
        
        # Add cards
        self.vBoxLayout.addWidget(self.basicExpandCard)
        self.vBoxLayout.addWidget(self.groupExpandCard)
        self.vBoxLayout.addWidget(self.simpleGroupCard)
        self.vBoxLayout.addWidget(self.headerCard)
        self.vBoxLayout.addWidget(self.mediaCard)
        self.vBoxLayout.addWidget(self.securityCard)
        
        # Add stretch at the end
        self.vBoxLayout.addStretch()

    def __connectSignals(self):
        """Connect widget signals"""
        # Theme radio buttons
        self.lightRadio.clicked.connect(lambda: self.__setTheme(Theme.LIGHT))
        self.darkRadio.clicked.connect(lambda: self.__setTheme(Theme.DARK))
        self.autoRadio.clicked.connect(lambda: self.__setTheme(Theme.AUTO))
        
        # Language combo
        self.languageCombo.currentTextChanged.connect(self.__onLanguageChanged)
        
        # Switches
        self.enableNotifications.checkedChanged.connect(self.__onNotificationToggle)
        self.enableAutoUpdate.checkedChanged.connect(self.__onAutoUpdateToggle)
        self.twoFactorSwitch.checkedChanged.connect(self.__onTwoFactorToggle)
        self.autoLoginSwitch.checkedChanged.connect(self.__onAutoLoginToggle)
        
        # Buttons
        self.pushBtn.clicked.connect(lambda: print("Push button clicked!"))
        self.primaryBtn.clicked.connect(lambda: print("Primary button clicked!"))
        self.changePasswordBtn.clicked.connect(lambda: print("Change password clicked!"))
        self.exportBackupBtn.clicked.connect(lambda: print("Export backup codes clicked!"))
        
        # Sliders
        self.slider.valueChanged.connect(lambda v: print(f"Basic slider value: {v}"))
        self.volumeSlider.valueChanged.connect(lambda v: print(f"Volume: {v}"))
        self.brightnessSlider.valueChanged.connect(lambda v: print(f"Brightness: {v}"))
        self.masterVolumeSlider.valueChanged.connect(lambda v: print(f"Master volume: {v}"))
        
        # Quality combo
        self.qualityCombo.currentTextChanged.connect(lambda text: print(f"Audio quality: {text}"))

    def __setTheme(self, theme):
        """Set application theme"""
        setTheme(theme)
        print(f"Theme changed to: {theme}")

    def __onLanguageChanged(self, language):
        """Handle language change"""
        print(f"Language changed to: {language}")

    def __onNotificationToggle(self, checked):
        """Handle notification toggle"""
        print(f"Notifications {'enabled' if checked else 'disabled'}")

    def __onAutoUpdateToggle(self, checked):
        """Handle auto update toggle"""
        print(f"Auto update {'enabled' if checked else 'disabled'}")

    def __onTwoFactorToggle(self, checked):
        """Handle two-factor authentication toggle"""
        print(f"Two-factor authentication {'enabled' if checked else 'disabled'}")

    def __onAutoLoginToggle(self, checked):
        """Handle auto login toggle"""
        print(f"Remember login {'enabled' if checked else 'disabled'}")


class MainWindow(QWidget):
    """Main demo window"""

    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        self.__initUI()

    def __initUI(self):
        """Initialize UI"""
        self.setWindowTitle("Expand Setting Cards Demo - PyQt-Fluent-Widgets")
        self.setWindowIcon(QIcon(":/qfluentwidgets/images/logo.png"))
        self.resize(900, 800)
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create demo widget
        self.demo = ExpandSettingDemo(self)
        layout.addWidget(self.demo)
        
        # Set style
        self.__setQss()

    def __setQss(self):
        """Set stylesheet"""
        color = 'dark' if isDarkTheme() else 'light'
        # Basic styling for the demo
        self.setStyleSheet(f"""
            QWidget#mainWindow {{
                background-color: {'#202020' if isDarkTheme() else '#fafafa'};
            }}
            QWidget#expandSettingDemo {{
                background-color: transparent;
                border: none;
            }}
        """)


if __name__ == '__main__':
    # Enable DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    
    # Uncomment to test with dark theme
    # setTheme(Theme.DARK)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
