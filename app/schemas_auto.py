from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Add(BaseModel):
    AddCode: str | None
    AddDescription: str | None

    class Config:
        orm_mode = True

class BarCodePool(BaseModel):
    ID: int | None
    TxNumber: str | None
    DateOfEntry: datetime | None
    SKU: str | None
    Qty: int | None

    class Config:
        orm_mode = True

class Branch(BaseModel):
    BranchCode: str | None
    BranchName: str | None
    ContactPerson: str | None
    JobTitle: str | None
    Address1: str | None
    Address2: str | None
    City: str | None
    Province: str | None
    PostalCode: str | None
    Country: str | None
    Phone: str | None
    Fax: str | None
    SummaryFlag: bool | None

    class Config:
        orm_mode = True

class BranchInventory(BaseModel):
    BranchCode: str | None
    SKU: str | None
    QtyOnHand: int | None

    class Config:
        orm_mode = True

class BranchSummary(BaseModel):
    BranchCode: str | None
    Year: int | None
    Month: int | None
    FirstDateOfMonth: datetime | None
    QtyBF: int | None
    AmtBF: Decimal | None
    QtyCD: int | None
    AmtCD: Decimal | None
    QtySold: int | None
    AmtSold: Decimal | None
    AmtCostOfGoodsSold: Decimal | None
    QtyPurchased: int | None
    AmtPurchased: Decimal | None
    QtyAdjustIncr: int | None
    AmtAdjustIncr: Decimal | None
    QtyAdjustDecr: int | None
    AmtAdjustDecr: Decimal | None
    QtyRejected: int | None
    AmtRejected: Decimal | None
    QtyRestocked: int | None
    AmtRestocked: Decimal | None
    QtyTransferIn: int | None
    AmtTransferIn: Decimal | None
    QtyTransferOut: int | None
    AmtTransferOut: Decimal | None

    class Config:
        orm_mode = True

class Brand(BaseModel):
    BrandCode: str | None
    BrandDescription: str | None

    class Config:
        orm_mode = True

class Category(BaseModel):
    DepartmentCode: str | None
    ClassCode: str | None
    CategoryCode: str | None
    CostingMethod: str | None
    InventoryMethod: str | None
    TaxMethod: str | None
    CategoryName: str | None
    SummaryFlag: bool | None

    class Config:
        orm_mode = True

class CategorySummary(BaseModel):
    DepartmentCode: str | None
    ClassCode: str | None
    CategoryCode: str | None
    Year: int | None
    Month: int | None
    FirstDateOfMonth: datetime | None
    QtyBF: int | None
    AmtBF: Decimal | None
    QtyCD: int | None
    AmtCD: Decimal | None
    QtySold: int | None
    AmtSold: Decimal | None
    AmtCostOfGoodsSold: Decimal | None
    QtyPurchased: int | None
    AmtPurchased: Decimal | None
    QtyAdjustedIncr: int | None
    AmtAdjustedIncr: Decimal | None
    QtyAdjustedDecr: int | None
    AmtAdjustedDecr: Decimal | None
    QtyRejected: int | None
    AmtRejected: Decimal | None
    QtyRestocked: int | None
    AmtRestocked: Decimal | None
    QtyTransferIn: int | None
    AmtTransferIn: Decimal | None
    QtyTransferOut: int | None
    AmtTransferOut: Decimal | None

    class Config:
        orm_mode = True

class City(BaseModel):
    Code: int | None
    CityName: str | None
    ProvinceCode: str | None
    CountryCode: str | None
    CityPhoneCode: str | None

    class Config:
        orm_mode = True

class Class(BaseModel):
    Department: str | None
    ClassCode: str | None
    ClassName: str | None
    SummaryFlag: bool | None

    class Config:
        orm_mode = True

