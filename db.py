import pymysql

# Establish a database connection
connect = pymysql.connect(host="localhost", user='your_user', password='your_password', database='your_database')

try:
    # Check if the 'user' table exists
    with connect.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'user'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create the 'user' table
            create_table_query = """
            CREATE TABLE user (
                id VARCHAR(500) PRIMARY KEY,
                limit_usertest INT(100) NOT NULL,
                roll_Status BOOLEAN NOT NULL,
                Processing_value VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
                Processing_value_one VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
                Processing_value_tow VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
                Processing_value_four VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
                step VARCHAR(1000) NOT NULL,
                description_blocking TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                number VARCHAR(2000) NOT NULL,
                Balance INT(255) NOT NULL,
                User_Status VARCHAR(500) NOT NULL,
                pagenumber INT(10) NOT NULL,
                message_count VARCHAR(100) NOT NULL,
                last_message_time VARCHAR(100) NOT NULL,
                affiliatescount VARCHAR(100) NOT NULL,
                affiliates VARCHAR(100) NOT NULL,
                username VARCHAR(1000) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """
            cursor.execute(create_table_query)

            # Commit changes to the database
            connect.commit()

        else:
            # Check if 'affiliatescount' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'affiliatescount'")
            if cursor.rowcount != 1:
                # Add 'affiliatescount' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD affiliatescount VARCHAR(100)")
                cursor.execute("UPDATE user SET affiliatescount = '0'")
                print("The affiliatescount field was added ✅")

            # Check if 'affiliates' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'affiliates'")
            if cursor.rowcount != 1:
                # Add 'affiliates' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD affiliates VARCHAR(100)")
                cursor.execute("UPDATE user SET affiliates = '0'")
                print("The affiliates field was added ✅")
            
            cursor.execute("SHOW COLUMNS FROM user LIKE 'message_count'")
            if cursor.rowcount != 1:
                # Add 'message_count' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD message_count VARCHAR(100)")
                cursor.execute("UPDATE user SET message_count = '0'")
                print("The message_count field was added ✅")

            # Check if 'last_message_time' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'last_message_time'")
            if cursor.rowcount != 1:
                # Add 'last_message_time' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD last_message_time VARCHAR(100)")
                cursor.execute("UPDATE user SET last_message_time = '0'")
                print("The last_message_time field was added ✅")

            # Check if 'Processing_value_four' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'Processing_value_four'")
            if cursor.rowcount != 1:
                # Add 'Processing_value_four' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD Processing_value_four VARCHAR(100)")
                print("The Processing_value_four field was added ✅")

            # Check if 'username' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'username'")
            if cursor.rowcount != 1:
                # Add 'username' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD username VARCHAR(1000)")
                cursor.execute("UPDATE user SET username = 'none'")
                print("The username field was added ✅")

            # Check if 'Processing_value' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'Processing_value'")
            if cursor.rowcount != 1:
                # Add 'Processing_value' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD Processing_value VARCHAR(1000)")
                cursor.execute("UPDATE user SET Processing_value = 'none'")
                print("The Processing_Value field was added ✅")

            cursor.execute("SHOW COLUMNS FROM user LIKE 'Processing_value_tow'")
            if cursor.rowcount != 1:
                # Add 'Processing_value_tow' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD Processing_value_tow VARCHAR(1000)")
                cursor.execute("UPDATE user SET Processing_value_tow = 'none'")
                print("The Processing_value_tow field was added ✅")

            # Check if 'Processing_value_one' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'Processing_value_one'")
            if cursor.rowcount != 1:
                # Add 'Processing_value_one' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD Processing_value_one VARCHAR(1000)")
                cursor.execute("UPDATE user SET Processing_value_one = 'none'")
                print("The Processing_value_one field was added ✅")

            # Check if 'Balance' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'Balance'")
            if cursor.rowcount != 1:
                # Add 'Balance' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD Balance INT(255)")
                cursor.execute("UPDATE user SET Balance = '0'")
                print("The Balance field was added ✅")

            # Check if 'number' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'number'")
            if cursor.rowcount != 1:
                # Add 'number' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD number VARCHAR(1000)")
                cursor.execute("UPDATE user SET number = 'none'")
                print("The number field was added ✅")
                
            cursor.execute("SHOW COLUMNS FROM user LIKE 'roll_Status'")
            if cursor.rowcount != 1:
                # Add 'roll_Status' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD roll_Status BOOLEAN")
                cursor.execute("UPDATE user SET roll_Status = false")
                print("The roll_Status field was added ✅")

            # Check if 'description_blocking' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'description_blocking'")
            if cursor.rowcount != 1:
                # Add 'description_blocking' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD description_blocking VARCHAR(5000)")
                print("The description_blocking field was added ✅")

            # Check if 'User_Status' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'User_Status'")
            if cursor.rowcount != 1:
                # Add 'User_Status' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD User_Status VARCHAR(500)")
                print("The User_Status field was added ✅")

            # Check if 'pagenumber' field exists
            cursor.execute("SHOW COLUMNS FROM user LIKE 'pagenumber'")
            if cursor.rowcount != 1:
                # Add 'pagenumber' field to the 'user' table
                cursor.execute("ALTER TABLE user ADD pagenumber INT(10)")
                print("The pagenumber field was added ✅")
            
            # Commit changes to the database
            connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))

