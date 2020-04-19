package com.software.domain;
public class Video {
	private int vid;
	private String uid;
	private int mid;
	private String vname;
	private String vaddr;
	private String vinfo;
	
	 public Video() {
		// TODO Auto-generated constructor stub
	}

	public Video(int vid, String uid, int mid, String vname, String vaddr, String vinfo) {
		super();
		this.vid = vid;
		this.uid = uid;
		this.mid = mid;
		this.vname = vname;
		this.vaddr = vaddr;
		this.vinfo = vinfo;
	}

	@Override
	public String toString() {
		return "Video [vid=" + vid + ", uid=" + uid + ", mid=" + mid + ", vname=" + vname + ", vaddr=" + vaddr
				+ ", vinfo=" + vinfo + "]";
	}

	public int getVid() {
		return vid;
	}

	public void setVid(int vid) {
		this.vid = vid;
	}

	public String getUid() {
		return uid;
	}

	public void setUid(String uid) {
		this.uid = uid;
	}

	public int getMid() {
		return mid;
	}

	public void setMid(int mid) {
		this.mid = mid;
	}

	public String getVname() {
		return vname;
	}

	public void setVname(String vname) {
		this.vname = vname;
	}

	public String getVaddr() {
		return vaddr;
	}

	public void setVaddr(String vaddr) {
		this.vaddr = vaddr;
	}

	public String getVinfo() {
		return vinfo;
	}

	public void setVinfo(String vinfo) {
		this.vinfo = vinfo;
	}
	 
	 
}