class ClassSummary(BaseModel):
    DepartmentCode: str | None
    ClassCode: str | None
    Year: int | None
    Month: int | None
    FirstDateOfMonth: datetime | None
    QtyBF: int | None
    AmtBF: Decimal | None
    QtyCD: int | None
    AmtCD: Decimal | None
    QtySold: int | None
    AmtSold: Decimal | None
    AmtCostOfGoodsSold: Decimal | None
    QtyPurchased: int | None
    AmtPurchased: Decimal | None
    QtyAdjustedIncr: int | None
    AmtAdjustedIncr: Decimal | None
    QtyAdjustedDecr: int | None
    AmtAdjustedDecr: Decimal | None
    QtyRejected: int | None
    AmtRejected: Decimal | None
    QtyRestocked: int | None
    AmtRestocked: Decimal | None
    QtyTransferIn: int | None
    AmtTransferIn: Decimal | None
    QtyTransferOut: int | None
    AmtTransferOut: Decimal | None

    class Config:
        orm_mode = True

class CostingMethod(BaseModel):
    CostingCode: str | None
    CostingName: str | None

    class Config:
        orm_mode = True

class Country(BaseModel):
    CountryName: str | None
    CountryCode: str | None
    CountryPhoneCode: str | None

    class Config:
        orm_mode = True

class Customer(BaseModel):
    ID: int | None
    VIPCode: str | None
    FirstName: str | None
    Initial: str | None
    LastName: str | None
    FullName: str | None
    Salutation: str | None
    Birthday: datetime | None
    HomeAddress: str | None
    HomeCity: int | None
    HomeProvince: str | None
    HomePostalCode: str | None
    HomeCountry: str | None
    HomePhone: str | None
    HomeFax: str | None
    Cellular: str | None
    Email: str | None
    BizCompanyName: str | None
    BizJobTitle: str | None
    BizAddress: str | None
    BizCity: int | None
    BizProvince: str | None
    BizPostalCode: str | None
    BizCountry: str | None
    BizPhone: str | None
    BizFax: str | None
    CreditLimit: Decimal | None
    PaymentTerms: str | None
    VIPMarkDownPct: float | None
    SummaryFlag: bool | None
    AccountingFlag: bool | None
    Remarks: str | None

    class Config:
        orm_mode = True

class CustomerAccounts(BaseModel):
    CustomerID: int | None
    JointDate: datetime | None
    TtlAmtPurchased: Decimal | None
    TtlAmtRefund: Decimal | None
    TtlAmtMrkdwnApplied: Decimal | None
    TtlAmtCpnUsed: Decimal | None
    YTDAmtPurchased: Decimal | None
    YTDAmtRefund: Decimal | None
    YTDAmtMrkdwnApplied: Decimal | None
    YTDAmtCpnUsed: Decimal | None
    LastPurchaseDate: datetime | None

    class Config:
        orm_mode = True

class CustomerMedical(BaseModel):
    CustomerID: int | None
    InsMaturityDate: datetime | None
    CareCardNo: str | None
    CareCardValidPeriod: str | None
    CareCardType: str | None
    PrescriptionLensFlag: bool | None
    PrescriptionContactFlag: bool | None

    class Config:
        orm_mode = True

class CustomerPresContact(BaseModel):
    CustomerID: int | None
    IssuedOn: datetime | None
    IssuedByDr: int | None
    RightSphere: float | None
    RightCylinder: float | None
    RightAxis: int | None
    RightKReadingV: float | None
    RightKReadingH: float | None
    RightPalp: float | None
    RightCorn: float | None
    RightPupil: float | None
    LeftSphere: float | None
    LeftCylinder: float | None
    LeftAxis: int | None
    LeftKReadingV: float | None
    LeftKReadingH: float | None
    LeftPalp: float | None
    LeftCorn: float | None
    LeftPupil: float | None
    History: str | None
    Medical: str | None
    Allergy: str | None
    Reason: str | None
    Evaluation: str | None
    Test: str | None

    class Config:
        orm_mode = True