try:
    # Check if the 'help' table exists
    with connect.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'help'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create the 'help' table
            create_table_query = """
            CREATE TABLE help (
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                name_os VARCHAR(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
                Media_os VARCHAR(5000) NOT NULL,
                type_Media_os VARCHAR(500) NOT NULL,
                Description_os TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """
            cursor.execute(create_table_query)

            # Commit changes to the database
            connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))

try:
    # Check if the 'setting' table exists
    with connect.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'setting'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create the 'setting' table
            create_table_query = """
            CREATE TABLE setting (
                Bot_Status VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                help_Status VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                roll_Status VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                get_number VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                iran_number VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                sublink VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                NotUser VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                configManual VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                Channel_Report VARCHAR(600) NULL,
                limit_usertest_all VARCHAR(600) NULL,
                time_usertest VARCHAR(600) NULL,
                val_usertest VARCHAR(600) NULL,
                flow VARCHAR(600) NULL,
                Extra_volume VARCHAR(600) NULL,
                MethodUsername VARCHAR(900) NULL,
                namecustome VARCHAR(100) NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """
            cursor.execute(create_table_query)

            # Insert initial values into the 'setting' table
            active_bot_text = "✅  ربات روشن است"
            active_roll_text = "❌ تایید قوانین خاموش است"
            active_phone_text = "❌ احرازهویت شماره تماس غیرفعال است"
            active_phone_iran_text = "❌ بررسی شماره ایرانی غیرفعال است"
            active_help = "❌ آموزش غیرفعال است"
            sublink = "✅ لینک اشتراک فعال است."
            config_manual = "❌ ارسال کانفیگ دستی خاموش است"
            method_username = "آیدی عددی + حروف و عدد رندوم"

            cursor.execute("""
                INSERT INTO setting 
                (Bot_Status, roll_Status, get_number, limit_usertest_all, time_usertest, val_usertest, help_Status, iran_number, 
                sublink, configManual, NotUser, MethodUsername, flow, namecustome) 
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (active_bot_text, active_roll_text, active_phone_text, '1', '1', '100', active_help,
                  active_phone_iran_text, sublink, config_manual, 'offnotuser', method_username, 'offflow', '0'))

            print("The setting table was created and initial values were inserted ✅")

            # Commit changes to the database
            connect.commit()

        else:
            # Check if 'namecustome' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'namecustome'")
            if cursor.rowcount != 1:
                # Add 'namecustome' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD namecustome VARCHAR(100)")
                print("The namecustome field was added ✅")

            # Check if 'namecustome' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'namecustome'")
            if cursor.rowcount != 1:
                # Add 'namecustome' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD namecustome VARCHAR(200)")
                print("The namecustome field was added ✅")

            # Check if 'Extra_volume' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'Extra_volume'")
            if cursor.rowcount != 1:
                # Add 'Extra_volume' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD Extra_volume VARCHAR(200)")
                print("The Extra_volume field was added ✅")

            # Check if 'flow' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'flow'")
            if cursor.rowcount != 1:
                # Add 'flow' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD flow VARCHAR(200)")
                print("The flow field was added ✅")

            # Check if 'MethodUsername' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'MethodUsername'")
            if cursor.rowcount != 1:
                # Add 'MethodUsername' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD MethodUsername VARCHAR(900)")
                print("The MethodUsername field was added ✅")

            # Check if 'NotUser' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'NotUser'")
            if cursor.rowcount != 1:
                # Add 'NotUser' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD NotUser VARCHAR(200)")
                print("The NotUser field was added ✅")

            # Check if 'sublink' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'sublink'")
            if cursor.rowcount != 1:
                # Add 'sublink' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD sublink VARCHAR(200)")
                print("The sublink field was added ✅")

            # Check if 'iran_number' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'iran_number'")
            if cursor.rowcount != 1:
                # Add 'iran_number' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD iran_number VARCHAR(200)")
                print("The iran_number field was added ✅")

            # Check if 'get_number' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'get_number'")
            if cursor.rowcount != 1:
                # Add 'get_number' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD get_number VARCHAR(200)")
                print("The get_number field was added ✅")

            # Check if 'time_usertest' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'time_usertest'")
            if cursor.rowcount != 1:
                # Add 'time_usertest' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD time_usertest VARCHAR(600)")
                print("The time_usertest field was added ✅")

            # Check if 'val_usertest' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'val_usertest'")
            if cursor.rowcount != 1:
                # Add 'val_usertest' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD val_usertest VARCHAR(600)")
                print("The val_usertest field was added ✅")

            # Check if 'help_Status' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'help_Status'")
            if cursor.rowcount != 1:
                # Add 'help_Status' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD help_Status VARCHAR(600)")
                print("The help_Status field was added ✅")

            # Check if 'limit_usertest_all' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'limit_usertest_all'")
            if cursor.rowcount != 1:
                # Add 'limit_usertest_all' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD limit_usertest_all VARCHAR(600)")
                print("The limit_usertest_all field was added ✅")

            # Check if 'Channel_Report' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'Channel_Report'")
            if cursor.rowcount != 1:
                # Add 'Channel_Report' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD Channel_Report VARCHAR(200)")
                print("The Channel_Report field was added ✅")

            # Check if 'Bot_Status' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'Bot_Status'")
            if cursor.rowcount != 1:
                # Add 'Bot_Status' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD Bot_Status VARCHAR(200)")
                print("The Bot_Status field was added ✅")

            # Check if 'roll_Status' field exists
            cursor.execute("SHOW COLUMNS FROM setting LIKE 'roll_Status'")
            if cursor.rowcount != 1:
                # Add 'roll_Status' field to the 'setting' table
                cursor.execute("ALTER TABLE setting ADD roll_Status VARCHAR(200)")
                cursor.execute("UPDATE setting SET roll_Status = '✅ روشن '")
                print("The roll_Status field was added ✅")

            # Fetch settings from the 'setting' table
            cursor.execute("SELECT * FROM setting")
            settingsql = cursor.fetchone()

            # Update 'configManual' if not set
            if 'configManual' not in settingsql:
                cursor.execute("UPDATE setting SET configManual = %s", ("❌ ارسال کانفیگ دستی خاموش است",))

            # Update 'flow' if not set
            if 'flow' not in settingsql:
                cursor.execute("UPDATE setting SET flow = %s", ('offflow',))

            # Update 'iran_number' if not set
            if 'iran_number' not in settingsql:
                cursor.execute("UPDATE setting SET iran_number = %s", ("❌ بررسی شماره ایرانی غیرفعال است",))

            # Update 'sublink' if not set
            if 'sublink' not in settingsql:
                cursor.execute("UPDATE setting SET sublink = %s", ("✅ لینک اشتراک فعال است.",))

            # Update 'NotUser' if not set
            if 'NotUser' not in settingsql:
                cursor.execute("UPDATE setting SET NotUser = %s", ('offnotuser',))

            # Update 'MethodUsername' if not set
            if 'MethodUsername' not in settingsql:
                cursor.execute("UPDATE setting SET MethodUsername = %s", ("آیدی عددی + حروف و عدد رندوم",))

        
            # Commit changes to the database
            connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        

try:
    with connect.cursor() as cursor:
        # Check if 'admin' table exists
        cursor.execute("SHOW TABLES LIKE 'admin'")
        table_exists = cursor.rowcount > 0

        if table_exists:
            # Fetch existing admin ids from the 'admin' table
            cursor.execute("SELECT id_admin FROM admin")
            admin_ids = [row['id_admin'] for row in cursor.fetchall()]

            # Check if adminnumber is not in the admin_ids list
            if adminnumber not in admin_ids:
                # Insert adminnumber into the 'admin' table
                cursor.execute("INSERT INTO admin (id_admin) VALUES (%s)", (adminnumber,))
                print("Table admin updated ✅")

        else:
            # Create 'admin' table
            cursor.execute("CREATE TABLE admin (id_admin VARCHAR(200) PRIMARY KEY NOT NULL)")
            
            # Insert adminnumber into the newly created 'admin' table
            cursor.execute("INSERT INTO admin (id_admin) VALUES (%s)", (adminnumber,))
            print("Table admin created and updated ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
try:
    with connect.cursor() as cursor:
        # Check if 'channels' table exists
        cursor.execute("SHOW TABLES LIKE 'channels'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'channels' table
            cursor.execute("CREATE TABLE channels (Channel_lock VARCHAR(200) NOT NULL, link VARCHAR(200) NOT NULL)")

            # Commit changes to the database
            connect.commit()

            print("Table channels created ✅")

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))

try:
    with connect.cursor() as cursor:
        # Check if 'marzban_panel' table exists
        cursor.execute("SHOW TABLES LIKE 'marzban_panel'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'marzban_panel' table
            cursor.execute("""
                CREATE TABLE marzban_panel (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    name_panel VARCHAR(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    url_panel VARCHAR(2000) NULL,
                    username_panel VARCHAR(200) NULL,
                    vmess VARCHAR(200) NULL,
                    vless VARCHAR(200) NULL,
                    trojan VARCHAR(200) NULL,
                    shadowsocks VARCHAR(200) NULL,
                    password_panel VARCHAR(200) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table marzban_panel created ✅")

        else:
            # Check and add missing columns
            columns_to_add = [('shadowsocks', 'offshadowsocks'), ('vless', 'onvless'), ('vmess', 'onvmess'), ('trojan', 'ontrojan')]

            for column_name, default_value in columns_to_add:
                check_field_query = f"SHOW COLUMNS FROM marzban_panel LIKE '{column_name}'"
                cursor.execute(check_field_query)

                if cursor.rowcount != 1:
                    add_field_query = f"ALTER TABLE marzban_panel ADD {column_name} VARCHAR(100)"
                    cursor.execute(add_field_query)

                    update_default_value_query = f"UPDATE marzban_panel SET {column_name} = '{default_value}'"
                    cursor.execute(update_default_value_query)

                    print(f"The {column_name} field was added ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))


try:
    with connect.cursor() as cursor:
        # Check if 'product' table exists
        cursor.execute("SHOW TABLES LIKE 'product'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'product' table
            cursor.execute("""
                CREATE TABLE product (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    code_product VARCHAR(200) NULL,
                    name_product VARCHAR(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    price_product VARCHAR(2000) NULL,
                    Volume_constraint VARCHAR(2000) NULL,
                    Location VARCHAR(1000) NULL,
                    Service_time VARCHAR(200) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table product created ✅")

        else:
            # Check and add missing columns
            columns_to_add = [('Location', 'VARCHAR(1000)'), ('code_product', 'VARCHAR(200)')]

            for column_name, data_type in columns_to_add:
                check_field_query = f"SHOW COLUMNS FROM product LIKE '{column_name}'"
                cursor.execute(check_field_query)

                if cursor.rowcount != 1:
                    add_field_query = f"ALTER TABLE product ADD {column_name} {data_type}"
                    cursor.execute(add_field_query)

                    print(f"The {column_name} field was added ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
        
try:
    with connect.cursor() as cursor:
        # Check if 'invoice' table exists
        cursor.execute("SHOW TABLES LIKE 'invoice'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'invoice' table
            cursor.execute("""
                CREATE TABLE invoice (
                    id_invoice VARCHAR(200) PRIMARY KEY,
                    id_user VARCHAR(200) NULL,
                    username VARCHAR(2000) NULL,
                    Service_location VARCHAR(2000) NULL,
                    time_sell VARCHAR(2000) NULL,
                    name_product VARCHAR(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    price_product VARCHAR(2000) NULL,
                    Volume VARCHAR(2000) NULL,
                    Service_time VARCHAR(200) NULL,
                    Status VARCHAR(200) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table invoice created ✅")

        else:
            # Check and add missing columns
            columns_to_add = [('time_sell', 'VARCHAR(2000)'), ('Status', 'VARCHAR(2000)')]

            for column_name, data_type in columns_to_add:
                check_field_query = f"SHOW COLUMNS FROM invoice LIKE '{column_name}'"
                cursor.execute(check_field_query)

                if cursor.rowcount != 1:
                    add_field_query = f"ALTER TABLE invoice ADD {column_name} {data_type}"
                    cursor.execute(add_field_query)

                    print(f"The {column_name} field was added ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
        
try:
    with connect.cursor() as cursor:
        # Check if 'Payment_report' table exists
        cursor.execute("SHOW TABLES LIKE 'Payment_report'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'Payment_report' table
            cursor.execute("""
                CREATE TABLE Payment_report (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    id_user VARCHAR(200),
                    id_order VARCHAR(500),
                    time VARCHAR(200) NULL,
                    price VARCHAR(400) NULL,
                    dec_not_confirmed VARCHAR(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    Payment_Method VARCHAR(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    payment_Status VARCHAR(2000) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table Payment_report created ✅")

        else:
            # Check and add missing columns
            columns_to_add = [('Payment_Method', 'VARCHAR(1000)')]

            for column_name, data_type in columns_to_add:
                check_field_query = f"SHOW COLUMNS FROM Payment_report LIKE '{column_name}'"
                cursor.execute(check_field_query)

                if cursor.rowcount != 1:
                    add_field_query = f"ALTER TABLE Payment_report ADD {column_name} {data_type}"
                    cursor.execute(add_field_query)

                    print(f"The {column_name} field was added ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        

try:
    with connect.cursor() as cursor:
        # Check if 'Discount' table exists
        cursor.execute("SHOW TABLES LIKE 'Discount'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'Discount' table
            cursor.execute("""
                CREATE TABLE Discount (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    code VARCHAR(2000) NULL,
                    price VARCHAR(200) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table Discount created ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        

try:
    with connect.cursor() as cursor:
        # Check if 'Giftcodeconsumed' table exists
        cursor.execute("SHOW TABLES LIKE 'Giftcodeconsumed'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'Giftcodeconsumed' table
            cursor.execute("""
                CREATE TABLE Giftcodeconsumed (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    code VARCHAR(2000) NULL,
                    id_user VARCHAR(200) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table Giftcodeconsumed created ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
    
try:
    with connect.cursor() as cursor:
        # Check if 'TestAccount' table exists
        cursor.execute("SHOW TABLES LIKE 'TestAccount'")
        table_exists = cursor.rowcount > 0

        if not table_exists:
            # Create 'TestAccount' table
            cursor.execute("""
                CREATE TABLE TestAccount (
                    id_invoice VARCHAR(200) PRIMARY KEY,
                    id_user VARCHAR(200) NULL,
                    username VARCHAR(200) NULL,
                    Service_location VARCHAR(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    time_sell VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)

            print("Table TestAccount created ✅")

        # Commit changes to the database
        connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
        
try:
    with connect.cursor() as cursor:
        # Check if 'textbot' table exists
        cursor.execute("SHOW TABLES LIKE 'textbot'")
        table_exists = cursor.rowcount > 0

        # Define text values
        text_roll = """
♨️ قوانین استفاده از خدمات ما

1- به اطلاعیه هایی که داخل کانال گذاشته می شود حتما توجه کنید.
2- در صورتی که اطلاعیه ای در مورد قطعی در کانال گذاشته نشده به اکانت پشتیبانی پیام دهید
3- سرویس ها را از طریق پیامک ارسال نکنید برای ارسال پیامک می توانید از طریق ایمیل ارسال کنید.
"""

        text_dec_fq = """
💡 سوالات متداول ⁉️

1️⃣ فیلترشکن شما آیپی ثابته؟ میتونم برای صرافی های ارز دیجیتال استفاده کنم؟

✅ به دلیل وضعیت نت و محدودیت های کشور سرویس ما مناسب ترید نیست و فقط لوکیشن‌ ثابته.

2️⃣ اگه قبل از منقضی شدن اکانت، تمدیدش کنم روزهای باقی مانده می سوزد؟

✅ خیر، روزهای باقیمونده اکانت موقع تمدید حساب میشن و اگه مثلا 5 روز قبل از منقضی شدن اکانت 1 ماهه خودتون اون رو تمدید کنید 5 روز باقیمونده + 30 روز تمدید میشه.

3️⃣ اگه به یک اکانت بیشتر از حد مجاز متصل شیم چه اتفاقی میافته؟

✅ در این صورت حجم سرویس شما زود تمام خواهد شد.

4️⃣ فیلترشکن شما از چه نوعیه؟

✅ فیلترشکن های ما v2ray است و پروتکل‌های مختلفی رو ساپورت میکنیم تا حتی تو دورانی که اینترنت اختلال داره بدون مشکل و افت سرعت بتونید از سرویستون استفاده کنید.

5️⃣ فیلترشکن از کدوم کشور است؟

✅ سرور فیلترشکن ما از کشور  آلمان است

6️⃣ چطور باید از این فیلترشکن استفاده کنم؟

✅ برای آموزش استفاده از برنامه، روی دکمه «📚 آموزش» بزنید.

7️⃣ فیلترشکن وصل نمیشه، چیکار کنم؟

✅ به همراه یک عکس از پیغام خطایی که میگیرید به پشتیبانی مراجعه کنید.

8️⃣ فیلترشکن شما تضمینی هست که همیشه مواقع متصل بشه؟

✅ به دلیل قابل پیش‌بینی نبودن وضعیت نت کشور، امکان دادن تضمین نیست فقط می‌تونیم تضمین کنیم که تمام تلاشمون رو برای ارائه سرویس هر چه بهتر انجام بدیم.

9️⃣ امکان بازگشت وجه دارید؟

✅ امکان بازگشت وجه در صورت حل نشدن مشکل از سمت ما وجود دارد.

💡 در صورتی که جواب سوالتون رو نگرفتید میتونید به «پشتیبانی» مراجعه کنید.
"""

        text_channel = """   
        ⚠️ کاربر گرامی؛ شما عضو چنل ما نیستید
از طریق دکمه زیر وارد کانال شده و عضو شوید
پس از عضویت دکمه بررسی عضویت را کلیک کنید"""

        if not table_exists:
            # Create 'textbot' table
            cursor.execute("""
                CREATE TABLE textbot (
                    id_text VARCHAR(600) PRIMARY KEY NOT NULL,
                    text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)
            print("Table textbot created ✅")

            # Insert initial data
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_start', 'سلام خوش آمدید')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_usertest', '🔑 اکانت تست')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_Purchased_services', '🛍 سرویس های من')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_support', '☎️ پشتیبانی')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_help', '📚 آموزش')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_bot_off', '❌ ربات خاموش است، لطفا دقایقی دیگر مراجعه کنید')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_roll', %s)", (text_roll,))
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_fq', '❓ سوالات متداول')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_dec_fq', %s)", (text_dec_fq,))
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_account', '👨🏻‍💻 مشخصات کاربری')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_sell', '🔐 خرید اشتراک')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_Add_Balance', '💰 افزایش موجودی')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_channel', %s)", (text_channel,))
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_Discount', '🎁 کد هدیه')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_Tariff_list', '💰 تعرفه اشتراک ها')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_dec_Tariff_list', 'تنظیم نشده است')")
            cursor.execute("INSERT INTO textbot (id_text, text) VALUES ('text_Account_op', '🎛 حساب کاربری')")

        else:
            # Insert data if not exists
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_start', 'سلام خوش آمدید')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_usertest', '🔑 اکانت تست')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_Purchased_services', '🛍 سرویس های من')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_support', '☎️ پشتیبانی')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_help', '📚 آموزش')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_bot_off', '❌ ربات خاموش است، لطفا دقایقی دیگر مراجعه کنید')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_roll', %s)", (text_roll,))
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_fq', '❓ سوالات متداول')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_dec_fq', %s)", (text_dec_fq,))
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_account', '👨🏻‍💻 مشخصات کاربری')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_sell', '🔐 خرید اشتراک')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_Add_Balance', '💰 افزایش موجودی')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_channel', %s)", (text_channel,))
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_Discount', '🎁 کد هدیه')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_Tariff_list', '💰 تعرفه اشتراک ها')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_dec_Tariff_list', 'تنظیم نشده است')")
            cursor.execute("INSERT IGNORE INTO textbot (id_text, text) VALUES ('text_Account_op', '🎛 حساب کاربری')")

    connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))



try:
    with connect.cursor() as cursor:
        # Check if the 'PaySetting' table exists
        cursor.execute("SHOW TABLES LIKE 'PaySetting'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Create 'PaySetting' table
            cursor.execute("""
                CREATE TABLE PaySetting (
                    NamePay VARCHAR(500) PRIMARY KEY NOT NULL,
                    ValuePay TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)
            print("Table PaySetting created ✅")

            # Insert initial data
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('CartDescription', '603700000000')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('Cartstatus', 'oncard')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('apinowpayment', '0')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('nowpaymentstatus', 'offnowpayment')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('digistatus', 'offdigi')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('statusaqayepardakht', 'offaqayepardakht')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('merchant_id_aqayepardakht', '0')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('perfectmoney_Payer_Account', '0')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('perfectmoney_AccountID', '0')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('perfectmoney_PassPhrase', '0')")
            cursor.execute("INSERT INTO PaySetting (NamePay, ValuePay) VALUES ('status_perfectmoney', 'offperfectmoney')")

        else:
            # Insert data if not exists
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('Cartstatus', 'oncard')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('CartDescription', '603700000000')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('apinowpayment', '0')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('nowpaymentstatus', 'offnowpayment')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('digistatus', 'offdigi')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('statusaqayepardakht', 'offaqayepardakht')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('merchant_id_aqayepardakht', '0')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('perfectmoney_Payer_Account', '0')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('perfectmoney_AccountID', '0')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('perfectmoney_PassPhrase', '0')")
            cursor.execute("INSERT IGNORE INTO PaySetting (NamePay, ValuePay) VALUES ('status_perfectmoney', 'offperfectmoney')")

    connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
        
try:
    with connect.cursor() as cursor:
        # Check if the 'DiscountSell' table exists
        cursor.execute("SHOW TABLES LIKE 'DiscountSell'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Create 'DiscountSell' table
            cursor.execute("""
                CREATE TABLE DiscountSell (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    codeDiscount VARCHAR(1000) NOT NULL,
                    price VARCHAR(200) NOT NULL,
                    limitDiscount VARCHAR(500) NOT NULL,
                    usedDiscount VARCHAR(500) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)
            print("Table DiscountSell created ✅")

    connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
        
try:
    with connect.cursor() as cursor:
        # Check if the 'affiliates' table exists
        cursor.execute("SHOW TABLES LIKE 'affiliates'")
        table_exists = cursor.fetchone()

        if not table_exists:
            # Create 'affiliates' table
            cursor.execute("""
                CREATE TABLE affiliates (
                    description TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    status_commission VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    Discount VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    price_Discount VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    id_media VARCHAR(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL,
                    affiliatesstatus VARCHAR(600) NULL,
                    affiliatespercentage VARCHAR(600) NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin
            """)
            print("Table affiliates created ✅")

            # Insert a record into the 'affiliates' table
            cursor.execute("""
                INSERT INTO affiliates (description, id_media, status_commission, Discount, affiliatesstatus, affiliatespercentage)
                VALUES ('none', 'none', 'oncommission', 'onDiscountaffiliates', 'offaffiliates', '0')
            """)
            print("Record inserted into affiliates ✅")

    connect.commit()

except Exception as e:
    # Write the exception message to a file
    with open("error_log.txt", "w") as error_file:
        error_file.write(str(e))
        
finally:
    connect.close()
    print("Database connection closed ✅")