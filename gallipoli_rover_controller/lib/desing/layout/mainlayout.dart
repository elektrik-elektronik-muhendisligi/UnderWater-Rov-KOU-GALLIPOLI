import "package:flutter/material.dart";
import 'package:flutter_webview_plugin/flutter_webview_plugin.dart';

class MainLayout extends StatefulWidget {

  @override
  _MainLayoutState createState() => _MainLayoutState();
}

class _MainLayoutState extends State<MainLayout> {
  String url="10.0.2.2:9875/video_feed";

  String video_feed="10.0.3.2:9875/video_feed";

  String denemeUrl="https://github.com/flutter/flutter/issues/27834";

  bool setts=true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: Text("pulse"),
        onPressed: (){
          setState(() {
            setts==true?true:false;
          });
        },
      ),
      body: Container(
        child:Column(
          children: <Widget>[
           Expanded(
             child:WebviewScaffold(
             url: setts==false?denemeUrl:url,
             mediaPlaybackRequiresUserGesture: true,
             withJavascript: true,
            ),
           ),
           Expanded(
             child: Image.network(url),
           )
          ],
        )
      ),
    );
  }
}

//"10.0.2.2:9875/video_feed"