class CustomerPresLens(BaseModel):
    CustomerID: int | None
    IssuedOn: datetime | None
    IssuedByDr: int | None
    RightSphere: float | None
    RightCylinder: float | None
    RightAxis: int | None
    RightPdDist: float | None
    RightPdNear: float | None
    RightPrism: float | None
    RightAdd: float | None
    RightPupil: float | None
    LeftSphere: float | None
    LeftCylinder: float | None
    LeftAxis: int | None
    LeftPdDist: float | None
    LeftPdNear: float | None
    LeftPrism: float | None
    LeftAdd: float | None
    LeftPupil: float | None

    class Config:
        orm_mode = True

class Department(BaseModel):
    DepartmentCode: str | None
    DepartmentName: str | None
    SummaryFlag: bool | None

    class Config:
        orm_mode = True

class DeptSummary(BaseModel):
    DepartmentCode: str | None
    Year: int | None
    Month: int | None
    FirstDateOfMonth: datetime | None
    QtyBF: int | None
    AmtBF: Decimal | None
    QtyCD: int | None
    AmtCD: Decimal | None
    QtySold: int | None
    AmtSold: Decimal | None
    AmtCostOfGoodsSold: Decimal | None
    QtyPurchased: int | None
    AmtPurchased: Decimal | None
    QtyAdjustedIncr: int | None
    AmtAdjustedIncr: Decimal | None
    QtyAdjustedDecr: int | None
    AmtAdjustedDecr: Decimal | None
    QtyRejected: int | None
    AmtRejected: Decimal | None
    QtyRestocked: int | None
    AmtRestocked: Decimal | None
    QtyTransferIn: int | None
    AmtTransferIn: Decimal | None
    QtyTransferOut: int | None
    AmtTransferOut: Decimal | None

    class Config:
        orm_mode = True

class Doctor(BaseModel):
    ID: int | None
    DoctorName: str | None
    Address: str | None
    City_: int | None
    Province: str | None
    Country_: str | None
    Phone: str | None
    PostalCode: str | None
    Fax: str | None
    Emergency: str | None

    class Config:
        orm_mode = True

class Footer(BaseModel):
    FooterCode: str | None
    FooterDescription: str | None
    FooterNote: str | None

    class Config:
        orm_mode = True

class Hardening(BaseModel):
    ID: int | None
    Name: str | None

    class Config:
        orm_mode = True

class Inventory(BaseModel):
    DepartmentCode: str | None
    ClassCode: str | None
    CategoryCode: str | None
    SupplierCode: str | None
    BrandCode: str | None
    SKU: str | None
    Model: str | None
    Color: str | None
    Size: str | None
    Bridge: int | None
    Temple: int | None
    AddCode: str | None
    MaterialCode: str | None
    Sphere: float | None
    Cylinder: float | None
    Axis: int | None
    BaseCurve: float | None
    Diameter: float | None
    Name: str | None
    Description: str | None
    Remarks: str | None
    ABCGrading: str | None
    InventoryType: str | None
    InventoryStatus: str | None
    KitSetFlag: bool | None
    AverageCost: Decimal | None
    ReOrderLevel: int | None
    ReOrderQty: int | None
    QtyTotalOnHand: int | None
    QtySaleOrder: int | None
    QtyPurchaseOrder: int | None
    QtyHolded: int | None
    QtyInTransit: int | None
    DateLastIssued: datetime | None
    DateLastReceived: datetime | None
    RetailPriceFlag: bool | None
    WholeSalePriceFlag: bool | None
    InventoryLotFlag: bool | None

    class Config:
        orm_mode = True

class InvtLotRecord(BaseModel):
    SKU: str | None
    LotNo: str | None
    SupplierCode: str | None
    DateReceived: datetime | None
    QtyPurchased: int | None
    QtyUsed: int | None
    QtyOnHand: int | None
    UnitAmountPurchased: Decimal | None
    TotalAmountPurchased: Decimal | None

    class Config:
        orm_mode = True

class InvtMethod(BaseModel):
    InvtMethodCode: str | None
    InvtMethodName: str | None

    class Config:
        orm_mode = True

