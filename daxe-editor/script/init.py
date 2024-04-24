import psycopg2
import requests;
import json;
import uuid;

#establishing the connection
conn = psycopg2.connect(
   database="mdo_auth", user='postgres', password='enter', host='host.docker.internal', port= '5432'
)
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

#Insert the guest user into mdo_auth
org_id = '3878293375';
company_name = 'fuse';
tenantId = '101';
role = '34827926642';
userUuid  = str(uuid.uuid4());

## insert into org_info
authConnection =conn.cursor();
authConnection.execute("select count(*) from PUBLIC.org_info where org_id="+org_id);
if(authConnection.fetchone()[0]<=0):
    authConnection.execute("INSERT INTO public.org_info(org_id,company_name, authenticate_with) VALUES ('"+org_id+"', '"+company_name+"', 'email');")
    conn.commit();
    print('Org created successfuly with name :: ', company_name)
else:
    print("Skipped org creation already exits...");    

## Insert into org_tenant_mapping
authConnection.execute("select count(*) from PUBLIC.org_tenant_mapping where tenant_id ='"+tenantId+"' and org_id ='"+org_id+"'");
if(authConnection.fetchone()[0]<=0):
    authConnection.execute("INSERT INTO PUBLIC.org_tenant_mapping(tenant_id, org_id, tenant_type, redirect_url, tenant_name) VALUES ('"+tenantId+"', '"+org_id+"', 'PROD', 'http://localhost:8080', 'Development');")
    conn.commit();
    print('Org tenant created successfuly with tenant ::' + tenantId)
else:
    print("Skipped org tenant creation already exits...");

## Insert into user_mdo
authConnection.execute("select count(*) from PUBLIC.user_mdo where org_id='"+org_id+"' and userid='guest'");
if(authConnection.fetchone()[0]<=0):
    authConnection.execute("INSERT INTO public.user_mdo(userid, password, email, status, service_acc, password_active_date, has_admin_access, failed_login_attempts, last_active_date, org_id, uuid) VALUES ('guest', '$2a$10$k2Sml5fkiF5y6paVlk8nLu269mbvBxagx39aFsqwJz4iKSf5I9mpm', 'guest', 'ACTIVE', true, '17009290998717', true, 0, '17009290998717', '"+org_id+"', '"+userUuid+"');")
    conn.commit();
    print('User created  successfuly:: guest with password guest')
else:
    authConnection.execute("select uuid from PUBLIC.user_mdo where org_id='"+org_id+"' and userid='guest'");
    userUuid = authConnection.fetchone()[0];
    print('userUuid', userUuid);
    print("Skipped user creation...");

## Insert into user_tenant_mapping
authConnection.execute("select count(*) from PUBLIC.user_tenant_mapping where user_id='"+userUuid+"'");
if(authConnection.fetchone()[0]<=0):
    authConnection.execute("insert into PUBLIC.user_tenant_mapping(uuid,user_id,tenantid,is_default,org_id) values ('"+str(uuid.uuid4())+"','"+userUuid+"','"+tenantId+"',true,'"+org_id+"')")
    conn.commit();
    print('User tenant mapped successfuly tenant id : ', tenantId)
else:
    print("Skipped user tenant mapping ...");

## Insert into user roles
authConnection.execute("select count(*) from PUBLIC.user_roles where userid='"+userUuid+"'");
if(authConnection.fetchone()[0]<=0):
    authConnection.execute("insert into  PUBLIC.user_roles(uuid,roleid,userid,isdefault,tenantid) values('"+str(uuid.uuid4())+"','"+role+"','"+userUuid+"',true,'"+tenantId+"')")
    conn.commit();
    print('User role mapped successfuly role id : ', role)
else:
    print("Skipped user role mapping ...");
authConnection.close();

# cursor.execute("select *from user_mdo")
# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()
# print("Connection established to: ",data)

#Closing the connection
conn.close()


