package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gorilla/mux"
)

//mux: https://github.com/gorilla/mux

*******************************go get 安装并使用第3方开源包（不需要git clone，go get会自动下载源码到GOPATH目录下）
设置GOPATH：export GOPATH=/Users/liangzeng/go ，必须用export,
运行命令 go get -u github.com/gorilla/mux  (如果出错，通过go env查看GOPATH值是否为空)
源码会自动下载到 $GOPATH/src/github.com/gorilla/mux ，然后可以在任意目录下面新建project来使用这个pkg 了， 
为了让vscode能够自动导入该pkg，还得在vscode 中修改settings.json, 在WorkspaceSettings>页面设置："go.gopath": "/Users/liangzeng/go/" ，
这样当代码中用到了该pkg时vscode就会自动import "github.com/gorilla/mux" ，也能看到源码;



/*
1.路由精确完整匹配，每个路由都要显式注册，不会默认路由到 "/",不注册返回404;
2.不会根据前缀匹配，比如只注册了"/zhejiang" ，req="/zhejiang/a" 就会返回404;
3.支持注册默认路由，通过r.PathPrefix("/"), 处理不了的path都会交给它处理，但要注意：那些specific path必须在它前面注册，顺序很重要 ！
4.支持正则匹配， refer: https://regex101.com
5.支持Method匹配；
6.支持Host匹配，注册时通过Host(),不能直接把domain加入path注册；
7.支持 middleware 预处理；
*/

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%v \n", "Hello,Mux!")
}
func HangZhouHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "HZ: %v \n", r.URL.Path)
}

func ZheJiangHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "ZJ: %v \n", r.URL.Path)
}
func BucketListHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "BucketList: %v \n", r.URL.Path)
}
func BucketHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "BucketHandler: %v \n", r.URL.Path)
	vars := mux.Vars(r)
	fmt.Fprintf(w, "bucketname: %v \n", vars["bucketname"])
}
func ObjectHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "regexp: %v \n", r.URL.Path)
	vars := mux.Vars(r)
	fmt.Fprintf(w, "bucketname: %v, objname: %v \n", vars["bucketname"], vars["objname"])
}

func BucketHandlerDuplicate(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Duplicate: %v \n", r.URL.Path)
	vars := mux.Vars(r)
	fmt.Fprintf(w, "bucketname: %v, objname: %v \n", vars["bucketname"], vars["objname"])
}

func MimeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Mime: %v \n", r.URL.Path)
	vars := mux.Vars(r)
	fmt.Fprintf(w, "bucketname: %v, objname: %v \n", vars["bucketname"], vars["objname"])
}
func MetaHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Meta: %v \n", r.URL.Path)
	vars := mux.Vars(r)
	fmt.Fprintf(w, "bucketname: %v, objname: %v, metaKey: %v \n", vars["bucketname"], vars["objname"], vars["metaKey"])
}

func PostHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	fmt.Fprintf(w, "POST == %v, bucketname: %v \n", r.Method, vars["bucketname"])
}

func PutHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	fmt.Fprintf(w, "PUT == %v, bucketname: %v \n", r.Method, vars["bucketname"])
}

func GetHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	fmt.Fprintf(w, "GET == %v, bucketname: %v \n", r.Method, vars["bucketname"])
}

func DeleteHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	fmt.Fprintf(w, "DELETE == %v, bucketname: %v \n", r.Method, vars["bucketname"])
}

func HeadHandler(w http.ResponseWriter, r *http.Request) {
	// fmt.Println("HeadHandler", r.URL.String())
	vars := mux.Vars(r)
	fmt.Fprintf(w, "HEAD == %v, bucketname: %v \n", r.Method, vars["bucketname"])
	// fmt.Printf("HEAD == %v, bucketname: %v \n", r.Method, vars["bucketname"])

}

func HostHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Host:%v", r.Host)
}

func DomainHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Domain:%v", r.URL.String())
}

func SchemeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Scheme:%v", r.URL.Scheme)
}

func SecurityHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Scheme:%v", r.URL.Scheme)
}

func FinalHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "FinalHandler:%v, %v", r.Header.Get("Foo"), r.Header.Get("Hello")) //这些值在Middleware中设置了
}

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Do stuff here
		fmt.Println("\n loggingMiddleware called!")
		r.Header.Set("Foo", "bar")
		// Call the next handler, which can be another middleware in the chain, or the final handler.
		next.ServeHTTP(w, r)
	})
}
func AnotherMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Do stuff here
		fmt.Println("AnotherMiddleware called!")
		r.Header.Set("Hello", "World")
		// Call the next handler, which can be another middleware in the chain, or the final handler.
		next.ServeHTTP(w, r)
	})
}

func SpecificHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "SpecificHandler:%v", r.URL.String())
}

func DefaultHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "DefaultHandler:%v", r.URL.String())
}

func OldHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "OldHandler:%v", r.URL.String())
}

func NewHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "NewHandler:%v", r.URL.String())
}