class InvtSTDetails(BaseModel):
    ID: int | None
    HeaderID: int | None
    SKU: str | None
    ComputerQty: float | None
    PhysicalQty: float | None
    DiffQty: float | None
    AverageCost: Decimal | None

    class Config:
        orm_mode = True

class InvtSTHeader(BaseModel):
    ID: int | None
    Name: str | None
    DateOfCreation: datetime | None
    DateOfUpdate: datetime | None
    DateOfPurge: datetime | None
    Status: int | None

    class Config:
        orm_mode = True

class InvtSTImport(BaseModel):
    HeaderID: int | None
    SKU: str | None
    Qty: int | None
    Status: int | None

    class Config:
        orm_mode = True

class InvtSTStatus(BaseModel):
    Code: int | None
    Name: str | None

    class Config:
        orm_mode = True

class InvtSummary(BaseModel):
    SKU: str | None
    Year: int | None
    Month: int | None
    FirstDateOfMonth: datetime | None
    QtyBF: int | None
    AmtBF: Decimal | None
    QtyCD: int | None
    AmtCD: Decimal | None
    QtySold: int | None
    AmtSold: Decimal | None
    AmtCostOfGoodsSold: Decimal | None
    QtyPurchased: int | None
    AmtPurchased: Decimal | None
    QtyAdjIncr: int | None
    AmtAdjIncr: Decimal | None
    QtyAdjDecr: int | None
    AmtAdjDecr: Decimal | None
    QtyRejected: int | None
    AmtRejected: Decimal | None
    QtyRestocked: int | None
    AmtRestocked: Decimal | None
    QtyTransferIn: int | None
    AmtTransferIn: Decimal | None
    QtyTransferOut: int | None
    AmtTransferOut: Decimal | None

    class Config:
        orm_mode = True

class JobNature(BaseModel):
    Code: str | None
    Name: str | None

    class Config:
        orm_mode = True

class JobStatus(BaseModel):
    Code: str | None
    Name: str | None

    class Config:
        orm_mode = True

class JobTitle(BaseModel):
    JobTitleCode: str | None
    JobTitle: str | None

    class Config:
        orm_mode = True

class MaritalStatus(BaseModel):
    Code: str | None
    MaritalStatus: str | None

    class Config:
        orm_mode = True

class Material(BaseModel):
    MaterialCode: str | None
    MaterialDescription: str | None

    class Config:
        orm_mode = True

class PayPer(BaseModel):
    Code: str | None
    Name: str | None

    class Config:
        orm_mode = True

class PayPeriod(BaseModel):
    Code: str | None
    Name: str | None

    class Config:
        orm_mode = True

class PaymentMethods(BaseModel):
    PaymentCode: str | None
    PaymentNameShort: str | None
    PaymentNameLong: str | None
    ExchangeRate: float | None
    RevisedDate: datetime | None
    TodayAmtOpening: Decimal | None
    TodayAmtClosing: Decimal | None
    TodayAmtSold: Decimal | None
    TodayNumberOfSold: int | None
    TodayAmtRefund: Decimal | None
    TodayNumberOfRefund: int | None
    TodayAmtChanged: Decimal | None
    TodayNumberOfChange: int | None
    TodayAmtPaidOut: Decimal | None
    TodayNumberOfPaidOut: int | None
    TodayAmtBankIn: Decimal | None
    TodayNumberOfBankIn: int | None
    AlertLevel: Decimal | None

    class Config:
        orm_mode = True

class PaymentSummary(BaseModel):
    PaymentCode: str | None
    Date: datetime | None
    ExchangeRate: int | None
    AmtOpening: Decimal | None
    AmtClosing: Decimal | None
    AmtSold: Decimal | None
    NumberOfSold: int | None
    AmtRefund: Decimal | None
    NumberOfRefund: int | None
    AmtChanged: Decimal | None
    NumberOfChange: int | None
    AmtPaidOut: Decimal | None
    NumberOfPaidOut: int | None
    AmtBankIn: Decimal | None
    NumberOfBankIn: int | None

    class Config:
        orm_mode = True

