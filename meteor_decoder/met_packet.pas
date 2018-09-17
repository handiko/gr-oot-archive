//############################################################################//
//Made in 2017 by Artyom Litvinovich
//medet: Parse packets
//############################################################################//
unit met_packet;
interface
uses asys,met_jpg;
//############################################################################//
var
md_debug:boolean=false;
quiet:boolean=false;
print_stats:boolean=true;
time_file:boolean=false;

no_time_yet:boolean=true;
first_time,last_time:integer;
//############################################################################//  
procedure parse_cvcdu(p:pbytea;len:integer);
//############################################################################//
implementation
//############################################################################//
const packet_full_mark=2047;
//############################################################################//
var
last_frame:integer=0;
partial_packet:boolean=false;
packet_buf:array[0..2*1024-1]of byte;
packet_off:integer=0;
//############################################################################//
procedure parse_70(p:pbytea;len:integer);
var h,m,s,ms:integer;
begin
 h:=p[8];
 m:=p[9];
 s:=p[10];
 ms:=p[11]*4;

 last_time:=h*3600*1000+m*60*1000+s*1000+ms;

 if no_time_yet then begin  
  no_time_yet:=false;
  first_time:=last_time;
 end;

 if not quiet then write('Onboard time: ',trimsl(stri(h),2,'0'),':',trimsl(stri(m),2,'0'),':',trimsl(stri(s),2,'0'),'.',trimsl(stri(ms),3,'0'));
 if not quiet and md_debug then writeln;
end;
//############################################################################//
procedure act_apd(p:pbytea;len:integer;apd,pck_cnt:integer);
var mcu_id,scan_hdr,seg_hdr,q:integer;
//f:file;
begin
 mcu_id:=p[0];
 scan_hdr:=(p[1] shl 8) or p[2];
 seg_hdr:=(p[3] shl 8) or p[4];
 q:=p[5];

 if md_debug then writeln('apd=',apd:2,' pck_cnt=',pck_cnt:5,' mcu_id=',mcu_id:3,' scan_hdr=',scan_hdr,' seg_hdr=',seg_hdr,' q=',q);
 {
 assignfile(f,'tst_'+stri(pck_cnt)+'.apd'+stri(apd));
 rewrite(f,1);
 blockwrite(f,p[6],len-6);
 closefile(f);
 }

 mj_dec_mcus(@p[6],len-6,apd,pck_cnt,mcu_id,q);
end;
//############################################################################//
procedure parse_apd(p:pbytea;len:integer);
var w:word;
//day,us,ver,typ:integer
ms,sec,apd,pck_cnt,len_pck:integer;
begin
 w:=(p[0] shl 8) or p[1];
 //ver:=w shr 13;
 //typ:=(w shr 12) and 1;
 sec:=(w shr 11) and 1;
 apd:=w and $7FF;

 pck_cnt:=((p[2] shl 8) or p[3]) and $3FFF;
 len_pck:=(p[4] shl 8) or p[5];

 //day:=(p[6] shl 8) or p[7];
 ms:=(p[8] shl 24) or (p[9] shl 16) or (p[10] shl 8) or p[11];
 //us:=(p[12] shl 8) or p[13];

 if md_debug then writeln('sec=',sec,' (pck: ',len_pck+1:4,'/total: ',len:4,') ms=',ms:8);

 if apd=70 then parse_70(@p[14],len-14)
           else act_apd(@p[14],len-14,apd,pck_cnt);
end;
//############################################################################//
function parse_partial(p:pbytea;len:integer):integer;
var len_pck:integer;
begin
 result:=0;
 if len<6 then begin partial_packet:=true;exit;end;

 len_pck:=(p[4] shl 8) or p[5];
 if len_pck>=len-6 then begin partial_packet:=true;exit;end;

 parse_apd(p,len_pck+1);

 partial_packet:=false;
 result:=len_pck+6+1;
end;
//############################################################################//
procedure parse_cvcdu(p:pbytea;len:integer);
var n,data_len,off:integer;
ver,ssid,fid:integer;
frame_cnt:integer;
hdr_mark:byte;
hdr_off:word;
w:word;
begin
 w:=(p[0] shl 8) or p[1];
 ver:=w shr 14;
 ssid:=(w shr 6)and $FF;
 fid:=w and $3F;

 frame_cnt:=(p[2] shl 16)or(p[3] shl 8)or p[4];

 w:=(p[8] shl 8) or p[9];
 hdr_mark:=w shr 11;
 hdr_off:=w and $7FF;

 if md_debug then writeln('ver=',ver:1,' ssid=',ssid:2,' fid=',fid:2,' frame_cnt=',frame_cnt:7,' hdr_mark=',hdr_mark:3,' hdr_off=',hdr_off:3);
 if (ver=0)or(fid=0) then exit; //Empty packet

 data_len:=len-10;
 if frame_cnt=last_frame+1 then begin
  if partial_packet then begin  
   if hdr_off=packet_full_mark then begin      //Packet could be larger than one frame
    hdr_off:=len-10;
    move(p[10],packet_buf[packet_off],hdr_off);
    packet_off:=packet_off+hdr_off;
   end else begin                              
    move(p[10],packet_buf[packet_off],hdr_off);
    n:=parse_partial(@packet_buf[0],packet_off+hdr_off);
   end;
  end;
 end else begin
  if hdr_off=packet_full_mark then exit;    //Packet could be larger than one frame
  partial_packet:=false;
  packet_off:=0;
 end;
 last_frame:=frame_cnt;

 data_len:=data_len-hdr_off;
 off:=hdr_off;
 while data_len>0 do begin
  n:=parse_partial(@p[10+off],data_len);
  if partial_packet then begin
   packet_off:=data_len;
   move(p[10+off],packet_buf[0],packet_off);
   break;
  end else begin
   off:=off+n;
   data_len:=data_len-n;
  end;
 end;
end;
//############################################################################//
begin
end. 
//############################################################################//

