class TestData:

    # Options driver_Path, driver_manager, driver_environment
    DRIVER_SELECTION = 'driver_Path'
    BROWSER = 'chrome'
    CHROME_EXECUTABLE_PATH = "browserDrivers/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "browserDrivers/geckodriver.exe"

    URL = "https://www.inspire.com/"
    USERNAME = "srinivas.anand1@gmail.com"
    PASSWORD = "Srinivas@12345"
    USERNAME = "QA_candidate_SrinivasAnand"

    PLATFORM = 'ANDROID'

    # Database Connection
    HOST_NAME = "localhost"
    DATABASE_NAME = "postgres"
    USER_NAME = "postgres"
    USER_PASSWORD = "postgressdb"
    PORT_NUMBER = "5432"

    IMPLICIT_WAIT = 30

    # Database Queries
    Create_emp_Table = """
    create table emp(
    emp_id int primary key,
    emp_name varchar(30) not null,
    emp_address varchar(50),
    emp_doj date,
    emp_department int);
    """
    data_emp = """
    insert into emp values
    (101, 'Steve', 'bangalore','2019-02-10', 1),
    (102, 'Jos', 'bangalore','2019-02-10', 1),
    (103, 'Kate', 'bangalore','2019-02-10', 2),
    (104, 'Stacy', 'bangalore','2019-02-10', 2),
    (105, 'Nancy', 'bangalore','2019-02-10', 2),
    (106, 'Maria', 'bangalore','2019-02-10', 3),
    (107, 'Danny', 'bangalore','2019-02-10', 3),
    (108, 'Joseph', 'bangalore','2019-02-10', 3),
    (109, 'Mark', 'Pune','2019-02-10', 4),
    (110, 'Satish', 'Pune','2019-02-10', 4)
    """
    query1 = """
    select * from emp;
    """
    query1 = """
        select * from emp where emp_name like 'S%';
        """