class PrefTxNumber(BaseModel):
    TxPrefix: str | None
    TxNextNumber: int | None
    Description: str | None
    Value: str | None
    Remarks: str | None

    class Config:
        orm_mode = True

class Preference(BaseModel):
    Serial_Number: str | None
    NumberOfUser: int | None
    Paltform: str | None
    ProductName: str | None
    UserName: str | None
    OwnerName: str | None
    BranchNumber: str | None
    PSTNumber: str | None
    GSTNumber: str | None
    NextInvtControlNumber: int | None
    NextInvtSKU: int | None
    NextInvoiceNumber: int | None
    NextSalesOrderNumber: int | None
    DateOfInstallation: datetime | None
    UserAddress: str | None
    UserCity: int | None
    UserProvince: str | None
    UserPostalCode: str | None
    UserCountry: str | None
    UserPhone: str | None
    UserFax: str | None
    UserContactPerson: str | None
    OwnerAddress: str | None
    OwnerCity: int | None
    OwnerProvince: str | None
    OwnerPostalCode: str | None
    OwnerCountry: str | None
    OwnerPhone: str | None
    OwnerFax: str | None
    OwnerContactPerson: str | None
    CountryCode: str | None
    TaxARate: float | None
    TaxBRate: float | None
    FiscalPeriod: datetime | None
    CurrentMonth: datetime | None

    class Config:
        orm_mode = True

class Province(BaseModel):
    ProvinceName: str | None
    ProvinceCode: str | None

    class Config:
        orm_mode = True

class ReBuildCost(BaseModel):
    SKU: str | None
    AverageCost: Decimal | None
    LSP: Decimal | None

    class Config:
        orm_mode = True

class Remarks(BaseModel):
    RemarksCode: str | None
    RemarksDescription: str | None
    RemarksNote: str | None

    class Config:
        orm_mode = True

class RetailPrice(BaseModel):
    SKU: str | None
    LeastSellingPrice: Decimal | None
    RetailPrice: Decimal | None
    RetailMarkDownAmt: Decimal | None
    RetailmarkDownPct: float | None

    class Config:
        orm_mode = True

class SalesOrderStatus(BaseModel):
    Code: str | None
    Name: str | None

    class Config:
        orm_mode = True

class Salutation(BaseModel):
    Salutation: str | None

    class Config:
        orm_mode = True

class Security(BaseModel):
    LeveL: int | None
    Point_of_Sale: bool | None
    Inventory_Control: bool | None
    OLAP: bool | None
    Information_Centre: bool | None
    Coding: bool | None
    Report_Centre: bool | None
    Preference_: bool | None
    Cost: bool | None

    class Config:
        orm_mode = True

class Sex(BaseModel):
    Code: str | None
    Sex: str | None

    class Config:
        orm_mode = True

class Staff(BaseModel):
    StaffCode: str | None
    SecurityLevel: int | None
    DateHired: datetime | None
    SIN: str | None
    StaffFirstName: str | None
    StaffLastName: str | None
    StaffFullName: str | None
    StaffInitial: str | None
    JobTitle_: str | None
    JobStatus_: str | None
    JobNature_: str | None
    Password: str | None
    DateLeaved: datetime | None
    Birthday: datetime | None
    Sex_: str | None
    MaritalStatus_: str | None
    HomeAddress: str | None
    HomeCity: int | None
    HomeProvince: str | None
    HomeCountry: str | None
    HomePostalCode: str | None
    HomePhone: str | None
    HomeFax: str | None
    SalaryBasic: Decimal | None
    SalaryPer: str | None
    SalaryPayPeriod: str | None
    BankAccount: str | None
    CommissionRate: int | None
    CommissionBonus: int | None
    CommissionGeneral: int | None

    class Config:
        orm_mode = True

class StaffHistory(BaseModel):
    StaffCode: str | None
    Date: datetime | None
    Remarks_: str | None
    Reason: str | None

    class Config:
        orm_mode = True

