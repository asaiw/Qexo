"""
@Project   : zh-CN
@Author    : abudu
@Blog      : https://www.oplog.cn
"""

from ..core import Language


class Main(Language):
    name = 'zh_CN'
    default = {
        "name": name,
        "data": {
            'JUMPED': '跳过',
            "ERROR_GETTING_PROVIDER": "获取PROVIDER时出错",
            "RETRY": "重试",
            "CONSOLE": "管理面板",
            "CACHE": "缓存",
            "REBUILD_CACHE_SUCCESS": "重建{}缓存成功",
            "PURGE_ALL_CACHE_SUCCESS": "清除全部缓存成功",
            "SAVE_SETTING": "保存设置",
            "SAVE_CUSTOM": "保存自定义字段",
            "GET_UPDATE_SUCCESS": "获取更新成功",
            "GET_UPDATE_FAILED": "获取更新失败",
            "API_VERIFY_FAILED": "API鉴权失败, 访问IP: {}",
            "FIX_SUCCESS": "已修复{}个设置",
            "FIX_VALUE": "修正字段",
            "FIX_DISPLAY": "尝试自动修复了 {} 个字段，请在稍后检查和修改配置",
            "DEL_VALUE": "删除字段",
            "READ_FILE": "读取文件",
            "UPDATE_QUEUING": "更新失败: 当前有部署正在进行",
            "UPDATE_SUCCESS": "更新成功",
            "START_DEL": "开始删除文件...",
            "DEL_FAILED": "删除失败",
            "START_VERCEL_UPDATE": "开始更新, 使用Vercel方案",
            "START_EXTRACT_UPDATE": "下载更新完成, 开始解压",
            "FIND_UPDATE_INDEX": "解压完成, 寻找Index目录",
            "FIND_INDEX_SUCCESS": "找到Index目录",
            "FIND_INDEX_FAILED": "'更新失败: 未找到Index目录",
            "START_LOCAL_UPDATE": "开始更新, 使用本地方案, 准备临时目录",
            "START_COPY": "删除完成, 正在拷贝文件...",
            "DEL_TMP": "删除临时目录",
            "UPDATE_LIB": "开始更新库...",
            "MIGRATE_DB": "开始迁移数据库",
            "LOCAL_UPDATE_SUCCESS": "更新完成，五秒后重启线程",
            "QEXO_MSG": "Qexo消息",
            "PROVIDER_VERIFY_ERROR": "校验配置出错",
            "PROVIDER_VERIFY_SUCCESS": "Provider校验结果: {}",
            "FRONT_MATTER_GET_ERROR": "FrontMatter解析失败: {}",
            "UNTITLED": "未命名",
            "UPDATE_POST_INDEX": "更新文章详情索引",
            "DEL_POST_INDEX": "删除文章详情索引",
            "CURRENT_ENV": "当前环境",
            "LOCAL": "本地",
            "ELEVATOR_START": "开始运行自动更新迁移程序...来自{}",
            "ELEVATOR_ERROR": "自动更新迁移程序出错: {}",
            "CAPTCHA_GET_FAILED": "获取失败",
            "CAPTCHA_FAILED": "人机验证失败!",
            "CAPTCHA_RESULT": "reCaptcha{}结果: {}",
            "CAPTCHA_NO": "未收到人机验证信息",
            "LOGIN_SUCCESS": "登录成功，等待转跳",
            "LOGIN_FAILED": "登录信息错误",
            "USER_IS_NOT_STAFF": "子用户{}尝试访问{}被拒绝",
            "USER_IS_NOT_STAFF_MODIFY": "子用户{}尝试修改{}被拒绝",
            "USER_IS_NOT_STAFF_DEL": "子用户{}尝试删除{}被拒绝",
            "USER_IS_NOT_STAFF_RENAME": "子用户{}尝试重命名{}被拒绝",
            "NO_PERMISSION": "子用户不支持此操作！",
            "HEXO_TOKEN_FAILED": "远程连接错误!请检查Token",
            "HEXO_VERSION": "检测到Hexo版本: {}",
            "HEXO_VERSION_FAILED": "未检测到Hexo",
            "HEXO_INDEX_FAILED": "\n检测到index.html, 这可能不是正确的仓库",
            "HEXO_CONFIG": "\n检测到Hexo配置文件",
            "HEXO_CONFIG_FAILED": "\n未检测到Hexo配置文件",
            "HEXO_THEME": "\n检测到主题目录",
            "HEXO_THEME_FAILED": "\n未检测到主题目录",
            "HEXO_PACKAGE": "\n检测到package.json",
            "HEXO_PACKAGE_FAILED": "\n未检测到package.json",
            "HEXO_SOURCE": "\n检测到source目录",
            "HEXO_SOURCE_FAILED": "\n未检测到source目录",
            "HEXO_CONFIG_UPDATE": "\nHexo配置文件更新成功",
            "HEXO_CONFIG_UPDATE_FAILED": "\n配置校验失败",
            "SAVE_SUCCESS": "保存成功!",
            "SAVE_FAILED": "保存失败!",
            "SAVE_SUCCESS_REDIRECT": "保存成功, 转跳中...",
            "SAVE_SUCCESS_AND_DEPLOY": "保存成功并提交部署!",
            "DRAFT_SAVE_SUCCESS": "草稿保存成功!",
            "DRAFT_SAVE_SUCCESS_AND_DEPLOY": "草稿保存成功并提交部署!",
            "DEL_SUCCESS": "删除成功!",
            "DEL_SUCCESS_AND_DEPLOY": "删除成功并提交部署!",
            "RENAME": "重命名",
            "RENAME_SUCCESS": "重命名成功!",
            "RENAME_SUCCESS_AND_DEPLOY": "重命名成功并提交部署!",
            "TEST_MESSAGE": "如果你收到了这则消息, 那么代表您的消息配置成功了",
            "RESET_PASSWORD_NO_MATCH": "两次密码不一致!",
            "RESET_PASSWORD_NO": "请输入正确的密码！",
            "RESET_PASSWORD_NO_USERNAME": "请输入正确的用户名！",
            "RESET_PASSWORD_NO_OLD": "原密码错误!",
            "RESET_PASSWORD_NO_PASSWORD": "密码不能为空！",
            "UPDATE_NO_CHANNEL": "无此更新渠道",
            "UPDATE_SUCCESS_DISPLAY": "更新成功，请等待自动部署!",
            "IMAGE_DEL_SUCCESS": "已删除本地记录",
            "PROVIDER_NO_SUPPORT": "服务商不支持！",
            "UPLOAD_SUCCESS": "上传成功！",
            "UPLOAD_FAILED": "上传失败！",
            "ADD_SUCCESS": "添加成功！",
            "EDIT_SUCCESS": "修改成功！",
            "CLEAN_FLINKS_SUCCESS": "成功清理了{}条友链",
            "CLEAN_FLINKS_FAILED": "无隐藏的友链",
            "UPDATE_LABEL": "程序更新",
            "UPDATE_CONTENT": "检测到更新: {}<br>{}<p>可前往 <object><a href=\"/settings.html\">设置</a></object> 在线更新</p>",
            "UNKNOWN_SIDEBAR": "未知侧边栏",
            "PUBLISH_SUCCESS": "发布成功!",
            "SCRIPT_RUN": "执行云端命令: {}",
            "SCRIPT_RUN_SUCCESS_LOG": "执行{}成功: {}",
            "SCRIPT_RUN_SUCCESS": "运行成功",
            "SCRIPT_ARGV_FAILED": "请输入正确的参数！",
            "SYSTEM_ERROR": "程序遇到了错误！",
            "NOT_INIT": "未完成初始化配置, 转跳到初始化页面",
            "AUTO_PROVIDER_FAILED": "自动生成PROVIDER错误，请检查配置并提交",
            "INIT_USER_FAILED": "初始化用户名密码错误: {}",
            "INIT_PROVIDER_FAILED": "初始化PROVIDER错误: {}",
            "INIT_VERCEL_FAILED": "初始化Vercel错误: {}",
            "VERIFY_FAILED": "校验失败",
            "INIT_SUCCESS": "已完成初始化, 转跳至首页",
            "LOGOUT_SUCCESS": "注销成功",
            "MIGRATE_CONFIG_SUCCESS": "迁移配置完成！",
            "MIGRATE_IMAGE_SUCCESS": "迁移图片完成！",
            "MIGRATE_FLINKS_SUCCESS": "迁移友链完成！",
            "MIGRATE_MSG_SUCCESS": "迁移消息完成！",
            "MIGRATE_CUSTOM_SUCCESS": "迁移自定义字段完成！",
            "MIGRATE_UV_SUCCESS": "迁移UV完成！",
            "MIGRATE_PV_SUCCESS": "迁移PV完成！",
            "MIGRATE_POST_SUCCESS": "迁移文章索引完成！",
            "MIGRATE_TALKS_SUCCESS": "迁移说说完成！",
            "MIGRATE_FAILED": "迁移{}失败: {}",
            "JUMP_UPDATE": "检测到更新配置, 转跳至配置更新页面",
            "JUMP_UPDATE_FAILED": "检测配置更新失败, 转跳至更新页面",
            "DASHBOARD": "控制台",
            "PUBLISHED": "已发布",
            "DRAFT": "草稿",
            "EDIT_TALK": "编辑说说",
            "EDIT_PAGE": "编辑页面",
            "EDIT_POST": "编辑文章",
            "EDIT_CONFIG": "编辑配置",
            "NEW_PAGE": "新建页面",
            "GET_PAGE_SCAFFOLD_FAILED": "获取页面模板失败, 错误信息: {}",
            "NEW_POST": "新建文章",
            "GET_POST_SCAFFOLD_FAILED": "获取文章模板失败, 错误信息: {}",
            "POSTS_LIST": "文章列表",
            "PAGES_LIST": "页面列表",
            "CONFIGS_LIST": "配置列表",
            "TALKS_LIST": "说说列表",
            "IMAGES_LIST": "图片列表",
            "FLINKS_LIST": "友情链接",
            "SETTINGS": "设置",
            "GET_SETTINGS_FAILED": "配置获取错误, 转跳至配置更新页面",
            "ADVANCED_SETTINGS": "高级设置",
            "GET_ADVANCED_SETTINGS_FAILED": "高级设置获取错误: {}",
            "CUSTOM_LIST": "自定义字段",
            "GET_CUSTOM_FAILED": "自定义字段获取错误: {}",
            "SCRIPTS_LIST": "在线函数库",
            "GET_SCRIPTS_FAILED": "在线函数库获取错误: {}",
            "PAGE_404": "页面不存在: {}",
            "PAGE_500": "服务端错误: {}",
            "INDEX_POST_LABEL": "总文章",
            "INDEX_POST_TIP": "今天你写文章了吗",
            "INDEX_IMAGE_LABEL": "总图片",
            "INDEX_IMAGE_TIP": "尝试图片管理",
            "INDEX_VERSION_LABEL": "当前版本",
            "INDEX_VERSION_TIP": "是最新版哦",
            "INDEX_VERSION_HASNEW": "检测到更新",
            "INDEX_GITHUB_TIP": "支持作者",
            "INDEX_GUIDE_LABEL": "现在要做点什么？",
            "INDEX_GUIDE_LABEL_1": "新文章",
            "INDEX_GUIDE_TIP_1_P1": "写下你的",
            "INDEX_GUIDE_TIP_1_P2": "新构思",
            "INDEX_GUIDE_LABEL_2": "新页面",
            "INDEX_GUIDE_TIP_2_P1": "创建你的",
            "INDEX_GUIDE_TIP_2_P2": "新页面",
            "INDEX_GUIDE_LABEL_3": "新友链",
            "INDEX_GUIDE_TIP_3_P1": "添加你的",
            "INDEX_GUIDE_TIP_3_P2": "新朋友",
            "INDEX_GUIDE_LABEL_4": "新说说",
            "INDEX_GUIDE_TIP_4_P1": "分享你的",
            "INDEX_GUIDE_TIP_4_P2": "新动态",
            "INDEX_RECENT_POSTS": "最近文章",
            "POST_NAME": "文章名",
            "STATUS": "状态",
            "OPERATION": "操作",
            "INDEX_RANDOM_POSTS": "随机文章",
            "INDEX_RECENT_IMAGES": "最近图片",
            "IMAGE_NAME": "图片名",
            "SIZE": "大小",
            "INIT": "初始化",
            "INIT_WELCOME": "欢迎！请选择语言以开始初始化",
            "INIT_USER": "用户配置",
            "INIT_BLOG": "博客配置",
            "INIT_IMAGE": "图床配置",
            "INIT_VERCEL": "Vercel 配置",
            "INIT_FINISH": "恭喜您初始化完毕",
            "INIT_LOGIN_MSG_1": "请牢记您的登录信息：",
            "INIT_LOGIN_MSG_2": "用户名: ",
            "INIT_LOGIN_MSG_3": "密码: 您设定的值",
            "INIT_LOGIN_MSG_4": "登录控制台",
            "START": "开始",
            "INIT_2_1": "API 密钥",
            "INIT_2_1_PH": "留空即自动生成",
            "INIT_2_2": "用户名",
            "INIT_2_2_PH": "设置用户名",
            "INIT_2_3": "密码",
            "INIT_2_3_PH": "设置密码",
            "INIT_2_4": "确认密码",
            "INIT_2_4_PH": "再次输入以确认密码",
            "NEXT": "下一步",
            "INIT_3_1": "服务商",
            "INIT_3_2": "使用配置",
            "FORCE_SUBMIT": "强制提交",
            "FORCE_MSG": "确定要强制提交吗？",
            "INIT_4_1": "Vercel 密钥",
            "INIT_4_2": "项目 ID",
            "FINISH": "完成",
            "TIPS": "提示",
            "CONFIRM": "确定",
            "CANCEL": "取消",
            "LOGIN": "登录",
            "USERNAME": "用户名",
            "PASSWORD": "密码",
            "LOGIN_FAILED_1": "用户名不能为空! ",
            "LOGIN_FAILED_2": "密码不能为空! ",
            "LOGIN_FAILED_3": "请完成验证! ",
            "NETWORK_ERROR": "网络错误!",
            "MIGRATE": "迁移",
            "MIGRATE_LABEL": "迁移配置",
            "IMPORT": "导入",
            "EXPORT": "导出",
            "HOME": "主页",
            "HELP": "帮助",
            "BACKUP": "备份文件",
            "WARN": "警告",
            "IMPORT_WARN": "导入后, 您将会丢失现有的全部信息, 请确认!",
            "STILL_IMPORT": "仍然继续",
            "RESULT": "结果",
            "MIGRATE_SUCCESS": "全部迁移完成!",
            "SKIP": "跳过",
            "ERROR": "错误",
            "UPDATE_CONFIG": "配置更新",
            "CUSTOMIZE": "个性化",
            "CUSTOMIZE_LABEL": "仪表盘样式配置项",
            "SIDEBAR_COLOR": "侧边栏颜色",
            "SIDEBAR_TYPE": "侧栏类型",
            "SIDEBAR_TYPE_LABEL": "在以下两种样式中选择",
            "SIDEBAR_TYPE_TIP": "你只能在桌面端修改样式",
            "NAVBAR_FIX": "顶栏固定",
            "DARKMODE": "浅色 / 深色",
            "PROJECT_PAGE": "项目页面",
            "WIKI_LABEL": "查看文档",
            "THANK_LABEL": "感谢您的Star!",
            "POST": "文章",
            "PAGE": "页面",
            "CONFIG": "配置",
            "FLINK": "友链",
            "IMAGE": "图片",
            "TALK": "说说",
            "CUSTOM": "自定",
            "HELP_LABEL": "需要帮助?",
            "HELP_TIP": "点击这里查找文档",
            "DOC": "文档",
            "LOADING": "正在加载中...",
            "NO_MSG_TIP": "你当前没有消息哟~",
            "HAS_MSG_TIP_1": "你有",
            "HAS_MSG_TIP_2": "则未读消息",
            "CLEAR_ALL": "清除全部",
            "MSG_LOAD_ERROR": "消息加载失败",
            "NAME": "名称",
            "VALUE": "字段",
            "COMMAND": "命令",
            "WELCOME": "欢迎",
            "SUPPORT": "支持",
            "LOGOUT": "注销",
            "MSG_LOADING": "消息获取中...",
            "EXCERPT_LOADING": "摘要获取中...",
            "EXCERPT_FAILED": "摘要获取失败: ",
            "SEARCH": "搜索",
            "SEARCH_POST": "搜索文章",
            "SEARCH_PAGE": "搜索页面",
            "SEARCH_CONFIG": "搜索配置",
            "SEARCH_TALK": "搜索说说",
            "SEARCH_IMAGE": "搜索图片",
            "SEARCH_FLINK": "搜索友链",
            "SEARCH_CUSTOM": "搜索字段",
            "SEARCH_SCRIPT": "搜索命令",
            "SEARCH_SETTINGS": "搜索设置",
            "SCRIPTS_LABEL": "云端命令",
            "AUTHOR": "作者",
            "DESCRIPTION": "简介",
            "PREV_PAGE": "上一页",
            "NEXT_PAGE": "下一页",
            "CLOSE": "关闭",
            "NO_PREV_PAGE": "已是第一页",
            "NO_NEXT_PAGE": "已是最后一页",
            "INPUT_ARGV": "请输入参数",
            "CONFIRM_RUN": "确认要执行 {0} 吗？此操作不可中止",
            "RUNNING": "正在运行中...",
            "TALK_LABEL": "全部说说",
            "MEASURE_POST": "篇",
            "MEASURE_IMAGE": "张",
            "MEASURE_LINK": "条",
            "CONTENT": "内容",
            "TIME": "时间",
            "TAGS": "标签",
            "LOVE": "点赞",
            "DEL_CONFIRM_1": "确认要删除",
            "DEL_CONFIRM_2": "吗？此操作不可撤回",
            "DELETING": "正在删除中...",
            "SETTINGS_LABEL": "修改配置",
            "SET_WEBHOOK": "一键设置WEBHOOK",
            "ADVANCED": "高级设置",
            "CLOUD_SCRIPTS": "云端命令库",
            "PURGE_CACHE": "清除缓存",
            "ONEKEY_UPDATE": "一键更新",
            "SET_API": "API配置",
            "SET_API_1": "API密钥",
            "SET_API_1_PH": "留空将保持不变",
            "SET_API_2": "启用友链申请API",
            "SET_API_3": "使用 reCaptcha 验证友链申请",
            "SET_API_4": "reCaptcha 密钥",
            "SET_API_4_PH": "reCaptchaV3 服务器端 Token",
            "SUBMIT": "提交",
            "SET_STATISTICS": "统计配置",
            "SET_STATISTICS_1": "启用统计API",
            "SET_STATISTICS_2": "统计安全域名",
            "SET_STATISTICS_2_PH": "输入域名包含的关键字, 英文半角逗号间隔",
            "SET_USER": "用户配置",
            "SET_USER_1": "原密码",
            "SET_USER_1_PH": "请输入原密码",
            "SET_USER_2": "新用户名",
            "SET_USER_2_PH": "请输入新用户名",
            "SET_USER_3": "新密码",
            "SET_USER_3_PH": "请输入新密码",
            "SET_USER_4": "确认密码",
            "SET_USER_4_PH": "再次输入以确认密码",
            "SET_SECURE": "安全配置",
            "SET_SECURE_1": "登录页 reCaptchaV3 用户端密钥",
            "SET_SECURE_1_PH": "留空即关闭该功能",
            "SET_SECURE_2": "登录页 reCaptchaV3 服务器端密钥",
            "SET_SECURE_2_PH": "留空即关闭该功能",
            "SET_SECURE_3": "登录页 reCaptchaV2 用户端密钥",
            "SET_SECURE_3_PH": "留空即关闭该功能",
            "SET_SECURE_4": "登录页 reCaptchaV2 服务器端密钥",
            "SET_SECURE_4_PH": "留空即关闭该功能",
            "SET_BLOG": "博客配置",
            "SET_BLOG_1": "服务商",
            "SET_BLOG_2": "使用配置",
            "SET_NOTIFY": "消息配置",
            "SET_NOTIFY_1": "服务商",
            "TEST": "测试",
            "SET_ABBRLINK": "短链接设置",
            "SET_ABBRLINK_1": "短链接算法",
            "SET_ABBRLINK_2": "短链接进制",
            "SET_EXCERPT": "摘要配置",
            "SET_EXCERPT_1": "截取方法",
            "SET_EXCERPT_2": "自动截取",
            "SET_EXCERPT_3": "保存字段",
            "SET_EXCERPT_3_PH": "一般为 excerpt",
            "SET_IMAGE": "图床配置",
            "SET_IMAGE_1": "图床类型",
            "SET_CDN": "CDN 配置",
            "SET_CDN_1": "CDN 提供商",
            "SET_CUSTOM": "自定义配置",
            "SET_CUSTOM_1": "站点名称",
            "SET_CUSTOM_1_PH": "默认为 Hexo管理面板",
            "SET_CUSTOM_2": "站点连接符",
            "SET_CUSTOM_2_PH": "默认为“ - ”",
            "SET_CUSTOM_3": "默认为 images 下的 qexo.png",
            "SET_CUSTOM_4": "站点 ICON",
            "SET_CUSTOM_4_PH": "默认为 images 下的 icon.png",
            "SET_CUSTOM_5": "暗色 LOGO",
            "SET_CUSTOM_5_PH": "默认为 images 下的 qexo-dark.png",
            "RESET": "重置",
            "WARN_WEBHOOK": "确定要自动创建Webhook事件吗？这会清除您原仓库的所有Webhook事件",
            "UPDATE": "更新",
            "UPDATE_CHANNEL": "更新通道",
            "WARN_RESET": "确定要重置自定义配置吗？该操作不可回退",
            "SAVING": "正在保存中...",
            "CACHE_CLEAN_REQUEST": "确定清除所有缓存吗",
            "UPDATING": "正在更新中...",
            "REQUIRED": "必填",
            "EXCERPT_LOCAL_LENGTH": "摘要长度",
            "EXCERPT_LOCAL_LENGTH_PH": "截取的长度",
            "EXCERPT_TIANLI_KEY": "用户密钥",
            "EXCERPT_TIANLI_KEY_PH": "在爱发电获得的用户密钥",
            "EXCERPT_TIANLI_LENGTH": "发送长度",
            "EXCERPT_TIANLI_LENGTH_PH": "发送到服务端的内容长度",
            "POST_LABEL": "全部文章",
            "NEW_NAME": "新名称",
            "OPERATION_SUCCESS": "操作成功!",
            "PAGE_LABEL": "全部页面",
            "PAGE_NAME": "页面名",
            "PAGE_500_LABEL": "错误! Error 500",
            "PAGE_500_TIP": "报错信息：",
            "PAGE_404_LABEL": "错误! Error 404",
            "PAGE_404_TIP": "找不到页面 - ",
            "PAGE_403_LABEL": "错误! Error 403",
            "PAGE_403_TIP": "验证错误 - 请确认是否拥有权限",
            "NEW_PAGE_LABEL": "新建页面",
            "PAGE_ARGV_LABEL": "页面参数",
            "ADD": "添加",
            "OTHER_ARGV": "其他参数",
            "EDIT_SIDEBAR": "编辑侧边栏",
            "SEARCH_ITEM": "搜索项",
            "ICON": "图标",
            "NO_PAGE_NAME": "请在顶栏输入正确的页面名！",
            "UPLOAD_TIP": "上传图片",
            "LEAVE_CONFIRM": "确定要离开吗?",
            "SIDEBAR_EDIT_1": "冒号前的内容",
            "SIDEBAR_EDIT_2": "描述标题",
            "SIDEBAR_EDIT_3": "使用的图标",
            "NO_OTHER_ARGV": "暂无其他参数",
            "HEADER": "标头",
            "BOTTOM_PH": "若有多级, 请使用JSON格式",
            "NEW_POST_LABEL": "新建文章",
            "POST_ARGV_LABEL": "文章参数",
            "NO_POST_NAME": "请在顶栏输入正确的文章名！",
            "TAG_EXITS": "标签已存在!",
            "CATEGORY_EXITS": "分类已存在!",
            "ADD_TAG": "添加标签",
            "ADD_CATEGORY": "添加分类",
            "IMAGE_LABEL": "全部图片",
            "UPLOAD": "上传",
            "DEL_REMOTE": "删除远程文件",
            "FLINK_LABEL": "友情链接",
            "LINK": "链接",
            "IMAGE_LINK": "图片链接",
            "EDIT_FLINK": "编辑友链",
            "NEW_FLINK": "新增友链",
            "CONFIRM_CLEAN_FLINK": "确认要清理隐藏的链接吗？该操作不可回退",
            "EDIT_TALK_LABEL": "编辑说说",
            "TALK_ARGV_LABEL": "说说参数",
            "UPDATED_AT": "更新于",
            "UPDATED_AT_PH": "更新时间",
            "EDIT_TALK_PH": "在这里书写说说...",
            "ID_CODE": "识别代号",
            "EDIT_PAGE_LABEL": "编辑页面",
            "EDIT_POST_LABEL": "编辑文章",
            "CUSTOM_LABEL": "自定义字段",
            "VALUE_NAME": "字段名",
            "NEW_VALUE": "新建字段",
            "EDIT": "编辑",
            "CONFIRM_DEL_CUSTOM": "确认要删除 {0} 字段吗？该操作不可回退",
            "CONFIG_LABEL": "全部配置",
            "CONFIG_NAME": "配置名",
            "ADVANCED_SETTINGS_LABEL": "高级设置",
            "FIXING": "尝试修复中...请耐心等待",
            "CONFIRM_FIX": "确认要尝试自动修复程序吗？这会检查并创建/删除相应字段"
        }
    }