func main() {
	fmt.Println("demo_mux")

	r := mux.NewRouter()
	//1.测试精确匹配
	//a)对于 "/zhejiang/hangzhou"  调用 HangZhouHandler
	//b)对于 "/zhejiang", 调用ZheJiangHandler
	//c)对于 "/", 调用 HomeHandler
	//d)对于 "/dummy",返回 404;
	r.HandleFunc("/", HomeHandler)
	r.HandleFunc("/zhejiang", ZheJiangHandler)
	r.HandleFunc("/zhejiang/hangzhou", HangZhouHandler)

	//2.测试正则匹配，参数变量提取
	//a)对于 "/buckets/abc/objects/123" 可以正确提取参数
	//b)对于 "/buckets/abc/objects/" 返回 404; 也就是说{objname}里面必须有字符串，不能是空;
	//c)对于 "/buckets/abc/objects/123/dummy" 返回 404;
	//d)对于 "/buckets/abc/objects/1234/mime" 正常;
	//e)对于 "/buckets", 正常;
	//f)对于 "/buckets/" 返回 404;
	//g)对于 "/buckets/abc/objects/123/meta-a_A-0" 正常, 正则匹配符合预期;
	//h)如果对同样的path, 注册不同的handler, 不会报错，会路由到第1个handler;
	r.HandleFunc("/buckets", BucketListHandler)
	r.HandleFunc("/buckets/{bucketname}/objects/{objname}", ObjectHandler)
	r.HandleFunc("/buckets/{bucketname}/objects/{objname}/mime", MimeHandler)
	r.HandleFunc(`/buckets/{bucketname}/objects/{objname}/{metaKey:meta-[a-zA-Z0-9,\-,_]{1,5}}`, MetaHandler) //这里必须使用反单引号;
	// r.HandleFunc("/buckets/{bucketname}/objects/{objname}", BucketHandlerDuplicate)

	//3.测试根据 Method dispatch，url相同, 这里用 postman tool 测试
	//a)如果只注册POST, 而发的是PUT/GET/DELETE, 则返回405(Method Not Allowed);
	//b)如果 PUT/GET/DELETE/POST 都注册，可以正确的根据Method路由；
	//c)如果不显示注册Method,则 任意method 都可以访问；
	//d)可以设置允许的Method集合;
	// r.HandleFunc("/buckets/{bucketname}", BucketHandler)
	r.HandleFunc("/buckets/{bucketname}", PostHandler).Methods("POST")
	r.HandleFunc("/buckets/{bucketname}", PutHandler).Methods("PUT")
	r.HandleFunc("/buckets/{bucketname}", GetHandler).Methods("GET")
	r.HandleFunc("/buckets/{bucketname}", DeleteHandler).Methods("DELETE")
	r.HandleFunc("/buckets/{bucketname}", HeadHandler).Methods("HEAD") //由于postman tool的原因，显示不出来resp.body;

	// r.HandleFunc("/buckets/{bucketname}", MethodHandler).Methods("GET","PUT","POST","DELETE")//这4个method注册相同的回调

	//4.测试Host, 用 Postman tool 测试， 需要设置 Header.Host
	//a)如果req.Header.Host不对，返回404
	//b)设置req.Header.Host = "up.qiniu.com", 可以正确访问, 注意：和 url.domain没有关系；
	r.HandleFunc("/host", HostHandler).Host("up.qiniu.com")
	r.HandleFunc("127.0.0.1:8000/testdomain", DomainHandler) //不支持把domain放到path中，必须通过Host()设置;

	//5.测试Schemes, 在本地测试失败，可能是因为https在服务端需要特别配置
	// r.HandleFunc("/scheme", SchemeHandler) //only ok for "http", no resp for "https"
	// r.HandleFunc("/scheme", SchemeHandler).Schemes("https", "http") //404 for "http", no resp for "https"
	// r.HandleFunc("/scheme", SecurityHandler).Schemes("https") //404 for "http", no resp for "https"

	//6.测试 middleware,根据注册顺序调用，最后才调用业务handler;
	r.Use(loggingMiddleware, AnotherMiddleware) //注册2个预处理函数，先调用loggingMiddleware;
	r.HandleFunc("/middleware", FinalHandler)   //注册业务handler

	//7.测试  默认路由和指定路由, 指定路由必须在默认路由之前注册，否则无效
	r.HandleFunc("/specific", SpecificHandler)
	// r.PathPrefix("/").Handler(http.HandlerFunc(DefaultHandler)) //这行代码精辟，把一个普通函数转为一个interface instance.

	//8.同时使用新mux和原生的Mux, 在升级产品代码时推荐这样做，对于新添加的路由使用新的mux注册,老的路由不变(仍然使用go自带的mux)
	//路由查找规则：优先在route中查找，如果不成功，再去rawMux中查找，如果都不成功，则404；
	rawMux := http.NewServeMux()
	rawMux.HandleFunc("/oldpattern", OldHandler) //之前注册的老的路由
	r.HandleFunc("/newpattern", NewHandler)      //新添加的路由使用新的mux注册
	r.PathPrefix("/").Handler(rawMux)            //设置默认路由为老的mux

	svr := &http.Server{
		Handler: r,
		Addr:    "127.0.0.1:8000",

		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	log.Fatal(svr.ListenAndServe())
}