class Supplier(BaseModel):
    SupplierCode: str | None
    SupplierName: str | None
    Address: str | None
    City_: int | None
    Province_: str | None
    PostCode: str | None
    Country_: str | None
    PhoneGenVoice: str | None
    PhoneGenFax: str | None
    PhoneACDeptExt: str | None
    PhoneACDeptFax: str | None
    PhoneSaleExt: str | None
    PhoneSaleFax: str | None
    PhoneServiceExt: str | None
    PhoneServiceFax: str | None
    AccountNo: str | None
    DateStarted: datetime | None
    CreditLimit: Decimal | None
    PaymentTerms: str | None
    ContactPerson: str | None
    ContactPersonFlag: str | None
    SummaryFlag: str | None
    BranchFlag: str | None
    Remarks_: str | None
    GSTNumber: str | None
    PSTNumber: str | None
    TollFreePhone1: str | None
    TollFreePhone2: str | None
    TollFreeFax1: str | None
    TollFreeFax2: str | None

    class Config:
        orm_mode = True

class SupplierContactPerson(BaseModel):
    SupCode: str | None
    FirstName: str | None
    Initial: str | None
    LastName: str | None
    FullName: str | None
    Salutation_: str | None
    JobTitle_: str | None
    PhoneGeneralVoice: str | None
    PhoneGeneralFax: str | None
    PhoneHome: str | None
    PhoneMobile: str | None
    PhonePager: str | None
    PhoneWork: str | None

    class Config:
        orm_mode = True

class SupplierSummary(BaseModel):
    SupplierCode: str | None
    Year: int | None
    Month: int | None
    FirstDateOfMonth: datetime | None
    QtyPurchased: int | None
    AmtPurchased: Decimal | None
    QtyRejected: int | None
    AmtRejected: Decimal | None

    class Config:
        orm_mode = True

class TxDetails(BaseModel):
    ControlNumber: str | None
    TxType: str | None
    TxNumber: str | None
    DateofEntry: datetime | None
    RowNo: float | None
    SKU: str | None
    Remarks_: str | None
    PrescriptionLensFlag: bool | None
    PrescriptionContactFlag: bool | None
    Qty: int | None
    UnitAmount: Decimal | None
    UnitCost: Decimal | None
    UnitLSP: Decimal | None
    MarkDownPercent: float | None
    MarkDownAmount: Decimal | None
    Amount: Decimal | None
    TaxCode: str | None

    class Config:
        orm_mode = True

class TxHeader(BaseModel):
    ControlNumber: str | None
    TxType: str | None
    TxNumber: str | None
    DateOfEntry: datetime | None
    DateOfCreation: datetime | None
    RefNumber: str | None
    TrackingNumber: str | None
    CustomerID: int | None
    SupplierCode: str | None
    SecondDate: datetime | None
    Particulars: str | None
    TotalCost: Decimal | None
    TotalSale: Decimal | None
    TaxA: Decimal | None
    TaxB: Decimal | None
    TaxC: Decimal | None
    OtherCharges: Decimal | None
    GrossSale: Decimal | None
    SalesDiscount: Decimal | None
    TotalAmount: Decimal | None
    TotalQty: int | None
    PreviousPaid: Decimal | None
    ThisPaid: Decimal | None
    Change: Decimal | None
    PrintCounter: int | None
    PaymentLink: int | None
    SalesPersonLink: int | None
    Status: str | None

    class Config:
        orm_mode = True

class TxPayment(BaseModel):
    TxNumber: str | None
    PaymentLineNo: float | None
    Type: str | None
    CardNumber: str | None
    AuthorizationCode: str | None
    AmountTender: Decimal | None
    ExchangeRate: float | None
    EqAmount: Decimal | None
    TotalThisPay: Decimal | None

    class Config:
        orm_mode = True

class TxSOrderAdd(BaseModel):
    TxNumber: str | None
    LineNumber: float | None
    Supplier_: str | None
    Brand_: str | None
    Model: str | None

    class Config:
        orm_mode = True

