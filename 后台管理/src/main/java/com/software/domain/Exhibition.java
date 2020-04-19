package com.software.domain;
public class Exhibition {
	private int mid;
	private String eid;
	private int etheme;
	private String etime;
	private String introduce;
	
	public Exhibition() {
		// TODO Auto-generated constructor stub
	}

	public Exhibition(int mid, String eid, int etheme, String etime, String introduce) {
		super();
		this.mid = mid;
		this.eid = eid;
		this.etheme = etheme;
		this.etime = etime;
		this.introduce = introduce;
	}

	@Override
	public String toString() {
		return "Exhibition [mid=" + mid + ", eid=" + eid + ", etheme=" + etheme + ", etime=" + etime + ", introduce="
				+ introduce + "]";
	}

	public int getMid() {
		return mid;
	}

	public void setMid(int mid) {
		this.mid = mid;
	}

	public String getEid() {
		return eid;
	}

	public void setEid(String eid) {
		this.eid = eid;
	}

	public int getEtheme() {
		return etheme;
	}

	public void setEtheme(int etheme) {
		this.etheme = etheme;
	}

	public String getEtime() {
		return etime;
	}

	public void setEtime(String etime) {
		this.etime = etime;
	}

	public String getIntroduce() {
		return introduce;
	}

	public void setIntroduce(String introduce) {
		this.introduce = introduce;
	}
	
	
}
