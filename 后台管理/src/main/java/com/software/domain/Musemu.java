package com.software.domain;
public class Musemu {
	private String buildtime;
	private String cnum;
	private String ctype;
	private String evaluate;
	private String grade;
	private int mid;
	private String mimg;
	private String mname;
	private String enumb;
	private String mtype;
	private String opentime;
	private String ticket;
	
	public Musemu() {
		// TODO Auto-generated constructor stub
	}

	public Musemu(String buildtime, String cnum, String ctype, String evaluate, String grade, int mid, String mimg,
			String mname, String enumb, String mtype, String opentime, String ticket) {
		super();
		this.buildtime = buildtime;
		this.cnum = cnum;
		this.ctype = ctype;
		this.evaluate = evaluate;
		this.grade = grade;
		this.mid = mid;
		this.mimg = mimg;
		this.mname = mname;
		this.enumb = enumb;
		this.mtype = mtype;
		this.opentime = opentime;
		this.ticket = ticket;
	}

	@Override
	public String toString() {
		return "Musemu [buildtime=" + buildtime + ", cnum=" + cnum + ", ctype=" + ctype + ", evaluate=" + evaluate
				+ ", grade=" + grade + ", mid=" + mid + ", mimg=" + mimg + ", mname=" + mname + ", enumb=" + enumb
				+ ", mtype=" + mtype + ", opentime=" + opentime + ", ticket=" + ticket + "]";
	}

	public String getBuildtime() {
		return buildtime;
	}

	public void setBuildtime(String buildtime) {
		this.buildtime = buildtime;
	}

	public String getCnum() {
		return cnum;
	}

	public void setCnum(String cnum) {
		this.cnum = cnum;
	}

	public String getCtype() {
		return ctype;
	}

	public void setCtype(String ctype) {
		this.ctype = ctype;
	}

	public String getEvaluate() {
		return evaluate;
	}

	public void setEvaluate(String evaluate) {
		this.evaluate = evaluate;
	}

	public String getGrade() {
		return grade;
	}

	public void setGrade(String grade) {
		this.grade = grade;
	}

	public int getMid() {
		return mid;
	}

	public void setMid(int mid) {
		this.mid = mid;
	}

	public String getMimg() {
		return mimg;
	}

	public void setMimg(String mimg) {
		this.mimg = mimg;
	}

	public String getMname() {
		return mname;
	}

	public void setMname(String mname) {
		this.mname = mname;
	}

	public String getEnumb() {
		return enumb;
	}

	public void setEnumb(String enumb) {
		this.enumb = enumb;
	}

	public String getMtype() {
		return mtype;
	}

	public void setMtype(String mtype) {
		this.mtype = mtype;
	}

	public String getOpentime() {
		return opentime;
	}

	public void setOpentime(String opentime) {
		this.opentime = opentime;
	}

	public String getTicket() {
		return ticket;
	}

	public void setTicket(String ticket) {
		this.ticket = ticket;
	}

	
	
	
	
}