class TxSOrderCont(BaseModel):
    TxNumber: str | None
    LineNumber: float | None
    IssuedOn: datetime | None
    IssuedBy: int | None
    RightSphere: float | None
    RightCylinder: float | None
    RightAxis: int | None
    RightKReadingV: float | None
    RightKReadingH: float | None
    RightPalp: float | None
    RightCorn: float | None
    RightPupil: float | None
    LeftSphere: float | None
    LeftCylinder: float | None
    LeftAxis: int | None
    LeftKReadingV: float | None
    LeftKReadingH: float | None
    LeftPalp: float | None
    LeftCorn: float | None
    LeftPupil: float | None
    History: str | None
    Medical: str | None
    Allergy: str | None
    Reason: str | None
    Evaluation: str | None
    Test: str | None
    SpecialInstruction: str | None

    class Config:
        orm_mode = True

class TxSOrderExtra(BaseModel):
    TxNumber: str | None
    Redo: bool | None
    Warranty: bool | None
    Mail: bool | None
    Msd: bool | None
    Remarks_: int | None

    class Config:
        orm_mode = True

class TxSOrderFrame(BaseModel):
    TxNumber: str | None
    LineNumber: float | None
    Supply: bool | None
    Enclosed: bool | None
    Follow: bool | None
    Lenses: bool | None
    Mode: str | None
    Color: str | None
    EyeSize: str | None
    Bridge: int | None
    Temple: int | None
    R1: str | None
    R2: str | None
    R3: str | None
    A: str | None
    B: str | None
    SpecialInstruction: str | None

    class Config:
        orm_mode = True

class TxSOrderLens(BaseModel):
    TxNumber: str | None
    LineNumber: float | None
    IssuedOn: datetime | None
    IssuedBy: int | None
    RightSphere: float | None
    RightCylinder: float | None
    RightAxis: int | None
    RightPdDist: float | None
    RightPdNear: float | None
    RightPrism: float | None
    RightAdd: float | None
    RightPupil: float | None
    RightStyle: str | None
    RightSegHt: float | None
    RigthOC: float | None
    RigthBase: float | None
    RightVD: float | None
    LeftSphere: float | None
    LeftCylinder: float | None
    LeftAxis: int | None
    LeftPdDist: float | None
    LeftPdNear: float | None
    LeftPrism: float | None
    LeftAdd: float | None
    LeftPupil: float | None
    LeftStyle: str | None
    LeftSegHt: float | None
    LeftOC: float | None
    LeftBase: float | None
    LeftVD: float | None
    Type: str | None
    Hardening_: str | None
    Material_: str | None
    Coating: str | None
    Tint: str | None
    Others: str | None
    HardCoat: bool | None
    ARCoat: bool | None
    UV: bool | None

    class Config:
        orm_mode = True

class TxSalePerson(BaseModel):
    TxNumber: str | None
    SalesRowNo: float | None
    StaffCode: str | None

    class Config:
        orm_mode = True

class Users(BaseModel):
    id: int | None
    email: str | None
    hashed_password: str | None
    is_active: bool | None

    class Config:
        orm_mode = True

class UtilCheckLog(BaseModel):
    LogNumber: int | None
    DateOfLog: datetime | None
    ParentTable: str | None
    ParentKey: str | None
    Remarks_: str | None

    class Config:
        orm_mode = True

class WholesalePrice(BaseModel):
    SKU: str | None
    SuggestedRetailPrice: Decimal | None
    SellingPriceGradeA: Decimal | None
    SellingPriceGradeB: Decimal | None
    SellingPriceGradeC: Decimal | None

    class Config:
        orm_mode = True

class ZDefaultClass(BaseModel):
    Code: str | None
    Name: str | None

    class Config:
        orm_mode = True

class ZDefaultRemarks(BaseModel):
    ID: int | None
    Group: int | None
    Remarks_: str | None

    class Config:
        orm_mode = True

